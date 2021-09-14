#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from src.util.convert_util import body_joiner

class NodeParser(object):
    def __init__(self, theParser, options, indent, paths):
        self.parse = theParser
        self.options = options
        self.indent = indent
        self.paths = paths
        self.body_joiner = body_joiner