#! /usr/bin/bash
#! -*- coding: utf-8 -*-

"""
定義済みの変数のログを残す
def func():
    hoge = Hoge()
    hoge.huga.hamachi = ...
ならfunc.hoge.huga.hamachiとして記録
"""
class PredefinedVariables(object):
    def __init__(self):
        self.list_ = list()
        return
    
    # def add(self, path):
    #     """
    #     パスを追加する
    #     """
    #     self.list_.append(path)
    #     return
    
    # def remove(self, path):
    #     """
    #     削除する
    #     """
    #     self.list_.remove(path)
    
    # def is_exists(self, path):
    #     """
    #     リストに存在するか(定義済みの変数であるか)判定
    #     """
    #     return path in self.list_
