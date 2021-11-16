#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from py2js.modules.nodeParser import NodeParser
from py2js.util.jscode import JsCode

class Arg(NodeParser):

    def convert_Arg(self):
        jscode: JsCode = JsCode()
        # print('arg!!', self.nodes.__dict__)
        jscode.add(self.nodes.__dict__.get('arg'))
        # jscode.add(v.get('arg', ''))
        return jscode