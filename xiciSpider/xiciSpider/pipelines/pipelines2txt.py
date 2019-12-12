# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

from xiciSpider.utils.log_utils import LogUtils
from xiciSpider.utils.path_utils import get_root_path


class ToTxtPipeline(object):
    myLog = LogUtils()

    def process_item(self, item, spider):
        fileName = os.path.join(get_root_path(), 'build/proxy.txt')
        # self.myLog.info('开始写入到%s，item=%s' % (fileName, item))
        with open(fileName, 'a') as fp:
            fp.write(item['ip'] + '\t')
            fp.write(item['port'] + '\t')
            fp.write(item['protocol'] + '\t')
            fp.write(item['type'] + '\t\t')  # 中文则加两个 \t 防止对不齐
            fp.write(item['location'] + '\t\t')
            fp.write(item['source'] + '\n')
        return item
