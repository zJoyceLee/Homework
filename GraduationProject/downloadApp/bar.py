from progressbar import ProgressBar
import requests

url = "http://jbcdn2.b0.upaiyun.com/2017/03/d0e5d9795c14684deb0ab99fc2291c17.gif"
res = requests.get(url)
total = int(res.headers.get('Content-Length'))
n = 100
offset = int(total/n)
pieces =  []
for i in range(n):
    if i == (n-1):
        pieces.append((i*offset, ''))
    else:
        pieces.append((i*offset,  (i+1)*offset))

pbar = ProgressBar(maxval=n)

with open('./download/bar.gif', 'wb') as f:
    for i, piece in  enumerate(pieces):
        start, end = piece
        h = {'Range': 'Bytes={}-{}'.format(start, end), 'Accept-Encoding': '*'}
        res = requests.get(url, headers = h)
        f.write(res.content)
        pbar.update(i)

pbar.finish()
