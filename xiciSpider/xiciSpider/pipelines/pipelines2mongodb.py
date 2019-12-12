#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     pipelines2mongodb
   Description :
   Author :        ZYZ
   date：          2019/12/11
"""

# coding:utf-8
import requests
import json
import pymongo  # 引入模块

from xiciSpider.data.db import db_data


class ToMongoDbPipeline(object):

    def process_item(self, item, spider):
        conn = pymongo.MongoClient(host=db_data['host'], port=db_data['port'])  # 连接到 Mongo
        dbToutiao = conn[db_data['db']]  # 选择或创建数据 库
        newsDataTable = dbToutiao['news']  # 选择或创建数据 表

        # 存储数据到 MongoDB 并读取出来
        title = item['title']
        img_url = item['image_url']
        url = item['media_url']
        data = {
            'title': title,
            'img_url': img_url,
            'url': url
        }
        newsDataTable.insert_one(data)  # 插入一行数据
        return item
