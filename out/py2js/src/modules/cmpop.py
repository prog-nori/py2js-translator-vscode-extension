#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from src.modules.nodeParser import NodeParser


class Cmpop(NodeParser):

    def convert_Eq(self, nodes):
        return '=='

    def convert_NotEq(self, nodes):
        return '!='

    def convert_Lt(self, nodes):
        return '<'

    def convert_LtE(self, nodes):
        return '<=' # 行列乗算

    def convert_Gt(self, nodes):
        return '>'

    def convert_GtE(self, nodes):
        return '>='

    def convert_Is(self, nodes):
        return 'is'

    def convert_IsNot(self, nodes):
        return 'is not'

    def convert_In(self, nodes):
        return 'in'

    def convert_NotIn(self, nodes):
        return 'not in'