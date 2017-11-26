    # data = MycrawlItem()
    #
    # pattern = 'document_srl=(\d+)'
    # data['page_no'] = re.search(pattern, response.url).group(1)
    #
    # data['title'] = response.xpath('//div[@class="read_header"]').extract_first()
    # # data['content'] = response.xpath('//div[@class="read_body"]//div/text()').extract_first()
    # content = response.xpath('//div[@class="read_body"]//div[contains(@class, "xe_content")]').extract_first()
    # data['content'] = re.sub('<[A-Za-z\/][^>]*>', '', content)
    # data['comment'] = response.xpath('//div[@id="comment"]//div[contains(@class, "xe_content")]/text()').extract()
    #
    # data_set = response.xpath('//ul[@class="wt_box gray_color"]//li')
    # data['uploaded_at'] = data_set.re_first('\d{4}\.\d{2}\.\d{2}\W+\d{2}:\d{2}')
    # data['comment_count'] = data_set.xpath('a[@href="#comment"]//b/text()').extract_first()
    # print(data)
    # return data
    # print('Current page is "%s"' % response.url)
    #
    # item = MycrawlItem()
    # item['subject'] = response.xpath('//div[contains(@class, "read_header")]/h1/a/text()').extract()
    # item['contents'] = response.xpath('//div[contains(@class, "read_body")]/div/p/text()').extract()
    # item['level'] = response.xpath('//ul[contains(@class, "wt_box gray_color")]/li/a/img//@alt').extract()
    # item['searchCount'] = response.xpath('//li[contains(@class, "right")]/a/span/b/text()').extract()
    #
    # print(item)
    # return item
