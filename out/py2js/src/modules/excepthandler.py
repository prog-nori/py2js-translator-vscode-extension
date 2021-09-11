#! /usr/bin/env python3
#! -*- coding: utf-8 -*-
from src.modules.nodeParser import NodeParser
class ExceptHandler(NodeParser):
    def convert_ExceptHandler(self, nodes):
        exception = self.parse(nodes.type)
        name = self.parse(nodes.name)
        self.indent.increment()
        body = self.body_joiner(self.parse(nodes.body), self.indent)
        inner_state = f'{self.indent.get()}success = false\n{body}' if self.options.get('else') is True else body
        self.indent.decrement()
        anIndent = self.indent.get()
        state = f'{anIndent}}}'
        state += f' catch({name}) {{\n{inner_state}'
        return state