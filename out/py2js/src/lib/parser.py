#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from src.data.symbol import Symbol

class Parser(object):
    """
    解析器のスーパークラス
    """
    def __init__(self):
        """
        初期化作業
        """
        self.type_string = lambda aVariable: type(aVariable).__name__
        self.nodes = None

        self.symbol_ = Symbol(self.parse)
        return
    
    def get_nodes(self):
        """
        nodesを取得する
        """
        return self.nodes
    
    def parse(self, nodes):
        """
        astの解析を行う
        """
        type_name = self.type_string(nodes)
        type_ = type(nodes)
        func = self.symbol_.get(type_)
        print('[type]', type_name)
        if func is None:
            return
        res = func(nodes)
        return res
    
    def set_nodes(self, nodes):
        """
        nodesに値をセットする
        """
        self.nodes = nodes