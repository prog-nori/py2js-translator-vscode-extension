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
        return ''
    def convert_Dict(self, nodes):
        return ''
    def convert_Set(self, nodes):
        return ''
    def convert_ListComp(self, nodes):
        return ''
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
        return ''

    def convert_Call(self, nodes):
        """
        関数の呼び出し処理。キーワード付きのやーつ非対応
        """
        func = self.parse(nodes.func)
        args = self.parse(nodes.args)
        keywords = self.parse(nodes.keywords)
        arguments = ', '.join(args)
        result = f'{func}({arguments})'
        return result

    def convert_FormattedValue(self, nodes):
        return ''
    def convert_JoinedStr(self, nodes):
        return ''

    def convert_Constant(self, nodes):
        # value = self.parse(nodes.value)
        return str(nodes.value)

    def convert_Attribute(self, nodes):
        value = self.parse(nodes.value)
        attr = self.parse(nodes.attr)
        return '.'.join([value, attr])

    def convert_Subscript(self, nodes):
        return ''
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
