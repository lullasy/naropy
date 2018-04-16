import json
from urllib.request import urlopen
import gzip
import datetime
from functools import wraps

# FIXME: これconstantsとかに逃がしたい
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


# http://kk6.hateblo.jp/entry/20120616/1339803112
def ranking_validator(func):
    @wraps(func)
    def _ranking_validator(*args, **kwargs):
        year = int(kwargs['year'])
        month = int(kwargs['month'])
        day = int(kwargs['day'])
        date = datetime.date(year, month, day)
        func_name = _ranking_validator.__name__

        # 20130501 以降
        if 0 > (date - datetime.date(2013, 5, 1)).days:
            return []

        # 週間ランキングは火曜日のみ
        if func_name == "ranking_weekly" and date.weekday() != 1:
            return []

        # 月刊、四半期は1日のみ
        if (func_name == "ranking_monthly" or func_name == "ranking_quarterly") and day != 1:
            return []

        return func(*args, **kwargs)
    return _ranking_validator
