#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

class Stmt:
    def convert_FunctionDef(self, nodes, parse):
        name = parse(nodes.name)
        args = parse(nodes.args)
        body = '\n'.join(parse(nodes.body))
        frame = 'function {}({}){{\n{}}}\n'
        return frame.format(name, args, body)

    def convert_AsyncFunctionDef(self, nodes, parse):
        return f'async {self.convert_FunctionDef(nodes, parse)}'

    def convert_ClassDef(self, nodes, parse):
        name = parse(nodes.name)
        bases_ = parse(nodes.bases)
        bases = bases_[0] if len(bases_) > 0 else ''
        body = '\n'.join(parse(nodes.body))
        result = ''
        if len(bases) > 0:
            result = 'class {} extends {} {{\n{}}}\n'.format(name, bases, body)
        else:
            result = 'class {} {{\n{}}}\n'.format(name, body)
        return result

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
        