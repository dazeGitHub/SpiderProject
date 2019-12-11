# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from xiciSpider.custLog import CustLog


class GetproxyPipeline(object):
    myLog = CustLog()

    def process_item(self, item, spider):
        fileName = 'proxy.txt'
        # self.myLog.info('开始写入到%s，item=%s' % (fileName, item))
        with open(fileName, 'a') as fp:
            fp.write(item['ip'] + '\t')
            fp.write(item['port'] + '\t')
            fp.write(item['protocol'] + '\t')
            fp.write(item['type'] + '\t\t')  # 中文则加两个 \t 防止对不齐
            fp.write(item['loction'] + '\t\t')
            fp.write(item['source'] + '\n')
        return item
