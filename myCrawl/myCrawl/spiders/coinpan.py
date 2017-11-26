# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from myCrawl.items import MycrawlItem
from scrapy.http import FormRequest
import re
import config
from myCrawl.loaders import ChatLoader

class CoinpanSpider(CrawlSpider):
    name = 'coinpan'
    allowed_domains = ['coinpan.com']
    start_urls = ['https://coinpan.com/index.php?mid=index&act=dispMemberLoginForm']
    rules = (
        Rule(LinkExtractor(allow=('/free$', 'index.php?mid=coin_info&page=\d+$', )), callback="parse_item"),
        # Rule(LinkExtractor(allow=('/free/\d+$', 'document_srl=\d+',)), callback="parse_item")
    )

    def parse_start_url(self, response):
        self.logger.info('request login!')
        return FormRequest.from_response(
            response,
            formdata={'user_id': config.ID, 'password': config.PASSWORD},
            formxpath='//fieldset'
        )

    def parse_item(self, response):
        l = ChatLoader(item=MycrawlItem(), response=response)
        l.add_xpath('title', '//div[@class="read_header"]//a/text()')
        l.add_xpath('page_no', '//p[@class="perlink"]//@href', re='coinpan.com/(\d+)')
        l.add_xpath('content', '//div[@class="read_body"]//div[contains(@class, "xe_content")]')
        l.add_xpath('comment', '//div[@id="comment"]//div[contains(@class, "xe_content")]/text()')

        header = l.nested_xpath('//*[@id="board_list"]/table/tbody/tr')


        header = l.nested_xpath('//ul[@class="wt_box gray_color"]//li')
        header.add_xpath('uploaded_at', '//span', re='\d{4}\.\d{2}\.\d{2}\W+\d{2}:\d{2}')
        header.add_xpath('comment_count', 'a[@href="#comment"]//b/text()')

        header.add_xpath('good_count', '//a[contains(text(), "추천")]//b/text()')
        header.add_xpath('bad_count', '//a[contains(text(), "비추천")]//b/text()')
        header.add_xpath('view_count', '//a[contains(text(), "조회")]//b/text()')

        return l.load_item()
