#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

class ParseNodes(object):

    def __init__(self, the_function):
        self.recursional_function = the_function
        self.nodes = None
        return

    def set_nodes(self, nodes):
        self.nodes = nodes