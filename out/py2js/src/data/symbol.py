# #! /usr/bin/env python3
# #! -*- coding: utf-8 -*-
 
import ast

from src.modules.standard import Standard
from src.modules.mod import Mod
from src.modules.stmt import Stmt
from src.modules.expr import Expr
from src.modules.arguments import Arguments
from src.modules.arg import Arg
from src.modules.operator import Operator
from src.modules.comprehension import Comprehension
from src.modules.cmpop import Cmpop
from src.modules.excepthandler import ExceptHandler
from src.modules.alias import Alias

class Symbol(object):

    def __init__(self, parser, options, indent, predefinedVariables,
    current_scope_list, a_symbol_table, defined_vars_table):

        args = (parser, options, indent, predefinedVariables, current_scope_list, a_symbol_table, defined_vars_table)
        standard = Standard(*args)
        mod = Mod(*args)
        stmt = Stmt(*args)
        expr = Expr(*args)
        operator = Operator(*args)
        arguments = Arguments(*args)
        arg = Arg(*args)
        comprehension = Comprehension(*args)
        cmpop = Cmpop(*args)
        exceptionHandler = ExceptHandler(*args)
        alias = Alias(*args)

        self.indent = indent
        self.predefinedVariables = predefinedVariables
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
            ast.Return: stmt.convert_Return,
            ast.Delete: stmt.convert_Delete,
            ast.Assign: stmt.convert_Assign,
            ast.AugAssign: stmt.convert_AugAssign,
            ast.AnnAssign: stmt.convert_AnnAssign,
            ast.For: stmt.convert_For,
            ast.AsyncFor: stmt.convert_AsyncFor,
            ast.While: stmt.convert_While,
            ast.If: stmt.convert_If,
            ast.With: stmt.convert_With,
            ast.AsyncWith: stmt.convert_AsyncWith,
            ast.Raise: stmt.convert_Raise,
            ast.Try: stmt.convert_Try,
            ast.Assert: stmt.convert_Assert,
            ast.Import: stmt.convert_Import,
            ast.ImportFrom: stmt.convert_ImportFrom,
            ast.Global: stmt.convert_Global,
            ast.Nonlocal: stmt.convert_Nonlocal,
            ast.Expr: stmt.convert_Expr,
            ast.Pass: stmt.convert_Pass,
            ast.Break: stmt.convert_Break,
            ast.Continue: stmt.convert_Continue,
            # expr系
            ast.BoolOp: expr.convert_BoolOp,
            ast.NamedExpr: expr.convert_NamedExpr,
            ast.BinOp: expr.convert_BinOp,
            ast.UnaryOp: expr.convert_UnaryOp,
            ast.Lambda: expr.convert_Lambda,
            ast.IfExp: expr.convert_IfExp,
            ast.Dict: expr.convert_Dict,
            ast.Set: expr.convert_Set,
            ast.ListComp: expr.convert_ListComp,
            ast.SetComp: expr.convert_SetComp,
            ast.DictComp: expr.convert_DictComp,
            ast.GeneratorExp: expr.convert_GeneratorExp,
            ast.Await: expr.convert_Await,
            ast.Yield: expr.convert_Yield,
            ast.YieldFrom: expr.convert_YieldFrom,
            ast.Compare: expr.convert_Compare,
            ast.Call: expr.convert_Call,
            ast.FormattedValue: expr.convert_FormattedValue,
            ast.JoinedStr: expr.convert_JoinedStr,
            ast.Constant: expr.convert_Constant,
            ast.Attribute: expr.convert_Attribute,
            ast.Subscript: expr.convert_Subscript,
            ast.Starred: expr.convert_Starred,
            ast.Name: expr.convert_Name,
            ast.List: expr.convert_List,
            ast.Tuple: expr.convert_Tuple,
            ast.Slice: expr.convert_Slice,
            # expr_context系
            # boolop系
            # operator系
            ast.Add: operator.convert_Add,
            ast.Sub: operator.convert_Sub,
            ast.Mult: operator.convert_Mult,
            ast.MatMult: operator.convert_MatMult,
            ast.Div: operator.convert_Div,
            ast.Mod: operator.convert_Mod,
            ast.Pow: operator.convert_Pow,
            ast.LShift: operator.convert_LShift,
            ast.RShift: operator.convert_RShift,
            ast.BitOr: operator.convert_BitOr,
            ast.BitXor: operator.convert_BitXor,
            ast.BitAnd: operator.convert_BitAnd,
            ast.FloorDiv: operator.convert_FloorDiv,
            # unaryop系
            # cmpop系
            ast.Eq: cmpop.convert_Eq,
            ast.NotEq: cmpop.convert_NotEq,
            ast.Lt: cmpop.convert_Lt,
            ast.LtE: cmpop.convert_LtE,
            ast.Gt: cmpop.convert_Gt,
            ast.GtE: cmpop.convert_GtE,
            ast.Is: cmpop.convert_Is,
            ast.IsNot: cmpop.convert_IsNot,
            ast.In: cmpop.convert_In,
            ast.NotIn: cmpop.convert_NotIn,
            # comprehension系
            ast.comprehension: comprehension.convert_comprehension,
            # excepthandler系
            ast.ExceptHandler: exceptionHandler.convert_ExceptHandler,
            # arguments系
            ast.arguments: arguments.convert_Arguments,
            # arg系
            ast.arg: arg.convert_Arg,
            # keyword系
            # alias系
            ast.alias: alias.convert_Alias,
            # withitem系
            # type_ignore系
        }

    def get(self, aKey):
        if aKey.__name__ == 'NoneType':
            dummy = lambda _: ''
            return dummy
        else:
            return self.symbol_.get(aKey)