#! /usr/bin/env python3
#! -*- coding: utf-8 -*-
from src.modules.nodeParser import NodeParser

class Arguments(NodeParser):
    def _get_flat_list(self, aList):
        """
        多重リストを平坦化する
        """
        result = []
        if isinstance(aList, list):
            for item in aList:
                if isinstance(item, list):
                    result.extend(self._get_flat_list(item))
                else:
                    result.append(item)
        else:
            result = aList
        if result != []:
            result = [arg for arg in list(filter(lambda x: x != '\'\'', result))]
        return result

    def convert_Arguments(self, nodes):
        args = list(filter(lambda aString: aString != 'self', self.parse(nodes.args)))
        defaults = self.parse(nodes.defaults)
        # kw_defaults = self.parse(nodes.kw_defaults)
        kwarg = self.parse(nodes.kwarg)
        kwonlyargs = self.parse(nodes.kwonlyargs)
        vararg = self.parse(nodes.vararg)

        aList = []
        defaults.reverse()
        for idx, elem in enumerate(defaults):
            own = args[len(args) - (idx + 1)]
            args[len(args) - (idx + 1)] = '{}={}'.format(own, elem)
        aList.extend(args)
        aList = list(filter(lambda x: x not in [None, [], ''], [*args, kwarg, kwonlyargs, vararg]))
        return ', '.join(self._get_flat_list(aList))