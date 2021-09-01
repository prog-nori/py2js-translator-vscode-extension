#! /usr/bin/env python3
#! -*- coding: utf-8 -*-
from src.modules.nodeParser import NodeParser

class Expr(NodeParser):
    def convert_BoolOp(self, nodes):
        return ''
    def convert_NamedExpr(self, nodes):
        return ''
    def convert_BinOp(self, nodes):
        return ''
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
        return ''
    def convert_FormattedValue(self, nodes):
        return ''
    def convert_JoinedStr(self, nodes):
        return ''

    def convert_Constant(self, nodes):
        # value = self.parse(nodes.value)
        return str(nodes.value)

    def convert_Attribute(self, nodes):
        return ''
    def convert_Subscript(self, nodes):
        return ''
    def convert_Starred(self, nodes):
        return ''
    def convert_Name(self, nodes):
        id = self.parse(nodes.id)
        return id

    def convert_List(self, nodes):
        return ''
    def convert_Tuple(self, nodes):
        return ''
    def convert_Slice(self, nodes):
        return ''
