# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MycrawliItem(scrapy.Item):
    subject = scrapy.Field()
    view_count = scrapy.Field()
    user_id = scrapy.Field()
    comment_count = scrapy.Field()
    write_date = scrapy.Field()
    content = scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
