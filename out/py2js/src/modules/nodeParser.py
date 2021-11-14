#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from src.util.convert_util import body_joiner

class NodeParser(object):
    def __init__(self, theParser, options, indent, predefinedVariables, current_scope_list, a_symbol_table, defined_vars_table):
        self.parse = theParser
        self.options = options
        self.indent = indent
        self.body_joiner = body_joiner
        self.predefinedVariables = predefinedVariables
        self.current_scope_list = current_scope_list
        self.a_symbol_table = a_symbol_table
        self.defined_vars_table = defined_vars_table
    
    def isDefinedVar(self, theName):
        """
        その変数が定義済みであるか調べる。
        theName...変数名
        self.a_symbol_table...定義済み変数リスト(辞書)
        self.current_scope_list...名前空間をリストしている。リストの末尾の方が深層にあたる。
        """
        locals = 'locals'
        def search(
            theTarget,
            aCollection,
            aList = self.current_scope_list,
            aTable = self.defined_vars_table):
            
            isDefined = False
            if isinstance(aCollection, dict):
                head = aList[0]
                if head in aCollection.keys():
                    if not head in aTable:
                        aTable[head] = {}
                    if locals in list(aCollection[head].keys()):
                        if 'locals' in aTable[head]:
                            if theTarget in aTable[head]['locals']:
                                isDefined = True
                                pass
                        aTable[head] = is_not_find_then_create(aTable[head], locals, theTarget)
                    elif len(aList) > 1:
                        anotherTable, isDefined = search(theTarget, aCollection[head], aList[1:], aTable[head])
            #             print(anotherTable)
            #             print('#####', isDefined)
            # print('RESULT:', isDefined)
            return aTable, isDefined
        
        def is_not_find_then_create(aCollection, aKey, aValue):
            if not aKey in aCollection.keys():
                aCollection[aKey] = set()
            aCollection[aKey].add(aValue)
            return aCollection
        result = []

        if '=' in theName:
            names = theName.replace(' ', '').split('=')
            for aName in names:
                result.append(search(theTarget = aName, aCollection = self.a_symbol_table))
        else:
            resultTable, result = search(theTarget = theName, aCollection = self.a_symbol_table)
            self.defined_vars_table = resultTable
        return result