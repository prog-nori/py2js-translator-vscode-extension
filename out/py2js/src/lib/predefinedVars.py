#! /usr/bin/bash
#! -*- coding: utf-8 -*-

"""
定義済みの変数のログを残す
def func():
    hoge = Hoge()
    hoge.huga.hamachi = ...
ならfunc.hoge.huga.hamachiとして記録
"""
class PredefinedVars(object):
    def __init__(self):
        self.instances = list()
        self.vars = list() # リストとして変数一覧を記憶する
        self.dict_ = dict() # 辞書として変数一覧を記憶する
        return
    
    def add(self, var):
        if 'self.' in var:
            # インスタンス変数と判定
            if not var in self.instances:
                self.instances.append(var)
        else:
            # ローカル変数と判定
            if not var in self.vars:
                self.vars.append(var)
                # self.
    
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
