#! /usr/bin/env python3
#! -*- coding:utf-8 -*-
from operator import itemgetter

class NodeParser(object):

    def __init__(self, the_function):
        self.recursional_function = the_function
        self.nodes = None
        return

    def set_nodes(self, nodes):
        self.nodes = nodes
    
    def parseNodes(self, *items):
        values = itemgetter(*items)(self.nodes.__dict__)
        return values