#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

import ast
# from pprint import pprint
# from get_abstract_tree.parser import parse_nodes
from py2js.translator import Translator

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
        # pycode = args[0] # 本番はこれを使う
        # サンプルコードのast(dict)の取得
        with open(args[0]) as fp:
            pycode = ''.join(fp.readlines())
            abstract_tree = ast.parse(pycode)
            translator = Translator(abstract_tree)
            translator.run()
    
def add(a, b):
    return a + b

if __name__ == '__main__':
    import sys
    example = Example()
    example.main(sys.argv[1:])
    print(add(1, 2))