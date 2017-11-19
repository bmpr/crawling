# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from myCrawl.items import MycrawlItem

class CoinpanSpider(CrawlSpider):
    name = 'coinpan'
    allowed_domains = ['coinpan.com']
    start_urls = ['http://coinpan.com/index.php?mid=free&page=1']

    rules = (
        Rule(LinkExtractor(allow=('index.php\?mid=free&page=\d+$', )), follow=True),
        Rule(LinkExtractor(allow=('document_srl=\d+',)), callback="parse_item")
    )

    def parse_item(self, response):
        print('Current page is "%s"' % response.url)

        item = MycrawlItem()
        item['subject'] = response.xpath('//div[contains(@class, "read_header")]/h1/a/text()').extract()
        item['contents'] = response.xpath('//div[contains(@class, "read_body")]/div/p/text()').extract()
        item['level'] = response.xpath('//ul[contains(@class, "wt_box gray_color")]/li/a/img//@alt').extract()
        item['searchCount'] = response.xpath('//li[contains(@class, "right")]/a/span/b/text()').extract()

        print(item)
        return item
