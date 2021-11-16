#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from py2js.util.jscode import JsCode
from py2js.modules.nodeParser import NodeParser


class Cmpop(NodeParser):

    def convert_Eq(self):
        return JsCode('==')

    def convert_NotEq(self):
        return JsCode('!=')

    def convert_Lt(self):
        return JsCode('<')

    def convert_LtE(self):
        return JsCode('<=')

    def convert_Gt(self):
        return JsCode('>')

    def convert_GtE(self):
        return JsCode('>=')

    def convert_Is(self):
        return JsCode('===')

    def convert_IsNot(self):
        return JsCode('!==')

    def convert_In(self):
        return JsCode('in')

    def convert_NotIn(self):
        return JsCode('not in')