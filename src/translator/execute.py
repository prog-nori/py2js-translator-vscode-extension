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
        # pycode = self.get_pycode(5)
        # print('arguments')
        # print(args)
        # with open(args[0]) as fp:
        #     pycode = ''.join(fp.readlines())
        #     # サンプルコードのast(dict)の取得
        #     parsed_pycode = ast.parse(pycode)
        #     parsed_ast = parse_nodes(parsed_pycode)
        #     translator = Translator(parsed_ast)
        #     # translator.print()
        #     translator.run()
        return [len(args), type(args)]

if __name__ == '__main__':
    import sys
    example = Example()
    example.main(sys.argv[1:])