#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

# import ast
import re
def atopy(aString):
    anotherString = ''
    data_type = ''
    if re.match(r'\[(\w|\W)+\]', aString):
        # こっちは問題なく動作
        anotherString = eval(aString)
        data_type = 'list'
    elif re.match(r'\{(\w|\W)+\}', aString):
        # 動作未確認
        anotherString = dict(aString)
        data_type = 'dict'
    elif re.match(r'range\((\w|\W)+\)', aString):
        anotherString = str(re.sub(r'range\(([\W|\w]+)\)', r'\1', aString))
        data_type = 'range'
    else:
        # 一旦保留
        return aString, 'else'
    return anotherString, data_type