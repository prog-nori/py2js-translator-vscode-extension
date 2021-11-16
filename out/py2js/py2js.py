# #! /usr/bin/env python3
# #! -*- coding: utf-8 -*-

from src.lib.parser import Parser
from src.lib.SymTableCollection import SymTableCollection

class Py2JS(Parser):
    def __init__(self, an_abstract_tree, a_symbol_table):
        theSymtableCollection = SymTableCollection()
        the_dict = theSymtableCollection.get_dict(a_symbol_table)
        super().__init__(the_dict)
        self.ast_ = an_abstract_tree
        return
    
    def print(self):
        from pprint import pprint
        pprint(self.ast_)
    
    def run(self):
        result = self.parse(self.ast_)
        return result

import ast

class OutOfRangeValueError(Exception):
    """the value is out of range."""
    pass

class UnexpectedValueError(Exception):
    """the value is unexpected."""
    pass

from symtable import symtable

class Example():
    def __init__(self):
        return

    def get_text_from_the_file(filename):
        with open(filename) as fp:
            return fp.read()

    def main(self, args):
        # サンプルコード(python)の取得
        pycode = args[0]
        # サンプルコードのast(dict)の取得
        parsed_pycode = ast.parse(pycode)
        compile_type = 'exec'
        aSymbolTable = symtable(pycode, '', compile_type)
        py2js = Py2JS(parsed_pycode, aSymbolTable)
        result = py2js.run()
        print(result)

if __name__ == '__main__':
    import sys
    example = Example()
    example.main(sys.argv[1:])