#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

class Mod:
    def convert_Module(self, nodes, parse):
        # body
        body = parse(nodes.body)
        print(body)
        return 'hello module'

    def convert_Interactive(self, nodes, parse):
        return ''

    def convert_Expression(self, nodes, parse):
        return ''

    def convert_FunctionType(self, nodes, parse):
        return ''