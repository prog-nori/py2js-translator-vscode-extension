#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from src.modules.nodeParser import NodeParser


class Comprehension(NodeParser):

    def convert_comprehension(self, nodes):
        # target = self.parse(nodes.target)
        # iter = self.parse(nodes.iter)
        # ifs = self.parse(nodes.ifs).reverse()
        # is_async = self.parse(nodes.is_async)
        # if_statements = ''
        # for anIndex, aCondition in enumerate(ifs):
        #     indents = ''.join(['\t' for _ in range(anIndex)])
        #     if_statements += f'{indents}if({aCondition}) {{\n'
        # state = f'{if_statements}{iter}.map({target} => )'
        # return state
        return ''