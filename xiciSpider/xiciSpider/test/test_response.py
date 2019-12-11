#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     test_response
   Description :
   Author :        ZYZ
   date：          2019/12/10
"""

from scrapy.selector import Selector

from xiciSpider.spiders.proxyXiciSpider import ProxyXiciSpider

with open('./xici_response.xml', 'r') as fp:
    body = fp.read()
    bodySelector = Selector(text=body)
    # print('result=' + str(bodySelector.xpath('/*').extract()))
    xiciSpider = ProxyXiciSpider()
    xiciSpider.processData(bodySelector)