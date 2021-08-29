#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

class Standard:
    def convert_List(self, nodes, parse):
        result = []
        for item in nodes:
            result.append(parse(item))
        return result

    def convert_Dict(self, nodes, parse):
        result = []
        for item in nodes.values():
            result.append(parse(item))
        return result
    
    def convert_Str(self, nodes, _):
        return nodes
    
    def convert_None(self, nodes, _):
        print('<None type function!!>')
        return ''