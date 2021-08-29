#! /usr/bin/env python3
#! -*- coding: utf-8 -*-
import ast
from py2js import Py2JS

class Arg:
    def convert_Arg(self: Arg, nodes: ast.arg, parse: Py2JS.parse) -> str: ...