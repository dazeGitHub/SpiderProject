#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'xxx.@qq.com'

import logging
import getpass
import sys

# 定义 CustLog 类
class CustLog(object):
    
    def __init__(self): # 类 CustLog 的构造函数

        # 返回用户的“登录名称”。此函数会按顺序检查环境变量 LOGNAME, USER, LNAME 和 USERNAME，并返回其中第一个被设置为非空字符串的值。 如果均未设置，则在支持 pwd 模块的系统上将返回来自密码数据库的登录名，否则将引发一个异常。
        user = getpass.getuser()
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)

        # 切片操作list[<start>:<stop>:<step>] ，step 可以为负数，表示倒着数
        # 如果 python testCustLog.py 则 sys.argv[0][0:-3] 正好可以得到 testMyLog，即日志文件名为  testCustLog.log
        logFile = './' + sys.argv[0][0:-3] + '.log' # 日志文件名        

        # %(asctime)s :   字符串形式的当前时间。默认格式是“2003-07-08 16:49:45,896”。逗号后面的是毫秒
        # %(levelname)s	: 文本形式的日志级别
        # %(name)s :      Logger的名字
        # %(message)s	: 用户输出的消息
        formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')

        # 日志显示到屏幕上并输出到日志文件内
        logHand = logging.FileHandler(logFile)
        logHand.setFormatter(formatter)
        logHand.setLevel(logging.ERROR) # 只有错误才会被记录到 logfile 中

        logHandSt = logging.StreamHandler()
        logHandSt.setFormatter(formatter)

        self.logger.addHandler(logHand)
        self.logger.addHander(logHandSt)

    # 日志的 5 个级别对应以下 5 个函数
    def debug(self,msg):
        self.logger.debug(msg)

    def info(self,msg):
        self.logger.info(msg)    

    def warn(self,msg):
        self.logger.warn(msg) 

    def error(self,msg):
        self.logger.error(msg)

    def critical(self,msg):         #  [ˈkrɪtɪkl] 批评的
        self.logger.critical(msg)

if __name__ == '__main__':
    mylog = CustLog()
    mylog.debug("I'm debug")
    mylog.info("I'm info")
    mylog.warn("I'm warn")
    mylog.error("I'm error")
    mylog.critical("I'm critical")