import requests
import json

with open('./source/url.json', 'r') as src:
    d = json.load(src)

    for key, value  in d.items():
        h = {'Range': 'Bytes=0-15000', 'Accpet-Encoding': '*'}

        res = requests.get('{}'.format(value), headers=h)
        with open('./download/{}.jpg'.format(key), 'bw') as  f:
            f.write(res.content)
