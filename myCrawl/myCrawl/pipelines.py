# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class MycrawlPipeline(object):
    def process_item(self, item, spider):
        return item
# 
# class DuplicatesPipeline(object):
#
#     def __init__(self):
#         self.ids_seen = set() #중복 허용 안함
#
#     def process_item(self, item, spider):
#         if item['page_no'] in self.ids_seen:
#             raise DropItem("Duplicate item found: %s" % item['page_no'])
#         else:
#             self.ids_seen.add(item['page_no'])
#             return item
