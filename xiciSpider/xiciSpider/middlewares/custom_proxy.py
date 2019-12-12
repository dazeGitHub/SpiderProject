#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

from xiciSpider.data.resource import Resource
from xiciSpider.utils.log_utils import LogUtils

import random


class RandomProxy(object):

    def __init__(self):
        self.proxys = Resource.get_proxy()
        self.myLog = LogUtils()

    def process_request(self, request, spider):
        if len(Resource.get_proxy()) != 0:
            proxy = random.choice(Resource.get_proxy())
            proxy = proxy.replace('\n', '')
            proxy = proxy.strip()
            self.myLog.debug('random choice proxy = %s' % proxy)

            if request.url.startswith("http://"):
                request.meta['proxy'] = "http://180.96.27.12:88"  # http代理
            elif request.url.startswith("https://"):
                request.meta['proxy'] = "http://109.108.87.136:53281"  # https代理