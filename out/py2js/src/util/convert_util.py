#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

def body_joiner(aList, indent):
    body_ = [f'{indent.get()}{aString}' for aString in aList]
    body = '\n'.join(body_)
    return body