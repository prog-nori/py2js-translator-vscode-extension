#! /usr/bin/env python3
#! -*- coding: utf-8 -*-
from src.modules.nodeParser import NodeParser
class ExceptHandler(NodeParser):
    def convert_ExceptHandler(self, nodes):
        exception = self.parse(nodes.type)
        name = self.parse(nodes.name)
        body = ''.join(self.parse(nodes.body))
        inner_state = f'success = false\n{body}' if self.options.get('else') is True else body
        # handler = f'{exception} {name}' if name else exception
        state = f"""}} catch({name}) {{
    {inner_state}
}}"""
        return state