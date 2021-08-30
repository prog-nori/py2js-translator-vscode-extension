#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from py2js import Py2JS
import ast

def main():
    with open('./pycode.py') as fp:
        tree = ast.parse(''.join(fp.readlines()))
        translator = Py2JS(tree)
        # translator.print()
        result = translator.run()
        print('== result ==')
        print(result)
    return

if __name__ == '__main__':
    main()