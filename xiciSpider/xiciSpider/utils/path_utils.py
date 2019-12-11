#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     path_utils
   Description :
   Author :        ZYZ
   date：          2019/12/11
"""
import os

project_name = 'xiciSpider'


def get_root_path():
    cwdPath = os.getcwd()
    lastIndex = cwdPath.rfind(project_name) + len(project_name)
    return cwdPath[0:lastIndex]


if __name__ == '__main__':
    print(get_root_path())
