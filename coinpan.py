# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class CoinpanSpider(CrawlSpider):
    name = 'coinpan'
    allowed_domains = ['coinpan.com']
    start_urls = ['https://coinpan.com/index.php?mid=free&page=1']

    rules = (
        Rule(LinkExtractor(allow=('index.php\?mid=free&page=\d+$', )), follow=True),
        Rule(LinkExtractor(allow=('document_srl=\d+',)), callback="parse_item')
    )

    def parse_item(self, response):
        print('Current page is "%s"' % response.url)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
