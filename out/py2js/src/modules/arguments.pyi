#! /usr/bin/env python3
#! -*- coding: utf-8 -*-
import ast
from py2js import Py2JS

class Arguments:
    def convert_Arguments(self: Arguments, nodes: ast.arguments, parse: Py2JS.parse) -> str: ...