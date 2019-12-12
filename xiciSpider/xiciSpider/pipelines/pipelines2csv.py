#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     pipelines2csv
   Description :
   Author :        ZYZ
   date：          2019/12/11
"""
import csv
import os

from xiciSpider.utils.log_utils import LogUtils
from xiciSpider.utils.path_utils import get_root_path


class ToCsvPipeline(object):
    myLog = LogUtils()

    def process_item(self, item, spider):
        csvFileName = os.path.join(get_root_path(), 'build/proxy.csv')
        # self.myLog.info('开始写入到%s，item=%s' % (csvFileName, item))

        with open(csvFileName, 'w+') as file:
            columns = ['ip', 'port', 'protocol', 'type', 'location', 'source']
            csvfile = csv.DictWriter(file, columns)
            # 写入 csv 文件列名
            csvfile.writeheader()
            # 写入行数据
            csvfile.writerow({
                'ip': item['ip'],
                'port': item['port'],
                'protocol': item['protocol'],
                'type': item['type'],
                'location': item['location'],
                'source': item['source']
            })
        return item
