# -*- coding: utf-8 -*-

import scrapy
from scrapy import Selector
from websource.items import WebsourceItem


class WebsourceSpider(scrapy.Spider):
    '''
    爬虫文件
    '''
    name = 'WebsourceSpider'
    allowed_domains = ['51240.com/']
    start_urls = ['https://xingzhengquhua.51240.com/']

    def parse(self, response):
        sel = Selector(response)
        addrs = sel.xpath('.//table//table//td[1]//a/text()').extract()
        codes = sel.xpath('.//table//table//td[2]//a/text()').extract()
        item = WebsourceItem()
        for addr, code in zip(addrs, codes):
            item['addr'] = addr
            item['code'] = code
            yield item
        return None
