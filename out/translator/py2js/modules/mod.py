#! /usr/bin/env python3
#! -*- coding:utf-8 -*-
from py2js.modules.parseNodes import ParseNodes
from ast2js.src.util.jscode import JsCode

class Mod(ParseNodes):
    """
    astモジュールで定義されているModに含まれるノードの解析を行う
    """    
    def convert_Module(self):
        jscode: JsCode = JsCode()
        body = self.recursional_function(self.nodes.body)
        jscode.add(body)
        return jscode
    
    def convert_Interactive(self):
        jscode: JsCode = JsCode()
        return jscode
    
    def convert_Expression(self):
        jscode: JsCode = JsCode()
        body = self.recursional_function(self.nodes.body)
        jscode.addln(body)
        return jscode

    def convert_FunctionType(self):
        jscode: JsCode = JsCode()
        return jscode