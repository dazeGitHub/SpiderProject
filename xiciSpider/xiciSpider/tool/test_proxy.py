#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试 proxy.txt 中的代理是否可用，将可用代理写入 alive.txt
import time
import urllib.request

# 测试 alive.txt 中的代理是否可用
from xiciSpider.data.resource import Resource
from xiciSpider.utils.log_utils import LogUtils


class TestProxy(object):

    def __init__(self):
        self.URL = r'http://www.cctv.com/'
        self.timeout = 3
        self.myLog = LogUtils()
        # self.run()

    # protocol: http        server: http://123.23.45.4:8080
    def link_with_server_port(self, protocol, server) -> bool:
        # self.myLog.info('link_with_server_port currentThreadName=%s' % threading.currentThread().getName())
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({protocol: server}))
        urllib.request.install_opener(opener)
        try:
            response = urllib.request.urlopen(self.URL, timeout=self.timeout)
        except Exception as e:
            self.myLog.warn('使用代理 %s connect failed, exception=%s' % (server, e))
            return False
        else:
            self.myLog.info('成功得到响应数据,响应码%s' % response.code)
            try:
                readResultStr = response.read().decode()  # response.read() 返回的是 bytes 格式，所以需要 decode()
            except Exception as e2:
                self.myLog.warn('%s connect response.read() failed, exception=%s' % (server, e2))
                return False
            if str(response.code) == '200':
                self.myLog.info('%s 请求成功' % self.URL)
                return True
            else:
                self.myLog.info('%s 请求失败' % self.URL)
                return False


if __name__ == '__main__':
    tp = TestProxy()
    for ele in Resource.get_proxy():
        print('开始测试代理: ele=%s' % ele)
        protocol = ele[0:ele.index(':')]
        tp.link_with_server_port(protocol, ele)
        time.sleep(7)
