#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

from operator import itemgetter

class NodeParser(object):
    """
    各ノードを解析するスーパークラス
    """

    def __init__(self, the_function):
        """
        コンストラクタ。再帰関数やノードの初期値をセットする
        """
        self.recursional_function = the_function
        self.nodes = None
        return

    def set_nodes(self, nodes):
        """
        ノードをインスタンス変数としてセットする
        """
        self.nodes = nodes
    
    def parseNodes(self, *items, isList=False):
        """
        ノードから複数のリーフ(または子ノード)を取得し、
        再帰的に処理したものをリストとして返す
        """
        aList = []
        # print(self.nodes.__dict__, self.nodes.__dict__.keys())
        # print(items[0], self.nodes.__dict__.get(items[0]))
        # for x in items:
        #     print(f'{x}|', x in self.nodes.__dict__)
        # print(items[0] in self.nodes.__dict__)
        # print(itemgetter(*items)(self.nodes.__dict__))
        anIterator = itemgetter(*items)(self.nodes.__dict__)
        # print(type(anIterator))
        if isinstance(anIterator, tuple):
            for item in anIterator:
                if isinstance(item, list) and isList:
                    anotherList = []
                    for grand_child in item:
                        anotherList.append(str(self.recursional_function(grand_child)))
                    # aList.append(', '.join(anotherList))
                    aList.append(anotherList)
                else:
                    res = self.recursional_function(item)
                    aList.append(str(res))
            # values = ''.join(aList)
        # values = [self.recursional_function(item) for item in itemgetter(*items)(self.nodes.__dict__)]
        return aList