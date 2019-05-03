# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GuokeSpider(CrawlSpider):
    name = 'guoke'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/ask/highlight']

    rules = (
        # 列表页的url
        Rule(LinkExtractor(allow=r'/ask/highlight/\?page=\d+'), follow=True),
        # 详情页的url
        Rule(LinkExtractor(allow=r'https://www.guokr.com/question/\d+/'), callback='parse_item')
    )

    def parse_item(self, response):
        item = {}
        item["article"] = response.xpath('//div/h1[@id="articleTitle"]/text()').extract_first()
        item["desc"] = response.xpath("//div[@id='questionDesc']/p/text()").extract_first()
        print(item)

