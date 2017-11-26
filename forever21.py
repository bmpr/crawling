# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ClothItem(scrapy.Item):
    title = scrapy.Field()
    size_label = scrapy.Field(serializer=str)
    color = scrapy.Field(serializer=str)
    image = scrapy.Field(serializer=str)
    price = scrapy.Field()

class ZaraSpider(CrawlSpider):
    name = 'forever21'
    allowed_domains = ['forever21.co.kr']
    start_urls = ['http://www.forever21.co.kr/']

    rules = (
        Rule(LinkExtractor(allow=('productid', 'ProductID')), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=('category',), deny=('br=acc', 'br=shoesnbag', 'br=f21_acc', 'br=f21_shoesnbag')), follow=True),
    )

    def parse_item(self, response):
        cloth = ClothItem()
        cloth['title'] = response.xpath('//h1[@class="item_name_p"]/text()').extract_first()
        cloth['size_label'] = response.xpath('//ul[@id="ulProductSize"]//label/text()').extract()
        cloth['color'] = response.xpath('//ul[@id="ulProductColor"]//img/@alt').extract()
        cloth['price'] = response.xpath('//span[@id="spanProductPrice"]/text()').extract_first()
        image = response.xpath('//li[contains(@id, "liImageButton")]//img/@src').extract()
        cloth['image'] = list(map(lambda x: x.replace('_58/', '_750/'), image))
        return cloth
