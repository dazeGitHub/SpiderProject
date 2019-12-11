#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

from xiciSpider.utils.resource import Resource
from xiciSpider.utils.cust_log import CustLog

import random


class RandomProxy(object):

    def __init__(self):
        self.proxys = Resource.get_proxy()
        self.myLog = CustLog()

    def process_request(self, request, spider):
        if len(Resource.get_proxy()) != 0:
            proxy = random.choice(Resource.get_proxy())
            self.myLog.info('random choice proxy = %s' % proxy)
            # request.meta['proxy'] = 'http://%s' % proxy
