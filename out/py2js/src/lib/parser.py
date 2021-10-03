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
        self.options = Options()
        self.indent = Indent()
        self.paths = PathList()
        self.predefinedVariables = {}

        self.symbol_ = Symbol(self.parse, self.options, self.indent, self.predefinedVariables)
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
        if func is None:
            return
        res = func(nodes)
        # if res == '' and nodes is not None:
        #     print('res is \'\':', type_name, nodes)
        return res
    
    def set_nodes(self, nodes):
        """
        nodesに値をセットする
        """
        self.nodes = nodes

class Options(object):
    def __init__(self):
        """
        オプションを準備する
        """
        self.options_ = {}
    
    def __str__(self):
        return str(self.options_)
    
    def add(self, key, value):
        """
        オプションを追加する
        """
        self.options_[key] = value
    
    def update(self, key, value):
        """
        オプションを更新する。事実上addと一緒
        """
        self.add(key, value)
    
    def remove(self, key):
        """
        オプションを除去する
        """
        del self.options_[key]
    
    def reset(self):
        """
        オプションを初期化する
        """
        self.options_ = {}
    
    def get(self, key):
        """
        オプションを取得する。なければNone
        """
        if key in self.options_:
            return self.options_[key]
        else:
            return None

class Indent:
    def __init__(self):
        self.indent_ = 0
    
    def increment(self):
        self.indent_ += 1
    
    def decrement(self):
        self.indent_ -= 1
    
    def get(self):
        aList = ['\t' for _ in range(self.indent_)]
        return ''.join(aList)
    
# class PathList(list):
#     def __init__(self):
#         super().__init__()
#         self.current = ''

#     def find(self, aString):
#         return aString in self
    
#     def rewrite(self, aPath):
#         self.current = aPath
    
#     def 

class PathList:
    def __init__(self):
        self.list_ = list()
        self.current_ = ''
    
    def put(self, aString):
        """
        カレントを初期化する
        """
        self.current_ = aString
    
    def append(self, aString):
        """
        新しいパスを結合する
        """
        self.current_ = '.'.join(self.current_, aString)
    
    def cd_prev(self):
        """
        1つ上の階層に戻る
        """
        self.current_ = '.'.join(self.current_.split('.')[:-1])
