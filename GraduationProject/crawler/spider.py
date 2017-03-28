# -*- coding: utf-8 -*-
import sys
import time
import requests
from bs4 import BeautifulSoup

def get_a_href_title(tag):
    return tag.has_attr('href') and tag.has_attr('title')

url =  'http://blog.jobbole.com/'
try:
    url = sys.argv[1]
except:
    print('[USAGE]:  python spider.py [url]')
    print('Default url: {}'.format(url))
    time.sleep(3)

print(url)
res = requests.get(url)

soup = BeautifulSoup(res.text)
# print(soup.prettify())
content_lst = soup.find_all(get_a_href_title)

[print('href: {}\ntitle: {}\ntext: {}\n'.format(x.get('href'), x.get('title'),x.get_text())) for x in content_lst]
