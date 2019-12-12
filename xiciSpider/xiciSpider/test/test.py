#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     test
   Description :   测试默认参数可以直接赋值 int 或 dict 等类型
   Author :        ZYZ
   date：          2019/12/11
"""


class Test:
    def __init__(
            self,
            document_class=int,
            **kwargs):
        print(type(document_class))


Test()  # <class 'type'>
Test(document_class=20)  # <class 'int'>
