#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     pipelines2mysql
   Description :
   Author :        ZYZ
   date：          2019/12/11
"""
import os.path
import pymysql

from xiciSpider.data.db import db_data


class ToMysqlPipeline(object):
    def process_item(self, item, spider):
        cityDate = item['cityDate'].encode('utf8')
        week = item['week'].encode('utf8')
        img = os.path.basename(item['img'])
        temperature = item['temperature'].encode('utf8')
        weather = item['weather'].encode('utf8')
        wind = item['wind'].encode('utf8')

        conn = pymysql.connect(host=db_data['host'], port=db_data['port'], user=db_data['user'],
                               password=db_data['password'], db=db_data['db'],
                               charset=db_data['charset'])
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO weather(cityDate,week,img,temperature,weather,wind) values('%s','%s','%s','%s','%s','%s')" % (
                    cityDate, week, img, temperature, weather, wind))
            conn.commit()  # 提交执行
        except:
            # 发生错误时回滚
            conn.rollback()
        cursor.close()  # 关闭游标
        conn.close()  # 最后关闭连接
        return item
