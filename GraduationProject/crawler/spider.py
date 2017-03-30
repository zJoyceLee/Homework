# -*- coding: utf-8 -*-
import sys
import time
import requests
from bs4 import BeautifulSoup

class Spider():
    def __init__(self):
        self.url = ''
        try:
            self.url = sys.argv[1]
        except:
            self.url = 'http://blog.jobbole.com/'
            print('[USAGE]:  python spider.py [url]')
            print('Default url: {}'.format(self.url))
            time.sleep(3)


    def get_a_href_title(tag):
        return tag.tag.has_attr('href') and tag.has_attr('title')

    def parse(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content)
        content_lst = soup.find_all('a')
        print('**********C-ontent**********')
        [print('''--link--{}
                   \n--title--{}
                   \n--text--{}\n\n'''
               .format(
                   x.get('href'),
                   x.get('title'),
                   x.get_text())
               ) for x in content_lst]
        print('**********Content**********')

s = Spider()
s.parse()
