#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

from xiciSpider.middlewares.resource import PROXIES
import random


class RandomProxy(object):

    def process_request(self, request, spider):
        if len(PROXIES) != 0:
            proxy = random.choice(PROXIES)
            request.meta['proxy'] = 'http://%s' % proxy
