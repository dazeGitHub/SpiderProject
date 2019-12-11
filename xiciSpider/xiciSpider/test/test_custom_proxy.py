#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     testCustomProxy
   Description :
   Author :        ZYZ
   date：          2019/12/11
"""
from xiciSpider.middlewares.custom_proxy import RandomProxy

if __name__ == '__main__':
    randomProxy = RandomProxy()
    randomProxy.process_request(None,None)