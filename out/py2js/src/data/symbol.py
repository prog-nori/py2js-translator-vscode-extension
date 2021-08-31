# #! /usr/bin/env python3
# #! -*- coding: utf-8 -*-
 
import ast

from src.modules.standard import Standard
from src.modules.mod import Mod
from src.modules.stmt import Stmt
from src.modules.arguments import Arguments
from src.modules.arg import Arg

class Symbol(object):

    def __init__(self, parser):
        mod = Mod(parser)
        standard = Standard(parser)
        stmt = Stmt(parser)
        arguments = Arguments(parser)
        arg = Arg(parser)

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
            ast.AsyncFunctionDef: stmt.convert_FunctionDef,
            ast.ClassDef: stmt.convert_ClassDef,
            # expr系
            # expr_context系
            # boolop系
            # operator系
            # unaryop系
            # cmpop系
            # comprehension系
            # excepthandler系
            # arguments系
            ast.arguments: arguments.convert_Arguments,
            # arg系
            ast.arg: arg.convert_Arg,
            # keyword系
            # alias系
            # withitem系
            # type_ignore系
        }

    def get(self, aKey):
        if aKey.__name__ == 'NoneType':
            dummy = lambda _: ''
            return dummy
        else:
            return self.symbol_.get(aKey)