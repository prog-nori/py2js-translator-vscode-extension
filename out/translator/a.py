# #! /usr/bin/env python3
# #! -*- coding: utf-8 -*-

# import ast
# from get_abstract_tree.parser import parse_nodes
# from ast2js.translate import Translator

# class OutOfRangeValueError(Exception):
#     """hogehoge"""
#     pass

# class UnexpectedValueError(Exception):
#     """hugahuga"""
#     pass

# class Example():
#     def __init__(self):
#         return
    
#     def main(self, args):
#         # print('hello world')
#         # print(args)
#         print(''.join(args))

# if __name__ == '__main__':
#     import sys
#     example = Example()
#     example.main(sys.argv[1:])

# print('hello world')
class Example:
    def __init__(self):
        return

    def main(self):
        print('hello japan')
        return
    
    def calc(self, a, b, mode):
        c = 0
        if mode == 'add':
            c = a + b
        elif mode == 'sub':
            c = a - b
        elif mode == 'mult':
            c = a * b
        elif mode == 'div':
            c = a // b
        return c

if __name__ == '__main__':
    example = Example()
    example.main()