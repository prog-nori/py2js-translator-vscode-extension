#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from py2js import Py2JS
import ast
from symtable import symtable

def get_text_from_the_file(filename):
    with open(filename) as fp:
        return fp.read()

def main():
    filename = './pycode.py'
    with open(filename) as fp:
        compile_type = 'exec'
        aSymbolTable = symtable(get_text_from_the_file(filename), filename, compile_type)
        lines = fp.readlines()
        tree = ast.parse(''.join(lines))
        translator = Py2JS(tree, aSymbolTable)
        # translator.print()
        result = translator.run()
        print('// == result ==')
        print('/**')
        print(translator.current_scope_list)
        print('*/')
        print(result)
    return

if __name__ == '__main__':
    main()