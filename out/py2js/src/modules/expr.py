#! /usr/bin/env python3
#! -*- coding: utf-8 -*-
from src.modules.nodeParser import NodeParser

class Expr(NodeParser):
    def convert_BoolOp(self, nodes):
        return ''

    def convert_NamedExpr(self, nodes):
        return ''

    def convert_BinOp(self, nodes):
        left = self.parse(nodes.left)
        op = self.parse(nodes.op)
        right = self.parse(nodes.right)
        binOp_statement = f'{left} {op} {right}'
        return binOp_statement

    def convert_UnaryOp(self, nodes):
        return ''

    def convert_Lambda(self, nodes):
        return ''

    def convert_IfExp(self, nodes):
        test = self.parse(nodes.test)
        body = ''.join(self.parse(nodes.body))
        # orelse = self.parse(nodes.orelse)
        state = f'{test}? {body}'
        # if orelse:
        if orelse := self.parse(nodes.orelse):
            state += f': {orelse}'
        else:
            state += f': null'
        return state

    def convert_Dict(self, nodes):
        keys = self.parse(nodes.keys)
        values = self.parse(nodes.values)
        aDict = dict()
        remove_quart = lambda aString: aString.replace('\'', '')
        for anIndex, aKey in enumerate(keys):
            aDict[remove_quart(aKey)] = remove_quart(values[anIndex])
        aString = str(aDict)
        self.indent.increment()
        aString = aString.replace('{', f'{{\n{self.indent.get()}')
        aString = aString.replace(', ', f',\n{self.indent.get()}')
        self.indent.decrement()
        aString = aString.replace('}', f'\n{self.indent.get()}}}\n')
        return aString

    def convert_Set(self, nodes):
        return ''

    def convert_ListComp(self, nodes):
        elt = self.parse(nodes.elt)
        self.options.add('elt', elt)
        namespace = '__listcomp__'
        before_scopelist_len = len(self.current_scope_list)
        self.current_scope_list.append(namespace)
        generators = ''.join(self.parse(nodes.generators))
        del self.current_scope_list[before_scopelist_len:]
        self.options.remove('elt')
        state = generators
        return state

    def convert_SetComp(self, nodes):
        return ''

    def convert_DictComp(self, nodes):
        return ''

    def convert_GeneratorExp(self, nodes):
        return ''

    def convert_Await(self, nodes):
        return ''

    def convert_Yield(self, nodes):
        return ''

    def convert_YieldFrom(self, nodes):
        return ''

    def convert_Compare(self, nodes):
        left = self.parse(nodes.left)
        ops = self.parse(nodes.ops)
        comparators = self.parse(nodes.comparators)
        state = left
        if len(comparators) == len(ops):
            for idx, aComparator in enumerate(comparators):
                state += f' {ops[idx]} {aComparator}'
        return state

    def convert_Call(self, nodes):
        """
        関数の呼び出し処理。キーワード付きのやーつ非対応
        """
        func = self.parse(nodes.func)
        args = self.parse(nodes.args)
        keywords = self.parse(nodes.keywords)
        arguments = ', '.join(args)
        func = 'console.log' if func == 'print' else func
        new = 'new ' if func.istitle() else ''
        result = f'{new}{func}({arguments})'
        return result

    def convert_FormattedValue(self, nodes):
        return ''
    def convert_JoinedStr(self, nodes):
        return ''

    def convert_Constant(self, nodes):
        value = nodes.value
        constant_statement = ''
        if isinstance(value, str):
            constant_statement = f'\'{value}\''
        else:
            constant_statement = str(value)
        return constant_statement

    def convert_Attribute(self, nodes):
        value = self.parse(nodes.value)
        attr = self.parse(nodes.attr)
        if value == 'self':
            return '.'.join(['this', attr])
        else:
            return '.'.join([value, attr])

    def convert_Subscript(self, nodes):
        """
        保留
        """
        value = self.parse(nodes.value)
        slice = self.parse(nodes.slice)
        state = f'{value}[{str(slice)}]'
        return state

    def convert_Starred(self, nodes):
        return ''
    def convert_Name(self, nodes):
        id = self.parse(nodes.id)
        return id

    def convert_List(self, nodes):
        elts = self.parse(nodes.elts)
        item = ', '.join(elts)
        return f'[{item}]'

    def convert_Tuple(self, nodes):
        return ''
    def convert_Slice(self, nodes):
        return ''
