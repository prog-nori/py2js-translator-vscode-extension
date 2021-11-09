#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from src.util.convert_util import body_joiner

class NodeParser(object):
    def __init__(self, theParser, options, indent, predefinedVariables, current_scope_list, a_symbol_table):
        self.parse = theParser
        self.options = options
        self.indent = indent
        self.body_joiner = body_joiner
        self.predefinedVariables = predefinedVariables
        self.current_scope_list = current_scope_list
        self.a_symbol_table = a_symbol_table
    
    def isDefinedVar(self, theName):
        """
        その変数が定義済みであるか調べる。
        theName...変数名
        self.a_symbol_table...定義済み変数リスト(辞書)
        self.current_scope_list...名前空間をリストしている。リストの末尾の方が深層にあたる。
        """
        # print(self.a_symbol_table)
        def search(aCollection):
            isDefined = False
            if isinstance(aCollection, dict):
                for aNamespace in self.current_scope_list:
                    print(aNamespace, aCollection)
                    if 'local' in aCollection[aNamespace]:
                        if theName in aCollection[aNamespace]['local']:
                            isDefined = True
                        # 再帰処理を書く
                    nest_result = search(aCollection[aNamespace])
                    if nest_result == True:
                        isDefined = True
            return isDefined

        return search(self.a_symbol_table)
        # return self.a_symbol_table, theName