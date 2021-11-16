#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from py2js.util.jscode import JsCode
from py2js.modules.nodeParser import NodeParser


class Operator(NodeParser):
    def convert_Add(self):
        return JsCode('+')

    def convert_Sub(self):
        return JsCode('-')

    def convert_Mult(self):
        return JsCode('*')

    def convert_MatMult(self):
        return JsCode('@') # 行列乗算

    def convert_Div(self):
        return JsCode('/')

    def convert_Mod(self):
        return JsCode('%')

    def convert_Pow(self):
        return JsCode('**') # power

    def convert_LShift(self):
        return JsCode('<<')

    def convert_RShift(self):
        return JsCode('>>')

    def convert_BitOr(self):
        return JsCode('|')

    def convert_BitXor(self):
        return JsCode('^')

    def convert_BitAnd(self):
        return JsCode('&')

    def convert_FloorDiv(self):
        return JsCode('//')