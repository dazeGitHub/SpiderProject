#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     interceptor
   Description :   拦截 request 和 response 并打印
   Author :        ZYZ
   date：          2019/12/13
"""
from xiciSpider.utils.log_utils import LogUtils


class InterceptorProxy(object):

    def __init__(self):
        self.myLog = LogUtils()

    def process_request(self, request, spider):
        self.myLog.debug('request=%s' % request)

    def process_response(self, request, response, spider):
        self.myLog.debug('%s 的 response = %s' % (request.url, response))
