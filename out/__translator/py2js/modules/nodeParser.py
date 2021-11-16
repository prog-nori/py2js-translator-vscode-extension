#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

from operator import itemgetter
import ast
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
        anIterator = itemgetter(*items)(self.nodes.__dict__)
        # print('iter:', type(anIterator), anIterator)
        if anIterator is not None:
            if isinstance(anIterator, list) or isinstance(anIterator, tuple):
                for item in anIterator:
                    if isinstance(item, list) and isList:
                        # print(1, item)
                        anotherList = []
                        for grand_child in item:
                            anotherList.append(self.recursional_function(grand_child))
                        aList.append(anotherList)
                    else:
                        # print(2, item)
                        res = self.recursional_function(item)
                        aList.append(res)
            else:
                # print(3, anIterator)
                res = self.recursional_function(anIterator)
                aList.append(res)
        # else:
        #     print(4, anIterator)
        return aList