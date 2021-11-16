import ast
# from pprint import pprint
# from get_abstract_tree.parser import parse_nodes
from py2js.translator import Translator
class Example:
    def __init__(self):
        return

    def main(self): # コメントなのだ
        print('Hello World')
        self.hello_world()
        print(self.str_join('Hello', 'World.'))
        print(self.equals('A', 'A'))
        a = b = 1
        for i in range(5):
            print(i)
        for j in [1, 2, 3]:
            print(j)
        aDict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
        aList = [1, 2, 3]
        anotherList = [item if item < 10 else item + 10 for item in aList]
        n = 5
        it = [1, 3, 5, 7, 9]
        aNumber = 111
        aNumber += 12
        aNumber -= 0
        aNumber = 100
        aString = 'String'
        aString = 'not String'
        for k in aDict:
            print(aDict[k])
        self.f(1, 2, 3, 4, 5)
        self.do_try()
    
    def do_try(self):
        a = 0
        b = 1
        print('try-catch')
        try:
            print(a / b)
        except Exception as e:
            print(e)
        print('try-catch-finally')
        try:
            print(a / b)
        except Exception as e:
            print(e)
        finally:
            print('ファイナリー')
        print('try-catch-else')
        try:
            print(a / b)
        except Exception as e:
            print(e)
        else:
            print('else')
        print('try-catch-else-finally')
        try:
            print(a / b)
        except Exception as e:
            print(e)
        else:
            print('else')
        finally:
            print('finally')
    
    # 追加
    def hello_world(self):
        hello = 'Hello World'
        return hello

    def str_join(self, *strings):
        res = ''
        for aString in strings:
            res += aString
        # return ''.join(strings)
        return res

    def equals(self, aString='', anotherString=''):
        return aString == anotherString
    
    def f(self, a, b=2, *c, **d):
        if a > b:
            print(1)
        elif a == b:
            print(2)
        elif a == d:
            print(2.5)
        else:
            print(3)
        
        if c == d:
            print(4)
        else:
            print(5)
        while b > 0:
            if a > b:
                print(1)
            elif a == b:
                print(2)
            else:
                print(3)
            
            if c == d:
                print(4)
            else:
                print(5)
            b -= 1
        return

def aFunction():
    a = 5
    b = a - 1
    anotherFunction(b)

def anotherFunction(x):
    print(x)

if __name__ == '__main__':
    example = Example()
    example.main()