#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

class Stmt:
    def convert_FunctionDef(self, nodes, parse):
        print('[FUNCTION]', nodes.__dict__)
        name = parse(nodes.name)
        args = parse(nodes.args)
        body = parse(nodes.body)
        print(f'function {name}({args})', '{', body, '}')
        return ''

    def convert_AsyncFunctionDef(self, nodes, parse):
        return ''

    def convert_ClassDef(self, nodes, parse):
        return ''

    def convert_Return(self, nodes, parse):
        return ''

    def convert_Delete(self, nodes, parse):
        return ''

    def convert_Assign(self, nodes, parse):
        return ''

    def convert_AugAssign(self, nodes, parse):
        return ''

    def convert_AnnAssign(self, nodes, parse):
        return ''

    def convert_For(self, nodes, parse):
        return ''

    def convert_AsyncFor(self, nodes, parse):
        return ''

    def convert_While(self, nodes, parse):
        return ''

    def convert_If(self, nodes, parse):
        return ''

    def convert_With(self, nodes, parse):
        return ''

    def convert_AsyncWith(self, nodes, parse):
        return ''

    def convert_Raise(self, nodes, parse):
        return ''

    def convert_Try(self, nodes, parse):
        return ''

    def convert_Assert(self, nodes, parse):
        return ''

    def convert_Import(self, nodes, parse):
        return ''

    def convert_ImportFrom(self, nodes, parse):
        return ''

    def convert_Global(self, nodes, parse):
        return ''

    def convert_Nonlocal(self, nodes, parse):
        return ''

    def convert_Expr(self, nodes, parse):
        return ''

    def convert_Pass(self, nodes, parse):
        return ''

    def convert_Break(self, nodes, parse):
        return ''

    def convert_Continue(self, nodes, parse):
        return ''
        