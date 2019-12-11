#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     test
   Description :
   Author :        ZYZ
   date：          2019/12/10
"""

# 测试 pipelines
from xiciSpider.pipelines import GetproxyPipeline

pipeLine = GetproxyPipeline()

item = {'ip': '123.623.88.23', 'port': '8888', 'protocol': 'http', 'type': '高匿', 'loction': '福建',
        'source': 'sourceTest'}

pipeLine.process_item(item, None)


