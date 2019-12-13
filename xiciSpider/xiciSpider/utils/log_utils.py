#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File    :   test_pipeline.py
@Time    :   2019/12/09 14:18:29
@Author  :   ZYZ
@Version :   1.0
@Contact :   zyz163mail@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   只有错误才会被记录到 logfile 中,使用 print() + 自定义颜色防止 logging 打印到控制台 log 两次
"""

import logging
import getpass
import os
import sys
from colorlog import ColoredFormatter

from xiciSpider.utils.path_utils import get_root_path


class LogUtils(object):
    # 语法: echo -e "\033[字背景颜色；文字颜色m字符串\033[0m"
    # 例如 echo -e "\033[41;36m something here \033[0m", 41的位置代表底色， 36的位置是代表字的颜色
    COLOR_DEFAULT_WHITE = "\033[0m"  # 默认白色
    COLOR_RED = '\033[91m'  # 红色
    COLOR_YELLOW = '\033[33m'  # 黄色
    COLOR_YELLOW_LIGHT = '\033[93m'  # 亮黄色
    COLOR_PINK = '\033[95m'  # 粉色
    COLOR_CYAN = "\033[96m"  # 青色
    COLOR_GREEN = "\033[32m"  # 绿色
    COLOR_BLUE = '\033[34m'  # 蓝色
    COLOR_BLACK = "\033[97m"  # 黑色

    def __init__(self):  # 类 CustLog 的构造函数
        LOG_LEVEL = logging.DEBUG

        LOGFORMAT = "  %(log_color)s%(asctime)s  %(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
        logging.root.setLevel(LOG_LEVEL)
        # formatter = ColoredFormatter(LOGFORMAT)

        # stream = logging.StreamHandler()
        # stream.setLevel(LOG_LEVEL)
        # stream.setFormatter(formatter)
        #
        user = getpass.getuser()
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)
        # self.logger.addHandler(stream)

        # ---------- 输出日志到文件 ----------
        # 切片操作list[<start>:<stop>:<step>] ，step 可以为负数，表示倒着数
        # 如果 python testCustLog.py 则 sys.argv[0][0:-3] 正好可以得到 testMyLog，即日志文件名为  testCustLog.log，并放到 log 目录下
        logFile = os.path.join(get_root_path(), 'log/' + os.path.basename(sys.argv[0][0:-3]) + '.log')  # 日志文件名

        # %(asctime)s :   字符串形式的当前时间。默认格式是“2003-07-08 16:49:45,896”。逗号后面的是毫秒
        # %(levelname)s	: 文本形式的日志级别
        # %(name)s :      Logger的名字
        # %(message)s	: 用户输出的消息
        logFormatStr = '%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s'
        formatter = logging.Formatter(logFormatStr)

        if not os.path.exists(logFile):
            print('%s 文件不存在,开始创建' % logFile)
            file = open(logFile, 'w')
            file.close()

        # 日志输出到日志文件内
        logHandFile = logging.FileHandler(logFile)
        logHandFile.setFormatter(formatter)
        logHandFile.setLevel(logging.ERROR)  # 只有错误才会被记录到 logfile 中

        self.logger.addHandler(logHandFile)

    # 日志的 5 个级别对应以下 5 个函数
    def debug(self, msg):
        print(LogUtils.COLOR_DEFAULT_WHITE, 'DEBUG: ' + msg)
        self.logger.debug(msg)

    def info(self, msg):
        print(LogUtils.COLOR_YELLOW, 'INFO: ' + msg)
        self.logger.info(msg)

    def warn(self, msg):
        print(LogUtils.COLOR_PINK, 'WARN: ' + msg)
        self.logger.warning(msg)

    def error(self, msg):
        print(LogUtils.COLOR_RED, 'ERROR: ' + msg)
        self.logger.error(msg)

    def critical(self, msg):  # [ˈkrɪtɪkl] 批评的
        print(LogUtils.COLOR_RED, 'CRITICAL: ' + msg)
        self.logger.critical(msg)

    def test_color(self, color):
        print(color, '测试')


if __name__ == '__main__':
    mylog = LogUtils()
    mylog.debug("I'm debug")
    mylog.info("I'm info")
    mylog.warn("I'm warn")
    mylog.error("I'm error")
    mylog.critical("I'm critical")

    # mylog.test_color(LogUtils.COLOR_DEFAULT_WHITE)
    # mylog.test_color(LogUtils.COLOR_RED)
    # mylog.test_color(LogUtils.COLOR_YELLOW)
    # mylog.test_color(LogUtils.COLOR_YELLOW_LIGHT)
    # mylog.test_color(LogUtils.COLOR_PINK)
    # mylog.test_color(LogUtils.COLOR_CYAN)
    # mylog.test_color(LogUtils.COLOR_GREEN)
    # mylog.test_color(LogUtils.COLOR_BLUE)
    # mylog.test_color(LogUtils.COLOR_BLACK)