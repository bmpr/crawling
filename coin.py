import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class Product(scrapy.Item):
    sub = scrapy.Field(serializer=str)
    # nickname = scrapy.Field(serializer=str)
    # date = scrapy.Field()
    # searchCount = scrapy.Field()

class CoinpanSpider(CrawlSpider):
    name = 'coin'
    allowed_domains = ['coinpan.com']
    start_urls = ['https://coinpan.com/free']

    rules = (
        Rule(LinkExtractor(allow=('free', )), callback='parse_item'),
    )

    def parse_item(self, response):
        board = Product()

        div = response.xpath('//*[@id="board_list"]/table/thead/tr/th')

            for a in div.xpath('//span'):
                print a.extract()
        board['sub'] = response.xpath('//*[@id="board_list"]/table/thead/tr/th[2]/span/text()').extract()
        board['nickname'] = response.xpath('//*[@id="board_list"]/table/thead/tr/th[3]/span/text()').extract()
        board['date'] = response.xpath('//*[@id="board_list"]/table/thead/tr/th[4]/span/a/text()').extract()
        board['searchCount'] = response.xpath('//*[@id="board_list"]/table/thead/tr/th[5]/span/a/@href').extract()
        print(board)
        return board
