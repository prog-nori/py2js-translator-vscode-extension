#! /usr/bin/env python3
#! -*- coding:utf-8 -*-
from py2js.modules.nodeParser import NodeParser
from ast2js.src.util.jscode import JsCode

class Stmt(NodeParser):
    """
    astモジュールで定義されているModに含まれるノードの解析を行う
    """
    def __init__(self, the_function):
        self.recursional_function = the_function
        self.isThisInClass = False
        return
    
    # def convertModule(self, nodes: Module, opt={}):
    #     jscode: JsCode = JsCode()
    #     body = self.recursional_function(nodes.body)
    #     jscode.add(body)
    #     return jscode

    def convert_FunctionDef(self):
        jscode: JsCode = JsCode()
        isThisInClass = self.isThisInClass
        _name, _args, _body = self.parseNodes('name', 'args', 'body')
        name = self.recursional_function(_name)
        args = self.recursional_function(_args)
        print('さいき')
        body = self.recursional_function(_body)
        print('\(・∀・)/')
        print(_name)
        print(_args)
        print(_body)

        print('=== function def ===')
        print('Name:', name, type(name))
        print('Args:', args, type(args))
        print('Body:', body, type(body))
        # for aContent in body:
        #     print('>', aContent)
        # for aContent in name:
        #     print('>>', aContent)
        # for aContent in args:
        #     print('>>>', aContent)

        # args = self.func(v.get('args'), {'list': True})
        # aList = list(filter(lambda x: x not in ['null'], args.get()))
        # aCondition = isinstance(aList, list) and len(aList) == 0
        # args = '' if aCondition else ','.join(aList if len(aList) > 0 else '')
        # func_name = v.get('name')

        # if isThisInClass is True:
        #     func_name = 'constructor' if func_name == '__init__' else func_name
        #     jscode.addln(f'{func_name}({args}) {{')
        # else:
        #     jscode.addln(f'const {func_name} = ({args}) => {{')
        # body = v.get('body', {})
        # _inner_process = self.func(body, opt={'list': True})
        # inner_process = []
        # for item in _inner_process:
        #     inner_process.extend([item for item in str(item).split('\n')])
        # jscode.addln(inner_process)
        # jscode.add_closer()
        # jscode.add_br()
        return jscode

    def convert_AsyncFunctionDef(self, v, opt={}):
        # async def main(): ...のような形
        return self.isFunctionDef(v, opt)

    def convert_ClassDef(self):
        jscode: JsCode = JsCode()
        # print(self.nodes, type(self.nodes))
        _name, _bases, _body = self.parseNodes('name', 'bases', 'body')
        print('\(・ω・)/')
        print(_name)
        print(_bases)
        print(_body)
        name = self.recursional_function(_name)
        bases = self.recursional_function(_bases)
        body = self.recursional_function(_body)

        print('=== ClassDef ===')
        print(_name, _bases, _body)
        # print(name.__dict__)
        print('Name:', name, type(name))
        print('Bases:', bases, type(bases))
        print('Body:', body, type(body))

        # name = v.get('name')
        # class_definition = f'class {name} '
        # if len(v['bases']) != 0:
        #     # 継承処理
        #     extends_classname = self.func(v.get('bases', 0))
        #     jscode.addln(f'{class_definition}extends {extends_classname}{{')
        # else:
        #     jscode.addln('{}{{'.format(class_definition))
        # self.isThisInClass = True
        # body = self.func(v.get('body'), {'list': True})
        # inner_process = []
        # for item in body:
        #     inner_process.extend([item for item in str(item).split('\n')])
        # jscode.add([f'{item}\n' for item in inner_process])
        # jscode.add_closer()
        # self.isThisInClass = False
        return jscode

    def convert_Return(self):
        # print('リターン！俺のターン！')
        jscode: JsCode = JsCode()
        value = self.parseNodes('value')
        if value != []:
            jscode.add(f'return {value}')
        else:
            jscode.add(f'return')
        return jscode

    def convert_Delete(self):
        jscode: JsCode = JsCode()
        jscode.add(self.recursional_function(self.nodes))
        # jscode.add(self.func(v, opt={}))
        return jscode

    def convert_Assign(self):
        jscode: JsCode = JsCode()
        targets = self.parseNodes('targets')
        print('Targets:', targets)
        # variable_name = self.func(deep_get(v, ['targets', 0], ''))
        # value = self.get_assign_variable_type(v.get('value'))
        # keyword = ''
        # if isinstance(value, str) and len(value) > 0:
        #     if value[0].isupper():
        #         value = 'new {}'.format(value)
        # keyword = 'let'
        # jscode.add(f'{keyword} {variable_name} = {value}')
        return jscode

    def convert_AugAssign(self):
        # += -= *= /=等
        jscode: JsCode = JsCode()
        # print('=AUG_ASSIGN=')
        # print(self.nodes.__dict__)
        # print(self.nodes.__dict__['target'].__dict__)
        target = self.recursional_function('target')
        op = self.recursional_function('op')
        value = self.recursional_function('value')
        if op:
            jscode.add(f'{target} {op}= {value}')
        else:
            jscode.add(f'{target} += {value}')
        # print(f'target / op: {target}/{op}')
        # target = v.get('target')
        # _key = v.get('op', {})
        # key = self.func(_key)
        # op = ''
        # if not key == '':
        #     op = f'{key}='
        # else:
        #     op = '+='
        # value = self.func(v.get('value'))
        # left = self.func(target)
        # jscode.add(f'{left} {op} {value}')
        return jscode

    def convert_AnnAssign(self, v, opt={}):
        jscode: JsCode = JsCode()
        jscode.add(self.func(v, opt={}))
        return jscode

    def convert_For(self, v, opt={}):
        jscode: JsCode = JsCode()
        _target = deep_get(v, ['target'], None)
        _iter = deep_get(v, ['iter'], None)
        target = ''
        iter = ''
        childNode = None
        if _target is not None:
            target = self.func(_target)
        if _iter is not None:
            childNode = list(_iter.keys())[0]
            iter = self.func(_iter)
            iter = re.sub(r'range\(([\W|\w]+)\)', r'\1', iter)
            try:
                iter = int(iter)
            except ValueError:
                pass
        if not (target == '' or iter == ''):
            if childNode == 'List':
                jscode.addln(f'for(const {target} of {iter}){{')
            elif childNode == 'Dict':
                jscode.addln(f'for(const {target} in {iter}){{')
            elif isinstance(iter, int):
                jscode.addln('for(let {0}=0; {0} < {1}; {0}++){{'.format(target, iter))
            else:
                jscode.addln(f'for(const {target} in {iter}){{')
            body =  self.func(v.get('body'), {'list': True})
            jscode.add([f'{item}\n' for item in body])
            jscode.add_closer()
        return jscode

    def convert_AsyncFor(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_While(self, v, opt={}):
        jscode: JsCode = JsCode()
        _test = v.get('test')
        _body = v.get('body')
        _orelse = v.get('orelse')
        test = self.func(_test)
        body = [self.func(item) for item in _body]
        orelse = [self.func(item) for item in _orelse]
        
        jscode.addln(f'while({test}){{')
        jscode.addln(body)
        jscode.add_closer()
        jscode.add(orelse)
        return jscode

    def convert_If(self, v, opt={}):
        jscode: JsCode = JsCode()
        _test = v.get('test')
        _body = v.get('body')
        _orelse = v.get('orelse', [])
        orelse = None
        if not (_test is None or _body is None):
            test = self.func(_test)
            body = self.func(_body)
            orelse = self.func(_orelse)
            jscode.addln(f'if({test}) {{')
            jscode.addln(f'{body}')
            jscode.add_closer()
        if not orelse == '':
            else_body = ''
            for item in _orelse:
                else_body += self.func(item)
                if 'If' in item and else_body:
                    jscode.addln(f' else {else_body}}}') #
                else:
                    jscode.addln(' else {')
                    jscode.add(else_body)
                    jscode.add_closer()
        else:
            jscode.add_br
        return jscode

    def convert_With(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_AsyncWith(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Raise(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Try(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Assert(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Import(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_ImportFrom(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Global(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Nonlocal(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Expr(self):
        jscode: JsCode = JsCode()
        print(self.nodes.__dict__)
        value = self.recursional_function('value')
        # for item in value:
        #     print('val:', item)
        val = self._get_flat_list(value)
        print('[value] ', type(val), val)
        jscode.add(self._get_flat_list(value))
        # _value = v.get('value')
        # if _value is not None:
        #     value = self.func(_value)
        #     jscode.add(value)
        return jscode

    def convert_Pass(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Break(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Continue(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_attributes(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def get_assign_variable_type(self, aVariable):
        if 'func' in aVariable:
            func_name = self.func(aVariable.get('func'))
            args = ''
            if 'args' in aVariable:
                args = ', '.join([item['value'] for item in aVariable['args']])
            return '{}({})'.format(func_name, args)
        else:
            return self.func(aVariable)