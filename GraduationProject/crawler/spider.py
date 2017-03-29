# -*- coding: utf-8 -*-
import sys
import time
import requests
from bs4 import BeautifulSoup

class Spider(object):
    def __init__(self):
        self.url = ''
        try:
            self.url = sys.argv[1]
        except:
            # self.url = 'http://blog.jobbole.com/'
            self.url = "http://v.youku.com/v_show/id_XMjYxMDUzNjg1Mg==.html"
            print('[USAGE]:  python spider.py [url]')
            print('Default url: {}'.format(self.url))
            time.sleep(3)

    def has_href_and_title(self, tag):
        return tag.has_attr('href') and tag.has_attr('title')

    def has_href_and_class(self, tag):
        return  tag.has_attr('href') and tag.has_attr('class')

    def parse(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content)
        content_lst = soup.find_all(self.has_href_and_title)
        content_lst = soup.find_all(attrs={"class": "sn"})
        print('**********C-ontent**********')
        [print(x.get('href')) for x in content_lst]
        print('total: {}'.format(len(content_lst)))
        print('**********Content**********')

s = Spider()
s.parse()
