import json
from urllib.request import urlopen
import gzip

# FIXME: これconstantsに逃がす
default_url = "http://api.syosetu.com/novelapi/api/?out=json&gzip=5"


def json_to_dictionary(raw_response):
    with gzip.open(raw_response, "rt", encoding="utf-8") as f:
        j_raw = f.read()

    json_object = json.loads(j_raw)

    return json_object


def detail_from_ncode(ncode):
    response = urlopen(default_url + "&ncode=" + ncode)
    with gzip.open(response, "rt", encoding="utf-8") as f:
        raw = f.read()
    ret = json.loads(raw)
    if ret[0]["allcount"] == 0:
        return {}
    return ret[1]


def details_from_list(ncode_list):
    ret = []
    for nowrank in ncode_list:
        detail = detail_from_ncode(nowrank["ncode"])
        if len(detail) > 0:
            detail["pt"] = nowrank["pt"]
            detail["rank"] = nowrank["rank"]
            ret.append(detail)

    return ret
