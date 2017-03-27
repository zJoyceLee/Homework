# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

class JobSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["http://blog.jobbole.com/"]
    start_urls = [
        "http://python.jobbole.com/87284/?utm_source=blog.jobbole.com&utm_medium=relatedPosts"
    ]

    def parse(self, response):
        selector = Selector(response)
        content_list = selector.xpath('//*[@class="meta-title"]')
        print('**********Content**********')
        for content in content_list:
            topic = content.xpath('string(.)').extract_first()
            print('========topic==========',topic)
            # url =  content.xpath('@herf').extract_first()
            # print('========url==========',url)
        print('**********Content**********')
