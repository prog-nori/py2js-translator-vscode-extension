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
        body = '\n'.join(self.parse(nodes.body))
        frame = 'function {}({}){{\n{}}}\n'
        return frame.format(name, args, body)

    def convert_AsyncFunctionDef(self, nodes):
        return f'async {self.convert_FunctionDef(nodes, self.parse)}'

    def convert_ClassDef(self, nodes):
        name = self.parse(nodes.name)
        bases_ = self.parse(nodes.bases)
        bases = bases_[0] if len(bases_) > 0 else ''
        body = '\n'.join(self.parse(nodes.body))
        result = ''
        if len(bases) > 0:
            result = 'class {} extends {} {{\n{}}}\n'.format(name, bases, body)
        else:
            result = 'class {} {{\n{}}}\n'.format(name, body)
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
        return ''

    def convert_AnnAssign(self, nodes):
        return ''

    def convert_For(self, nodes):
        """
        orelse以外実装
        """
        target = self.parse(nodes.target)
        iter = self.parse(nodes.iter)
        body = '\n'.join(self.parse(nodes.body))
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

        if data_type == 'list':
            for_statement = f'for(const {target} of {iter}) {{\n{body}\n}}\n'
        elif data_type == 'dict':
            for_statement = f'for(const {target} in {iter}) {{\n{body}\n}}\n'
        elif data_type == 'range':
            # 内部のループに対して[i]を与える処理はまだ実装していない
            for_statement = f'for(let i = 0; i < {times}; i++) {{\n{body}\n}}\n'
        # enumerate処理未実装
        # 例外処理未実装
        return for_statement

    def convert_AsyncFor(self, nodes):
        return ''

    def convert_While(self, nodes):
        return ''

    def convert_If(self, nodes):
        return ''

    def convert_With(self, nodes):
        return ''

    def convert_AsyncWith(self, nodes):
        return ''

    def convert_Raise(self, nodes):
        return ''

    def convert_Try(self, nodes):
        return ''

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
        return ''

    def convert_Continue(self, nodes):
        return ''
        