#! /usr/bin/env python3
#! -*- coding: utf-8 -*-
from src.modules.nodeParser import NodeParser

class Stmt(NodeParser):
    def convert_FunctionDef(self, nodes):
        name = self.parse(nodes.name)
        args = self.parse(nodes.args)
        body = '\n'.join(self.parse(nodes.body))
        frame = 'function {}({}){{\n{}}}\n'
        return frame.format(name, args, body)

    def convert_AsyncFunctionDef(self, nodes):
        return f'async {self.convert_FunctionDef(nodes, self.parse)}'

    def convert_ClassDef(self, nodes):
        name = self.parse(nodes.name)
        bases_ = self.parse(nodes.bases)
        bases = bases_[0] if len(bases_) > 0 else ''
        body = '\n'.join(self.parse(nodes.body))
        result = ''
        if len(bases) > 0:
            result = 'class {} extends {} {{\n{}}}\n'.format(name, bases, body)
        else:
            result = 'class {} {{\n{}}}\n'.format(name, body)
        return result

    def convert_Return(self, nodes):
        value = self.parse(nodes.value)
        result = ''
        if value:
            result = f'return {value}\n'
        else:
            result = 'return\n'
        return result

    def convert_Delete(self, nodes):
        return ''

    def convert_Assign(self, nodes):
        targets = self.parse(nodes.targets)
        theTarget = ' = '.join(targets)
        value = self.parse(nodes.value)
        # print(targets, value, ':', ' = '.join(targets), '=', value)
        return ' = '.join([theTarget, value])

    def convert_AugAssign(self, nodes):
        return ''

    def convert_AnnAssign(self, nodes):
        return ''

    def convert_For(self, nodes):
        return ''

    def convert_AsyncFor(self, nodes):
        return ''

    def convert_While(self, nodes):
        return ''

    def convert_If(self, nodes):
        return ''

    def convert_With(self, nodes):
        return ''

    def convert_AsyncWith(self, nodes):
        return ''

    def convert_Raise(self, nodes):
        return ''

    def convert_Try(self, nodes):
        return ''

    def convert_Assert(self, nodes):
        return ''

    def convert_Import(self, nodes):
        return ''

    def convert_ImportFrom(self, nodes):
        return ''

    def convert_Global(self, nodes):
        return ''

    def convert_Nonlocal(self, nodes):
        return ''

    def convert_Expr(self, nodes):
        return ''

    def convert_Pass(self, nodes):
        return ''

    def convert_Break(self, nodes):
        return ''

    def convert_Continue(self, nodes):
        return ''
        