import requests
import json

with open('./source/url.json', 'r') as src:
    d = json.load(src)

    for key, value  in d.items():
        res = requests.get('{}'.format(value))
        with open('./download/{}.jpg'.format(key), 'bw') as  f:
            f.write(res.content)
