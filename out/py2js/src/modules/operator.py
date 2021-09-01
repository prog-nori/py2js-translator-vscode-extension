#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from src.modules.nodeParser import NodeParser


class Operator(NodeParser):

    def convert_Add(self, nodes):
        return '+'

    def convert_Sub(self, nodes):
        return '-'

    def convert_Mult(self, nodes):
        return '*'

    def convert_MatMult(self, nodes):
        return '@' # 行列乗算

    def convert_Div(self, nodes):
        return '/'

    def convert_Mod(self, nodes):
        return '%'

    def convert_Pow(self, nodes):
        return '**' # power

    def convert_LShift(self, nodes):
        return '<<'

    def convert_RShift(self, nodes):
        return '>>'

    def convert_BitOr(self, nodes):
        return '|'

    def convert_BitXor(self, nodes):
        return '^'

    def convert_BitAnd(self, nodes):
        return '&'

    def convert_FloorDiv(self, nodes):
        return '//'