#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 测试 proxy.txt 中的代理是否可用，将可用代理写入 alive.txt

import urllib2
import re
import threading
from xiciSpider.custLog import CustLog

class TestProxy(object):

   def __init__(self):
        #字符串前面加 r 就不用管其中的特殊字符了，即整体转义
      self.sFile = r'proxy.txt'      # 全部代理.txt
      self.dFile = r'alive.txt'      # 可用代理.txt
      self.URL = r'http://www.baidu.com/'
      self.threads = 10
      self.timeout = 3
      self.regex = re.compile(r'baidu.com')
      self.aliveList = []
      self.myLog = CustLog()
      self.run()

   def run(self):
      with open(self.sFile, 'r') as fp:
         lines = fp.readlines()
         line = lines.pop()
         # 这段代码感觉始终有问题。。
         while lines:
            for i in range(self.threads):
               self.myLog.info('TestProxy run threadIndex=%d,line=%s'%(i,line))
               t = threading.Thread(target=self.linkWithProxy, args=(line,))
               t.start() #这里线程并没有 join()，可能主线程先执行完，
            #    if lines:
               line = lines.pop()
            #    else:
            #       continue
      if len(self.aliveList) !=0:
        with open(self.dFile, 'w') as fp:
            for i in range(len(self.aliveList)):
                fp.write(self.aliveList[i])
      else:
          self.myLog.info('')

   def linkWithProxy(self, line):
       self.myLog.info('linkWithProxy line=%s'%(line))
    #   lineList = line.split('\t')
    #   protocol = lineList[2].lower()
    #   server = protocol + r'://' + lineList[0] + ':' + lineList[1]
    #   opener = urllib2.build_opener(urllib2.ProxyHandler({protocol:server}))
    #   urllib2.install_opener(opener)
    #   try:
    #      response = urllib2.urlopen(self.URL, timeout=self.timeout)
    #   except:
    #      self.myLog.info('%s connect failed' %server)
    #      return
    #   else:
    #      try:
    #         str = response.read()
    #      except:
    #         self.myLog.info('%s connect failed' %server)
    #         return
    #      if self.regex.search(str):
    #         self.myLog.info('%s connect success ..........' %server)
    #         self.aliveList.append(line)

if __name__ == '__main__':
   TP = TestProxy()