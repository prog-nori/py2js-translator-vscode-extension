#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

import ast
import re
from py2js.modules.mod import Mod
from py2js.modules.stmt import Stmt

class Translator:
    def __init__(self, abstract_tree):
        self.abstract_tree = abstract_tree
        self.mod = Mod(self.parse)
        self.stmt = Stmt(self.parse)
        return

    # def ifTrueThen(self, aCondition: bool, theFunction):
    #     if aCondition:
    #         theFunction()
    #     return

    def parse(self, nodes):
        result = None
        ifTrueThen = lambda theClass, theFunction: theFunction() if isinstance(nodes, theClass) else None
        self.mod.set_nodes(nodes)
        self.stmt.set_nodes(nodes)

        # mod
        ifTrueThen(ast.Module, self.mod.convert_Module)
        ifTrueThen(ast.Interactive, self.mod.convert_Interactive)
        ifTrueThen(ast.Expression, self.mod.convert_Expression)
        ifTrueThen(ast.FunctionType, self.mod.convert_FunctionType)

        # stmt
        ifTrueThen(ast.FunctionDef, self.stmt.convert_FunctionDef)
        #
        ifTrueThen(ast.ClassDef, self.stmt.convert_ClassDef)

        if isinstance(nodes, list):
            print('list')
            for aNode in nodes:
                print(aNode)
                self.parse(aNode)
        elif isinstance(nodes, dict):
            for _, v in nodes.items():
                self.parse(v)
        elif isinstance(nodes, str):
            nodes
        return result
    
    def run(self):
        result = self.parse(self.abstract_tree)
        from pprint import pprint
        print('=== result ===')
        pprint(result)
        return