# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

from bs4 import BeautifulSoup
def has_href_and_title(tag):
    return tag.has_attr('href') and tag.has_attr('title')


class JobSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["http://blog.jobbole.com/"]
    start_urls = [
        "http://python.jobbole.com/87284/?utm_source=blog.jobbole.com&utm_medium=relatedPosts"
    ]

    def parse(self, response):
        print('----------response----------')
        print(response)
        print('----------response----------')
        soup = BeautifulSoup(response.body)
        content_lst = soup.find_all(has_href_and_title)
        print('**********Content**********')
        [print('''--link--{}
                   \n--title--{}
                   \n--text--{}\n'''
               .format(
                   x.get('href'),
                   x.get('title'),
                   x.get_text())
                ) for x in content_lst]
        print('**********Content**********')
