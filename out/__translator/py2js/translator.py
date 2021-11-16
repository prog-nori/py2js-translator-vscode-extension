#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

import ast
from py2js.modules.mod import Mod
from py2js.modules.stmt import Stmt
from py2js.modules.expr import Expr
from py2js.modules.standard import Standard
from py2js.modules.arguments import Arguments
from py2js.modules.arg import Arg
from py2js.modules.cmpop import Cmpop
from py2js.modules.operator import Operator

class Translator:
    def __init__(self, abstract_tree):
        self.abstract_tree = abstract_tree
        self.mod = Mod(self.parse)
        self.stmt = Stmt(self.parse)
        self.expr = Expr(self.parse)
        self.standard = Standard(self.parse)
        self.arguments = Arguments(self.parse)
        self.arg = Arg(self.parse)
        self.cmpop = Cmpop(self.parse)
        self.operator = Operator(self.parse)
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
            },{
                'type': ast.Assign,
                'function': self.stmt.convert_Assign
            },{
                'type': ast.AugAssign,
                'function': self.stmt.convert_AugAssign
            },{
                'type': ast.Expr,
                'function': self.stmt.convert_Expr
            },
            # expr
            {
                'type': ast.Call,
                'function': self.expr.convert_Call
            },{
                'type': ast.Name,
                'function': self.expr.convert_Name
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
            # cmpop
            {
                'type': ast.Eq,
                'function': self.cmpop.convert_Eq
            },{
                'type': ast.NotEq,
                'function': self.cmpop.convert_NotEq
            },{
                'type': ast.Lt,
                'function': self.cmpop.convert_Lt
            },{
                'type': ast.LtE,
                'function': self.cmpop.convert_LtE
            },{
                'type': ast.Gt,
                'function': self.cmpop.convert_Gt
            },{
                'type': ast.GtE,
                'function': self.cmpop.convert_GtE
            },{
                'type': ast.Is,
                'function': self.cmpop.convert_Is
            },{
                'type': ast.IsNot,
                'function': self.cmpop.convert_IsNot
            },{
                'type': ast.In,
                'function': self.cmpop.convert_In
            },{
                'type': ast.NotIn,
                'function': self.cmpop.convert_NotIn
            },
            # operator
            {
                'type': ast.Add,
                'function': self.operator.convert_Add
            },{
                'type': ast.Sub,
                'function': self.operator.convert_Sub
            },{
                'type': ast.Mult,
                'function': self.operator.convert_Mult
            },{
                'type': ast.Div,
                'function': self.operator.convert_Div
            },{
                'type': ast.Mod,
                'function': self.operator.convert_Mod
            },{
                'type': ast.Pow,
                'function': self.operator.convert_Pow
            },{
                'type': ast.LShift,
                'function': self.operator.convert_LShift
            },{
                'type': ast.RShift,
                'function': self.operator.convert_RShift
            },{
                'type': ast.BitOr,
                'function': self.operator.convert_BitOr
            },{
                'type': ast.BitXor,
                'function': self.operator.convert_BitXor
            },{
                'type': ast.BitAnd,
                'function': self.operator.convert_BitAnd
            },{
                'type': ast.FloorDiv,
                'function': self.operator.convert_FloorDiv
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
        # result = None
        print(nodes)
        ifTrueThen = lambda theClass, theFunction: theFunction() if isinstance(nodes, theClass) else None
        self.mod.set_nodes(nodes)
        self.stmt.set_nodes(nodes)
        self.expr.set_nodes(nodes)
        self.standard.set_nodes(nodes)
        self.arguments.set_nodes(nodes)
        self.arg.set_nodes(nodes)
        aList = []

        for aSymbol in self.synbols:
            response = ifTrueThen(aSymbol.get('type'), aSymbol.get('function'))
            aList.append(response)
        aList = list(filter(lambda x: x is not None, aList))
        # for anItem in aList:
        #     if anItem is not None:
        #         return anItem
        return aList
    
    def run(self):
        result = self.parse(self.abstract_tree)
        from pprint import pprint
        print('=== result ===')
        pprint(result)
        return