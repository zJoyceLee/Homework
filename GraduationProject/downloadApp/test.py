import requests
import json

class downloader:
    def __init__(self, myurl, myname):
        self.url = myurl
        self.thread_num = 8
        self.name = '{}{}'.format(myname, myurl[myurl.rfind('.'):])
        r = requests.head(self.url)
        self.total = int(r.headers['Content-length'])
        print('{}\ntotal is {}.'.format(self.url, self.total))
    def get_range(self):
        ranges = []
        offset = int(self.total / self.thread_num)
        for i in range(self.thread_num):
            if i == self.thread_num - 1:
                ranges.append((i*offset, ''))
            else:
                ranges.append((i*offset,  (i+1)*offset))
        return ranges
    def run(self, dest):
        with open('{}/{}'.format(dest, self.name), 'bw') as f:
            for piece  in self.get_range():
                res =  requests.get(
                    self.url,
                    headers={
                        'Range': 'Bytes={}-{}'.format(piece[0], piece[1]),
                        'Accept-Encoding': '*'
                    }
                )
                f.seek(piece[0])
                f.write(res.content)



with open('./source/url.json', 'r') as src:
    d = json.load(src)
    for key, value  in d.items():
        down = downloader(key, value)
        down.run('download')
