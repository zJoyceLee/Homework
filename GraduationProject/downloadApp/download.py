import requests
import sys

try:
    url  = sys.argv[1]
    dest = sys.argv[2]
    res = requests.get(url)
    with open('{}'.format(sys.argv[2]), 'bw') as f:
        f.write(res.content)
except:
    print('USAGE: python download.py [download-url] [save-path]')
