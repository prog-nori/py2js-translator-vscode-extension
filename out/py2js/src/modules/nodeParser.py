#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from src.util.convert_util import body_joiner

class NodeParser(object):
    def __init__(self, theParser, options, indent, predefinedVariables):
        self.parse = theParser
        self.options = options
        self.indent = indent
        self.body_joiner = body_joiner
        self.predefinedVariables = predefinedVariables