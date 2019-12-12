#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     pipelines2json
   Description :
   Author :        ZYZ
   date：          2019/12/11
"""
import os
import time
import json
import codecs

from xiciSpider.utils.path_utils import get_root_path


class ToJsonPipeline(object):

    def process_item(self, item, spider):
        jsonFileName = os.path.join(get_root_path(), 'build/proxy.json')
        with codecs.open(jsonFileName, 'a', encoding='utf8') as fp:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            fp.write(line)
        return item
