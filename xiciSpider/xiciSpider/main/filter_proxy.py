#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试 proxy.txt 中的代理是否可用，将可用代理写入 alive.txt
import os
import time
import urllib.request
import re
import threading

from xiciSpider.data.resource import Resource
from xiciSpider.utils.log_utils import LogUtils
from xiciSpider.utils.path_utils import get_root_path


class TestProxy(object):

    def __init__(self):
        # 字符串前面加 r 就不用管其中的特殊字符了，即整体转义
        print(get_root_path())  # '/Users/imac/MyDir/Project/PyProject/SpiderProject/xiciSpider/xiciSpider'
        self.totalProxyFile = os.path.join(get_root_path(), 'build/proxy.txt')  # 全部代理.txt
        self.aliveProxyFile = os.path.join(get_root_path(), 'build/alive.txt')  # 可用代理.txt
        self.URL = r'http://www.baidu.com/'
        self.threads = 5  # 10
        self.timeout = 3
        self.regex = re.compile(r'baidu.com')
        self.aliveList = []
        self.myLog = LogUtils()
        # self.run()

    def run(self):
        with open(self.totalProxyFile, 'r') as fp:
            lines = fp.readlines()

            if len(lines) == 0:
                self.myLog.error('读取 %s 内容是空的，退出程序' % self.totalProxyFile)

            perThreadDataSize = 0
            modResult = len(lines) % self.threads
            if modResult == 0:
                perThreadDataSize = len(lines) / self.threads
            else:
                perThreadDataSize = (len(lines) / self.threads) + 1
            perThreadDataSize = int(perThreadDataSize)
            self.myLog.info('len(lines) = %s, self.threads = %s, perThreadDataSize=%s' % (
                len(lines), self.threads, perThreadDataSize))

            threadList = []
            for index in range(self.threads):

                startIndex = index * perThreadDataSize
                if (index + 1) * perThreadDataSize > len(lines):
                    stopIndex = len(lines)
                else:
                    stopIndex = (index + 1) * perThreadDataSize

                # self.myLog.info('len(lines) = %s, startIndex=%s, stopIndex=%s' % (len(lines), startIndex, stopIndex))
                subLine = lines[startIndex: stopIndex]
                # self.myLog.info('TestProxy run threadIndex=%d,切割 lineList=%s' % (index, subLine))
                tempThread = threading.Thread(target=self.link_with_proxy, args=(subLine,))

                self.myLog.debug('开启线程: threadName=%s' % tempThread.name)
                tempThread.start()
                threadList.append(tempThread)
                # tempThread.join()

            for tt in threadList:
                tt.join()

        self.myLog.info('-- thread join 结束,准备写入 alive.txt --')
        if len(self.aliveList) != 0:
            self.myLog.info('self.aliveList 不为空,开始写入 alive.txt, len(aliveList)=%s' % len(self.aliveList))
            with open(self.aliveProxyFile, 'w') as fp:
                for i in range(len(self.aliveList)):
                    fp.write(self.aliveList[i])
                    fp.write('\n')
        else:
            self.myLog.error('self.aliveList 是空的，无法写入到 alive.txt')

    # protocol: http        server: http://123.23.45.4:8080
    def link_with_server_port(self, protocol, server) -> bool:
        self.myLog.info('link_with_server_port currentThreadName=%s' % threading.currentThread().getName())
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({protocol: server}))
        urllib.request.install_opener(opener)
        try:
            response = urllib.request.urlopen(self.URL, timeout=self.timeout)
        except Exception as e:
            self.myLog.warn('%s connect failed, exception=%s' % (server, e))
            return False
        else:
            try:
                readResultStr = response.read().decode()  # response.read() 返回的是 bytes 格式，所以需要 decode()
            except Exception as e2:
                self.myLog.warn('%s connect response.read() failed, exception=%s' % (server, e2))
                return False
            if self.regex.search(readResultStr):
                self.myLog.info('%s connect success ..........' % server)
                return True
            else:
                self.myLog.warn('regex 找不到 baidu.com')
                return False

    def link_with_proxy(self, lineList):
        # self.myLog.info('linkWithProxy line=%s' % line)
        for line in lineList:
            if line.find('HTTP') == -1:
                self.myLog.warn('发现了畸形数据: %s, threadName=%s' % (line, threading.currentThread().getName()))
                return
            lineList = line.split('\t')
            protocol = lineList[2].lower()
            ip_port = lineList[0] + ':' + lineList[1]
            server = protocol + r'://' + ip_port  # http://175.42.158.71:9999
            result = self.link_with_server_port(protocol, server)
            if result:
                self.aliveList.append(server)  # list.append() 是线程安全的，这里只添加 ip 地址:端口号


if __name__ == '__main__':
    tp = TestProxy()
    for ele in Resource.get_proxy():
        print('开始测试代理: ele=%s' % ele)
        protocol = ele[0:ele.index(':')]
        tp.link_with_server_port(protocol, ele)
        time.sleep(1)
    # tp.run()
