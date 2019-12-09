#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

# from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware   		scrapy 1.6 时 scrapy.contrib 已弃用并改到新包: scrapy.downloadermiddlewares
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from xiciSpider.middlewares.resource import UserAgents
import random

class RandomUserAgent(UserAgentMiddleware):
    def process_request(self,request,spider):
      ua = random.choice(UserAgents)
      request.headers.setdefault('User-Agent', ua)
