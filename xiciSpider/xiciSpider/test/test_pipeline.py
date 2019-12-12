#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     test
   Description :
   Author :        ZYZ
   date：          2019/12/10
"""

# 测试 pipelines
from xiciSpider.pipelines.pipelines2txt import ToTxtPipeline
from xiciSpider.pipelines.pipelines2csv import ToCsvPipeline
from xiciSpider.pipelines.pipelines2json import ToJsonPipeline
from xiciSpider.pipelines.pipelines2mysql import ToMysqlPipeline
from xiciSpider.pipelines.pipelines2mongodb import ToMongoDbPipeline

item = {'ip': '123.623.88.23', 'port': '8888', 'protocol': 'http', 'type': '高匿', 'location': '福建',
        'source': 'sourceTest'}

# print('测试 ToTxtPipeline')
# txtPipeline = ToTxtPipeline()
# txtPipeline.process_item(item, None)

# print('测试 ToCsvPipeline')
# csvPipeLine = ToCsvPipeline()
# csvPipeLine.process_item(item, None)
#
print('测试 ToJsonPipeline')
jsonPipeLine = ToJsonPipeline()
jsonPipeLine.process_item(item, None)

# print('测试 Mysql Pipeline')
# mysqlPipeLine = ToMysqlPipeline()
# mysqlPipeLine.process_item(item,None)

# print('测试 MongoDb Pipeline')
# mongoDbPipeLine = ToMongoDbPipeline()
# mongoDbPipeLine.process_item(item,None)
