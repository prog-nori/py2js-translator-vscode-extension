#! /usr/bin/env python3
#! -*- coding: utf-8 -*-
 
import ast
from src.modules.standard import Standard
from src.modules.mod import Mod
from src.modules.stmt import Stmt

class Symbol:
    def __init__(self):
        mod = Mod()
        standard = Standard()
        stmt = Stmt()
        self.symbol_ = {
            # 標準の型
            list: standard.convert_List,
            dict: standard.convert_Dict,
            str: standard.convert_Str,
            None: standard.convert_None,
            # mod系
            ast.Module: mod.convert_Module,
            ast.Interactive: mod.convert_Interactive,
            ast.Expression: mod.convert_Expression,
            ast.FunctionType: mod.convert_FunctionType,
            # stmt系
            ast.FunctionDef: stmt.convert_FunctionDef,
            ast.AsyncFunctionDef: stmt.convert_FunctionDef
            # expr系
            # expr_context系
            # boolop系
            # operator系
            # unaryop系
            # cmpop系
            # comprehension系
            # excepthandler系
            # arguments系
            # arg系
            # keyword系
            # alias系
            # withitem系
            # type_ignore系
        }
    
    def get(self, aKey):
        print(aKey.__name__)
        # print('>', self.symbol_.get(aKey))
        return self.symbol_.get(aKey)