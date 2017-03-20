import requests
import sys

try:
    url  = sys.argv[1]
    path = sys.argv[2]
    print('url: {}'.format(url))
    print('path: {}'.format(path))
    res = requests.get(url)
    with open('{}'.format(path), 'bw') as f:
        f.write(res.content)
except:
    print('USAGE: python download.py [download-url] [save-path]')
