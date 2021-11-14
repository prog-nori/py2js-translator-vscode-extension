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
        # print(self.a_symbol_table)
        print('initialize defined_vars', self.defined_vars_table)
        locals = 'locals'
        def search(
            theTarget,
            aCollection,
            aList = self.current_scope_list,
            aTable = self.defined_vars_table):
            
            isDefined = False
            print('\n==========\n')
            print('Table:', self.defined_vars_table)
            print('Target:', theTarget)
            print('Collection:', aCollection)
            # print('Defined:', definedVars)
            print('Scope:', aList)
            print('\n---\n')
            if isinstance(aCollection, dict):
                # print('aList0 =', aList[0], aList[0] in aCollection.keys())
                head = aList[0]
                if head in aCollection.keys():
                    if not head in aTable:
                        aTable[head] = {}
                    print(47, aTable[head])
                    print(48, aTable)
                    print('[locals in aCollection]', locals in aCollection.keys(), aCollection)
                    print(aCollection.keys())
                    print(51, list(aCollection[head].keys()), aCollection)
                    if locals in list(aCollection[head].keys()):
                        # defined_vars = self.defined_vars_table[head][locals]
                        # print('definedVars:', defined_vars)
                        # self.defined_vars_table[head][locals] = set()
                        # definedVars = self.defined_vars_table[head][locals]
                        # definedVars = definedVars | set(aCollection[head][locals])
                        # print('[JUDGE]', theTarget, theTarget in defined_vars, defined_vars)
                        # isDefined = theTarget in aTable[head][locals]
                        # print(99, theTarget, theTarget in aTable[head]['locals'], aTable[head])
                        if 'locals' in aTable[head]:
                            if theTarget in aTable[head]['locals']:
                                isDefined = True
                                pass
                        print(60, head, aTable[head], aTable)
                        print(59, locals in aTable[head], aTable[head]) # locals in aTable[head]がFlaseになる場合を探し、isDefinedを適宜書き換える。
                        aTable[head] = is_not_find_then_create(aTable[head], locals, theTarget)
                        print(56, aTable)
                        print(57, aTable[head], isDefined)
                        # if theTarget in defined_vars:
                        #     isDefined = True
                    elif len(aList) > 1:
                        print('ないから再帰')
                        print(62, aTable[head])
                        print(63, head, aTable)
                        anotherTable, isDefined = search(theTarget, aCollection[head], aList[1:], aTable[head])
                        print(anotherTable)
                        print('#####', isDefined)
            print('RESULT:', isDefined)
            return aTable, isDefined
        
        def is_not_find_then_create(aCollection, aKey, aValue):
            print('k({}) in o({}) >>'.format(aKey, list(aCollection.keys())), aKey in aCollection.keys())
            # theStatus = False
            if not aKey in aCollection.keys():
                aCollection[aKey] = set()
            # else:
            #     theStatus = True
            # print(':::', aValue)
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