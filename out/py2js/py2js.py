#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from src.lib.parser import Parser

class Py2JS(Parser):
    def __init__(self, an_abstract_tree):
        super().__init__()
        self.ast_ = an_abstract_tree
        return
    
    def print(self):
        from pprint import pprint
        pprint(self.ast_)
    
    def run(self):
        # self.set_nodes(self.ast_)
        result = self.parse(self.ast_)
        return result