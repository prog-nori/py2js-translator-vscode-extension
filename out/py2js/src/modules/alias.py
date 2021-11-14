#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from src.modules.nodeParser import NodeParser

class Alias(NodeParser):
    def convert_Alias(self, nodes):
        # return nodes.arg, nodes.arg
        return nodes.name