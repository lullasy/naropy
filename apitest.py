import json
from urllib.request import urlopen
import gzip
# import time

url = "http://api.syosetu.com/novelapi/api/?out=json&gzip=5"

response = urlopen(url)

with gzip.open(response, "rt", encoding="utf-8") as f:
    j_raw = f.read()

jObj = json.loads(j_raw)

cnt = 1
for a_novel in jObj[1:]:
    print(cnt)
    title = a_novel['title']
    print(title)

    story = a_novel['story']
    print(story)

    cnt += 1

url = "http://api.syosetu.com/rank/rankget/?out=json&gzip=5&rtype=20170906-d"

response = urlopen(url)

with gzip.open(response, "rt", encoding="utf-8") as f:
    j_raw = f.read()

jObj = json.loads(j_raw)

for a_novel in jObj[1:]:
    print(a_novel['rank'])

    code = a_novel['ncode']
    print(code)
    res = urlopen("http://api.syosetu.com/novelapi/api/?out=json&&gzip=5&ncode=" +
                  code)
    with gzip.open(res, "rt", encoding="utf-8") as f:
        raw = f.read()
    tmpjson = json.loads(raw)
    print(tmpjson)
    print(code, tmpjson[1]['title'])

    pt = a_novel['pt']
    print(pt)
