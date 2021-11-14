#! /usr/bin/env python3
#! -*- coding: utf-8 -*-
# from ..lib.parser import Parser
# from src.lib.parser import Parser
from src.modules.nodeParser import NodeParser

# class Mod(Parser):
class Mod(NodeParser):
    def convert_Module(self, nodes):
        # body
        # parse(nodes.body)
        body = self.parse(nodes.body)
        self.predefinedVariables['Module'] = []
        return '\n'.join(body)

    def convert_Interactive(self, nodes):
        return ''

    def convert_Expression(self, nodes):
        return ''

    def convert_FunctionType(self, nodes):
        return ''