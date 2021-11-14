#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from symtable import SymbolTable, Function, Class, Symbol

class SymTableCollection:

    def printTable(self, aTable):
        """
        symbolTable関連データを再帰的に解析、出力していく。
        """
        if isinstance(aTable, Function):
            aFunctionDict = dict()
            aFunctionDict['locals'] = aTable.get_locals()
            return { aTable.get_name(): aFunctionDict }

        elif isinstance(aTable, Class):
            aClassTuple = dict()
            if aTable.has_children():
                for aChild in aTable.get_children():
                    res = self.printTable(aChild)
                    aClassTuple.update(res)
            return { aTable.get_name(): aClassTuple }

        elif isinstance(aTable, Symbol):
            aSymbolTuple = list()
            return { aTable.get_name(): aSymbolTuple }

        elif isinstance(aTable, SymbolTable):
            aSymbolTableTuple = dict() # node
            if aTable.has_children():
                children = aTable.get_children()
                for aChild in children:
                    res = self.printTable(aChild)
                    aSymbolTableTuple.update(res)
            return aSymbolTableTuple
        else:
            pass
        return

    def get_dict(self, datas):
        # result = dict()
        result = self.printTable(datas)
        # print('// Result:', result)
        # # print('^^^')
        # print()
        # print(res)
        # result.update(res)

        # if isinstance(datas[0], str):
        #     datas = datas[1:]
        #     if isinstance(datas, tuple) and len(datas) == 1:
        #         datas = datas[0]
        # for aData in datas:
        #     res = self.printTable(aData)
        #     result.update(res)
        return result