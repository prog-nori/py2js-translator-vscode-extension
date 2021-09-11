#! /usr/bin/env python3
#! -*- coding: utf-8 -*-
from src.modules.nodeParser import NodeParser
from src.modules.module_options.for_extension import (
    atopy
)

class Stmt(NodeParser):
    def convert_FunctionDef(self, nodes):
        name = self.parse(nodes.name)
        args = self.parse(nodes.args)
        self.indent.increment()
        body = self.body_joiner(self.parse(nodes.body), self.indent)
        self.indent.decrement()
        functinon_statement = ''
        anIndent = lambda: self.indent.get()
        if self.options.get('in-class'):
            if name == '__init__':
                functinon_statement = f'constructor({args}) {{\n{body}\n'
            else:
                functinon_statement = f'{name}({args}) {{\n{body}\n'
        else:
            functinon_statement = f'function {name}({args}) {{\n{body}\n'
        functinon_statement += f'{anIndent()}}}\n'
        return functinon_statement

    def convert_AsyncFunctionDef(self, nodes):
        return f'{self.indent.get()}async {self.convert_FunctionDef(nodes, self.parse)}'

    def convert_ClassDef(self, nodes):
        name = self.parse(nodes.name)
        self.options.add('in-class', True)
        bases_ = self.parse(nodes.bases)
        bases = bases_[0] if len(bases_) > 0 else ''
        self.indent.increment()
        body = self.body_joiner(self.parse(nodes.body), self.indent)
        self.indent.decrement()
        self.options.remove('in-class')
        anIndent = lambda: self.indent.get()
        result = ''
        if len(bases) > 0:
            result = f'{anIndent()}class {name} extends {bases} {{\n{body}}}\n'
        else:
            result = f'{anIndent()}class {name} {{\n{body}}}\n'
        return result

    def convert_Return(self, nodes):
        value = self.parse(nodes.value)
        result = ''
        if value:
            result = f'return {value}\n'
        else:
            result = 'return\n'
        return result

    def convert_Delete(self, nodes):
        return ''

    def convert_Assign(self, nodes):
        targets = self.parse(nodes.targets)
        theTarget = ' = '.join(targets)
        value = self.parse(nodes.value)
        # print(targets, value, ':', ' = '.join(targets), '=', value)
        return ' = '.join([theTarget, value])

    def convert_AugAssign(self, nodes):
        target = self.parse(nodes.target)
        op = self.parse(nodes.op)
        value = self.parse(nodes.value)
        augAssign_statement = f'{target} {op}= {value}'
        return augAssign_statement

    def convert_AnnAssign(self, nodes):
        return ''

    def convert_For(self, nodes):
        """
        orelse以外実装
        """
        target = self.parse(nodes.target)
        iter = self.parse(nodes.iter)
        self.indent.increment()
        body = self.body_joiner(self.parse(nodes.body), self.indent)
        self.indent.decrement()
        orelse = self.parse(nodes.orelse)
        for_statement = ''
        times, data_type = atopy(iter)
        # orelseはbreakしないでループを抜け出した時のみはっか

        # print('===for===')
        # print('target:', target)
        # print('iter:', iter, type(iter), type(nodes.iter))
        # print('isList', data_type)
        # print('body:', body)
        # print('type:', times, data_type)

        done = False
        if data_type == 'list':
            for_statement = f'for(const {target} of {iter}) {{\n{body}\n'
            done = True
        elif data_type == 'dict' or data_type == 'else':
            for_statement = f'for(const {target} in {iter}) {{\n{body}\n'
            done = True
        elif data_type == 'range':
            # 内部のループに対して[i]を与える処理はまだ実装していない
            for_statement = f'for(let i = 0; i < {times}; i++) {{\n{body}\n'
            done = True
        
        if done:
            for_statement += f'{self.indent.get()}}}\n'
        # else:
        #     for_statement = f'for(let i = 0; i < {iter}.length; i++) {{\n{body}\n}}\n'
        # enumerate処理未実装
        # 例外処理未実装
        return for_statement

    def convert_AsyncFor(self, nodes):
        return ''

    def convert_While(self, nodes):
        test = self.parse(nodes.test)
        self.indent.increment()
        body = self.body_joiner(self.parse(nodes.body), self.indent)
        self.indent.decrement()
        # orelse = self.parse(nodes.orelse)
        # orelseはまだ実装しない
        while_statement = f'while({test}) {{\n{body}\n'
        while_statement += f'{self.indent.get()}}}\n'
        return while_statement

    def convert_If(self, nodes):
        test = self.parse(nodes.test)
        body = '\n'.join(self.parse(nodes.body))
        orelse = self.parse(nodes.orelse)
        aList = list()
        anIndent = lambda: self.indent.get()
        aList.append(f'if({test}){{')
        self.indent.increment()
        aList.append(f'{anIndent()}{body}')
        self.indent.decrement()
        if test == '__name__ == \'__main__\'':
            return body
        if not orelse == []:
            else_state = ''.join(orelse)
            if orelse[0][:2] == 'if':
                aList.append(f'{anIndent()}}} else {else_state}')
            else:
                aList.append(f'{anIndent()}}} else {{')
                self.indent.increment()
                aList.append(f'{anIndent()}{else_state}')
                self.indent.decrement()
                aList.append(f'{anIndent()}}}')
        else:
            aList.append(f'{anIndent()}}}')
        state = '\n'.join(aList)
        return state

    def convert_With(self, nodes):
        return ''

    def convert_AsyncWith(self, nodes):
        return ''

    def convert_Raise(self, nodes):
        return ''

    def convert_Try(self, nodes):
        orelse = ''.join(self.parse(nodes.orelse))
        has_orelse = True if orelse != '' else False
        self.options.add('else', has_orelse)
        self.indent.increment()
        finalbody = lambda: self.body_joiner(self.parse(nodes.finalbody), self.indent)
        self.indent.decrement()
        handlers = lambda: ''.join(self.parse(nodes.handlers))
        has_finally = bool(finalbody() != '')
        state = ''
        anIndent = lambda: self.indent.get()

        def get_try_catch():
            """
            try-catchを作る
            """
            self.indent.increment()
            body = self.body_joiner(self.parse(nodes.body), self.indent)
            self.indent.decrement()
            aList = list()
            aList.append(f'try {{')
            aList.append(f'{body}')
            aList.append(f'{handlers()}')
            return '\n'.join(aList)

        if has_orelse:
            if has_finally:
                # try-catch-else-finally
                try_catch_else_finally = list()
                try_catch_else_finally.append(f'try{{')
                self.indent.increment()
                try_catch_else_finally.append(f'{anIndent()}let success = true')
                try_catch_else_finally.append(f'{anIndent()}{get_try_catch()}')
                try_catch_else_finally.append(f'{anIndent()}if(success){{')
                self.indent.increment()
                try_catch_else_finally.append(f'{anIndent()}{orelse}')
                self.indent.decrement()
                try_catch_else_finally.append(f'{anIndent()}}}')
                self.indent.decrement()
                try_catch_else_finally.append(f'{anIndent()}}}\n')
                try_catch_else_finally.append(f'{anIndent()}}} finally {{')
                self.indent.increment()
                try_catch_else_finally.append(f'{finalbody()}')
                self.indent.decrement()
                try_catch_else_finally.append(f'{anIndent()}}}\n')
                state = '\n'.join(try_catch_else_finally)
            else:
                # try-catch-else
                try_catch_else = list()
                try_catch_else.append(f'let success = true')
                try_catch_else.append(f'{anIndent()}{get_try_catch()}')
                try_catch_else.append(f'{anIndent()}}}')
                try_catch_else.append(f'{anIndent()}if(success){{')
                self.indent.increment()
                try_catch_else.append(f'{anIndent()}{orelse}')
                self.indent.decrement()
                try_catch_else.append(f'{anIndent()}}}')
                state = '\n'.join(try_catch_else)
        else:
            if has_finally:
                # try-catch-finally
                try_catch_finally = list()
                try_catch_finally.append(get_try_catch())
                try_catch_finally.append(f'{anIndent()}}} finally {{')
                self.indent.increment()
                try_catch_finally.append(f'{finalbody()}')
                self.indent.decrement()
                try_catch_finally.append(f'{anIndent()}}}\n')
                state = '\n'.join(try_catch_finally)
            else:
                # try-catch
                try_catch = list()
                try_catch.append(get_try_catch())
                try_catch.append(f'{anIndent()}}}\n')
                state = '\n'.join(try_catch)
        self.options.remove('else')
        return state

    def convert_Assert(self, nodes):
        return ''

    def convert_Import(self, nodes):
        return ''

    def convert_ImportFrom(self, nodes):
        return ''

    def convert_Global(self, nodes):
        return ''

    def convert_Nonlocal(self, nodes):
        return ''

    def convert_Expr(self, nodes):
        value = self.parse(nodes.value)
        return value

    def convert_Pass(self, nodes):
        return ''

    def convert_Break(self, nodes):
        return 'break'

    def convert_Continue(self, nodes):
        return 'continue'
        