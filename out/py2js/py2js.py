# #! /usr/bin/env python3
# #! -*- coding: utf-8 -*-

from src.lib.parser import Parser
from src.lib.SymTableCollection import SymTableCollection

class Py2JS(Parser):
    def __init__(self, an_abstract_tree, a_symbol_table):
        theSymtableCollection = SymTableCollection()
        the_dict = theSymtableCollection.get_dict(a_symbol_table)
        # print('theDict')
        # print(the_dict)
        super().__init__(the_dict)
        self.ast_ = an_abstract_tree
        return
    
    def print(self):
        from pprint import pprint
        pprint(self.ast_)
    
    def run(self):
        # self.set_nodes(self.ast_)
        result = self.parse(self.ast_)
        # print('/** 【変数一覧】\n')
        # print(self.predefinedVariables)
        # print('\n*/\n')
        return result

import ast

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
        py2js = Py2JS(parsed_pycode)
        result = py2js.run()
        print(result)

if __name__ == '__main__':
    import sys
    example = Example()
    example.main(sys.argv[1:])