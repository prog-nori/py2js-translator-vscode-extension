#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from src.data.symbol import Symbol

class Py2JS:
    def __init__(self, an_abstract_tree):
        self.ast_ = an_abstract_tree
        self.type_string = lambda aVariable: type(aVariable).__name__
        self.symbol = Symbol()
        return
    
    def parse(self, nodes):
        type_name = self.type_string(nodes)
        type_ = type(nodes)
        func = self.symbol.get(type_)
        print('[type]', type_name)
        # print(func)
        if func is None:
            return
        res = func(nodes, self.parse)
        print(type_name)
        # print(res)
        return res
    
    def print(self):
        from pprint import pprint
        pprint(self.ast_)
    
    def run(self):
        self.parse(self.ast_)
        return