#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

from py2js.modules.nodeParser import NodeParser
from py2js.util.jscode import JsCode

class Standard(NodeParser):
    def convert_List(self):
        jscode: JsCode = JsCode()
        # print('ウエーい')
        for aNode in self.nodes:
            # print('aNode:', aNode, aNode.__dict__)
            res = self.recursional_function(aNode)
            # print('aNode res:', res)
            jscode.add(res)
            # jscode.add(self.recursional_function(aNode))
        return jscode
    
    def convert_Dict(self):
        jscode: JsCode = JsCode()
        for _, aNode in self.nodes.items():
            jscode.add(self.recursional_function(aNode))
        return jscode

    def convert_Str(self):
        jscode: JsCode = JsCode()
        jscode.add(self.nodes)
        return jscode