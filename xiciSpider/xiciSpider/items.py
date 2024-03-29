# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetproxyItem(scrapy.Item):  # scrapy.Item 最终继承的是 BaseItem
    # define the fields for your item here like:
    # name = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    type = scrapy.Field()
    location = scrapy.Field()
    protocol = scrapy.Field()
    source = scrapy.Field()
