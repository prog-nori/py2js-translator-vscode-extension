#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

import ast
from pprint import pprint
from get_abstract_tree.parser import parse_nodes
from ast2js.translate import Translator

class OutOfRangeValueError(Exception):
    """the value is out of range."""
    pass

class UnexpectedValueError(Exception):
    """the value is unexpected."""
    pass

class Example():
    def __init__(self):
        return

    def main(self, args):
        # サンプルコード(python)の取得
        pycode = args[0]
        # サンプルコードのast(dict)の取得
        parsed_pycode = ast.parse(pycode)
        parsed_ast = parse_nodes(parsed_pycode)
        translator = Translator(parsed_ast)
        translator.run()

if __name__ == '__main__':
    import sys
    example = Example()
    example.main(sys.argv[1:])