import json
from urllib.request import urlopen
import gzip

# FIXME: これconstantsに逃がす
default_url = "http://api.syosetu.com/novelapi/api/?out=json&gzip=5"


def detail_from_ncode(ncode):
    response = urlopen(default_url + "&ncode=" + ncode)
    with gzip.open(response, "rt", encoding="utf-8") as f:
        raw = f.read()
    ret = json.loads(raw)
    if ret[0]["allcount"] == 0:
        return {}
    return ret[1]
