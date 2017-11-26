# -*- coding: utf-8 -*-
import scrapy
from myCrawlI.items import MycrawliItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from myCrawlI.loaders import ChatLoader
import re

class CointalkSpider(CrawlSpider):
    name = 'cointalk'
    allowed_domains = ['cointalk.co.kr']
    start_urls = ['http://cointalk.co.kr/bbs/board.php?bo_table=freeboard']

    rules = (
        Rule(LinkExtractor(allow=('wr_id=\d+$', )), callback="parse_item"),
    )

    def parse_item(self, response):
        l = ChatLoader(item=MycrawliItem(), response=response)
        l.add_xpath('subject', '//h4[@class="subject"]/text()', re='[^\t\n]*')
        l.add_xpath('user_id', '//div[@class="dropdown"]/a/strong/text()')
        l.add_xpath('write_date', '//*[@id="st-view"]/div/div/strong[1]/text()', re="\d{4}-\d{1,2}-\d{1,2}")

        header = l.nested_xpath('//div[@class="desc"]')
        header.add_xpath('view_count', '//strong[2]/text()')
        header.add_xpath('comment_count', '//strong[3]/text()')

        # l.add_xpath('content', '//*[@id="st-view"]/section[1]/article/text()')
        return l.load_item()
