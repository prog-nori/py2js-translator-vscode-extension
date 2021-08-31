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
        return result
    def convert_Arguments(self, nodes):
        args = self.parse(nodes.args)
        defaults = self.parse(nodes.defaults)
        kw_defaults = self.parse(nodes.kw_defaults)
        kwarg = self.parse(nodes.kwarg)
        kwonlyargs = self.parse(nodes.kwonlyargs)
        vararg = self.parse(nodes.vararg)
        # print('[args]', args, defaults, kw_defaults, kwarg, kwonlyargs, vararg)
        # print('[args]', type(args), type(defaults), type(kw_defaults), type(kwarg), type(kwonlyargs), type(vararg))
        # print(''.join(self._get_flat_list([args, defaults, kw_defaults, kwarg, kwonlyargs, vararg])))
        aList = list(filter(lambda x: x not in [None, [], ''], [args, defaults, kw_defaults, kwarg, kwonlyargs, vararg]))

        # 仮の姿。まだやることはたくさんある
        # ・キーワード
        # ・可変長
        # ・初期値
        # ・self処理等
        return ', '.join(self._get_flat_list(aList))