#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     test_log
   Description :
   Author :        ZYZ
   date：          2019/12/10
"""
from colorlog import ColoredFormatter
import logging
import getpass

LOG_LEVEL = logging.DEBUG

LOGFORMAT = "  %(log_color)s%(asctime)s  %(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT)

stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)

user = getpass.getuser()
log = logging.getLogger(user)
log.setLevel(logging.DEBUG)
log.addHandler(stream)

# log = logging.getLogger('pythonConfig')
# log.setLevel(LOG_LEVEL)
# log.addHandler(stream)

log.debug("This is debug.")
log.info("This is info.")
log.warning("This is warning.")
log.error("This is error.")
log.critical("This is critical.")