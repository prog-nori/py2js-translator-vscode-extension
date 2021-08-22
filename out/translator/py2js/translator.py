#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

import ast
from py2js.modules.mod import Mod
from py2js.modules.stmt import Stmt
from py2js.modules.standard import Standard
from py2js.modules.arguments import Arguments
from py2js.modules.arg import Arg

class Translator:
    def __init__(self, abstract_tree):
        self.abstract_tree = abstract_tree
        self.mod = Mod(self.parse)
        self.stmt = Stmt(self.parse)
        self.standard = Standard(self.parse)
        self.arguments = Arguments(self.parse)
        self.arg = Arg(self.parse)
        self.synbols = [
            # mod
            {
                'type': ast.Module,
                'function': self.mod.convert_Module
            },{
                'type': ast.Interactive,
                'function': self.mod.convert_Interactive
            },{
                'type': ast.Expression,
                'function': self.mod.convert_Expression
            },{
                'type': ast.FunctionType,
                'function': self.mod.convert_FunctionType
            },
            # stmt
            {
                'type': ast.FunctionDef,
                'function': self.stmt.convert_FunctionDef
            },
            # {
            #     'type': ast.AsyncFunctionDef,
            #     'function': self.stmt.convert_AsyncFunctionDef
            # },
            {
                'type': ast.ClassDef,
                'function': self.stmt.convert_ClassDef
            },{
                'type': ast.Return,
                'function': self.stmt.convert_Return
            },
            # arguments
            {
                'type': ast.arguments,
                'function': self.arguments.convert_Arguments
            },
            {
                'type': ast.arg,
                'function': self.arg.convert_Arg
            },
            # ohters
            {
                'type': list,
                'function': self.standard.convert_List
            },{
                'type': dict,
                'function': self.standard.convert_Dict
            },{
                'type': str,
                'function': self.standard.convert_Str
            },
        ]
        return

    def parse(self, nodes):
        result = None
        ifTrueThen = lambda theClass, theFunction: theFunction() if isinstance(nodes, theClass) else None
        self.mod.set_nodes(nodes)
        self.stmt.set_nodes(nodes)
        self.standard.set_nodes(nodes)
        self.arguments.set_nodes(nodes)
        self.arg.set_nodes(nodes)
        aList = []

        for aSymbol in self.synbols:
            response = ifTrueThen(aSymbol.get('type'), aSymbol.get('function'))
            aList.append(response)
        for anItem in aList:
            if anItem is not None:
                return anItem
        return str(result)
    
    def run(self):
        result = self.parse(self.abstract_tree)
        from pprint import pprint
        print('=== result ===')
        pprint(result)
        return