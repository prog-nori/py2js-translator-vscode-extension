#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from src.modules.nodeParser import NodeParser

class Arg(NodeParser):
    def convert_Arg(self, nodes):
        # return nodes.arg, nodes.arg
        return nodes.arg