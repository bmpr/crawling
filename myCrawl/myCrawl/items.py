# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MycrawlItem(scrapy.Item):
    subject = scrapy.Field()
    contents = scrapy.Field()
    level = scrapy.Field()
    searchCount = scrapy.Field(serializer=str)
    pass
