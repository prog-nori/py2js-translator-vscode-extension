#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from py2js.util.jscode import JsCode
from py2js.modules.nodeParser import NodeParser
import re

class Expr(NodeParser):

    def __init__(self, the_function):
        self.recursional_function = the_function
        return

    def convert_BoolOp(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_NamedExpr(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_BinOp(self, v, opt={}):
        jscode: JsCode = JsCode()
        # left = self.func(v.get('left'))
        # k = v.get('op')
        # _op = k if k not in [{}, None] else {'Add': '+'}
        # op = self.func(_op)
        # right = self.func(v.get('right'))
        # jscode.add(f'{left} {op} {right}')
        return jscode

    def convert_UnaryOp(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Lambda(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_IfExp(self, v, opt={}):
        # 三項演算子
        jscode: JsCode = JsCode()
        _test = v.get('test')
        _body = v.get('body')
        _orelse = v.get('orelse', [])
        orelse = None
        if not (_test is None or _body is None):
            test = self.func(_test)
            body = self.func(_body)
            orelse = self.func(_orelse)
            jscode.add(f'{test}? {body}: {orelse}')
        return jscode

    def convert_Dict(self, v, opt={}):
        jscode: JsCode = JsCode()
        keys = [aGrandChild['Constant']['value'] for aGrandChild in v['keys']]
        values = [aGrandChild['Constant']['value'] for aGrandChild in v['values']]
        res = {}
        if len(keys) == len(values):
            for i, item in enumerate(keys):
                res[item] = values[i]
        jscode.add(','.join([
            re.sub(
                r'\'([\W|\w]+)\':',
                r'\1:',
                str(item)
            ) for item in str(res).split(',')
        ]))
        return jscode

    def convert_Set(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_ListComp(self, v, opt={}):
        jscode: JsCode = JsCode()
        generators = self.func(v.get('generators'), opt={
            'elt': v.get('elt')
        })
        jscode.add(generators)
        return jscode

    def convert_SetComp(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_DictComp(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_GeneratorExp(self, v, opt={}):
        jscode: JsCode = JsCode()
        elt = self.func(v.get('elt'))
        op = {
            'elt': {
                'Return': v.get('elt')
            }
        }
        generators = self.func(v.get('generators'), opt=op)
        return jscode

    def convert_Await(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Yield(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_YieldFrom(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Compare(self, v, opt={}):
        jscode: JsCode = JsCode()
        left = self.func(v.get('left'))
        ops = self.func(v.get('ops'))
        comparators = self.func(v.get('comparators'))
        jscode.add(f'{left} {ops} {comparators}')
        return jscode

    def convert_Call(self):
        # 関数呼び出し
        jscode: JsCode = JsCode()
        args = self.recursional_function('args')
        func = self.recursional_function('func')
        print('Call====')
        print(args, func)
        # _args = v.get('args')
        # _func = v.get('func')
        # args = ''
        # func = ''
        # if _args is not None:
        #     aList = []
        #     for item in _args:
        #         res = self.func(item)
        #         aList.append(res)
        #     args = aList
        # if _func is not None:
        #     name = self.func(_func)
        #     func = 'console.log' if name == 'print' else name
        # if not(args == '' or func == ''):
        #     arguments = ', '.join([arg.replace('\n', '') for arg in args]) if len(args) > 0 else ''
        #     jscode.add(f'{func}({arguments})')
        return jscode

    def convert_FormattedValue(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_JoinedStr(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Constant(self, v, opt={}):
        jscode: JsCode = JsCode()
        if 'value' in v:
            value = v.get('value')
            if isinstance(value, list):
                aString = ' '.join(value)
                anotherString = f'\'{aString}\''
                jscode.add(anotherString)
            elif isinstance(value, dict) and value == {}:
                jscode.add('null')
            elif isinstance(value, str):
                if value == 'None':
                    value = 'null'
                jscode.add(f'\'{value}\'')
            else:
                jscode.add(value)
        return jscode

    def convert_Attribute(self, v, opt={}):
        jscode: JsCode = JsCode()
        _parent = str(self.convert_Name(deep_get(v, ['value', 'Name'], {})))
        parent = 'this' if _parent == 'self' else _parent
        parent = '\'\'' if parent == '' else parent
        method = deep_get(v, ['attr'], {})
        jscode.add('.'.join([parent, method]))
        return jscode

    def convert_Subscript(self, v, opt={}):
        jscode: JsCode = JsCode()
        _slice = v.get('slice')
        _value = v.get('value')
        if _slice is not None and _value is not None:
            aSlice = self.func(_slice)
            aValue = self.func(_value)
            jscode.add(f'{aValue}[{aSlice}]')
        return jscode

    def convert_Starred(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Name(self):
        id = self.parseNodes('id')
        jscode: JsCode = JsCode()
        jscode.add(id)
        # print('name object is:', id)
        return jscode

    def convert_List(self, v, opt={}):
        jscode: JsCode = JsCode()
        aList = []
        if 'elts' in v:
            aList = [str(self.func(item, 'Constant')) for item in v['elts']]
        jscode.add('[')
        jscode.add(', '.join(aList))
        jscode.add(']')
        return jscode

    def convert_Tuple(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Slice(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_attributes(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode