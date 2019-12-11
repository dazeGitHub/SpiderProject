# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# 用来运行 spiders 文件夹中的 xxSpider 文件，但是运行不了，总是报找不到 xxSpider 文件?? KeyError: 'Spider not found: proxy360Spider.py'
'''
@File    :   test_pipeline.py
@Time    :   2019/12/09 14:18:29
@Author  :   ZYZ
@Version :   1.0
@Contact :   zyz163mail@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

import os
from scrapy.cmdline import execute

projectBaseName = 'xiciSpider'

spidersFolderpath = os.path.join(os.getcwd(), 'spiders')
print('spidersFolderpath=%s' % (spidersFolderpath))
spiderFiles = os.listdir(spidersFolderpath)  # 得到文件夹下的所有文件名称
spiderFileList = []

for file in spiderFiles:  # 遍历文件夹
    if not os.path.isdir(file) and str(file).find('Spider') != -1:  # 判断是否是文件夹
        spiderFileList.append(file)

intputInfo = '请输入想运行的 Spider 文件序号:\n'
for index in range(len(spiderFileList)):
    # print('找到了 Spider 文件:%s'%(str(file))) 
    intputInfo += (str(index) + ":" + str(spiderFileList[index]) + "\n")

wantRunIndex = int(input(intputInfo))
print('开始运行%s:%s' % (wantRunIndex, spiderFileList[wantRunIndex]))

cmd = '开始运行 %s' % spiderFileList[wantRunIndex]
print(cmd)
# os.system('cd %s \n cd %s \n %s'%(projectBaseName,projectBaseName,cmd))
realSpiderName = spiderFileList[wantRunIndex].split(".")[-2]
print(' 如果出现 Spider not found 错误，请检查 Spider 文件的 name 值是否和其文件名相同 ')
execute(['scrapy', 'crawl', realSpiderName])
