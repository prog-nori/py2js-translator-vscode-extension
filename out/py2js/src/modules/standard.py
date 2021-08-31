#! /usr/bin/env python3
#! -*- coding: utf-8 -*-
from src.modules.nodeParser import NodeParser

class Standard(NodeParser):
    def convert_List(self, nodes):
        result = []
        for item in nodes:
            parsed = self.parse(item)
            if parsed is not None:
                result.append(self.parse(item))
        return result

    def convert_Dict(self, nodes):
        result = []
        for item in nodes.values():
            result.append(self.parse(item))
        return result
    
    def convert_Str(self, nodes):
        return nodes
    
    def convert_None(self, nodes):
        print('<None type function!!>')
        return ''