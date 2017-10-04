import gzip
import json
import datetime
from urllib.request import urlopen
from functools import wraps
import utils


# FIXME: これconstantsに逃がす
defaultrank_url = "http://api.syosetu.com/rank/rankget/?out=json&gzip=5"


# http://kk6.hateblo.jp/entry/20120616/1339803112
def validator(func):
    @wraps(func)
    def _validator(*args, **kwargs):
        year = int(kwargs['year'])
        month = int(kwargs['month'])
        day = int(kwargs['day'])
        date = datetime.date(year, month, day)
        func_name = _validator.__name__

        # 20130501 以降
        if 0 > (date - datetime.date(2013, 5, 1)).days:
            return []

        # 週間ランキングは火曜日のみ
        if func_name == "weekly" and date.weekday() != 1:
            return []

        # 月刊、四半期は1日のみ
        if (func_name == "monthly" or func_name == "quarterly") and day != 1:
            return []

        return func(*args, **kwargs)
    return _validator


class Ranking:
    """
        get ranking
    """

    def __init__(self):
        pass

    @validator
    def daily(self, year, month, day):
        """
            daily ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        response = urlopen(defaultrank_url + "&rtype=" + date + "-d")

        details = self.__details_from_ranking(ranking_data=response)
        return details

    @validator
    def weekly(self, year, month, day):
        """
            weekly ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        response = urlopen(defaultrank_url + "&rtype=" + date + "-w")

        details = self.__details_from_ranking(ranking_data=response)
        return details

    @validator
    def monthly(self, year, month, day):
        """
            monthly ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        response = urlopen(defaultrank_url + "&rtype=" + date + "-m")

        details = self.__details_from_ranking(ranking_data=response)
        return details

    @validator
    def quarterly(self, year, month, day):
        """
            quaeterly ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        response = urlopen(defaultrank_url + "&rtype=" + date + "-q")

        details = self.__details_from_ranking(ranking_data=response)
        return details

    def __details_from_ranking(self, ranking_data):
        """
            private utils
        """

        with gzip.open(ranking_data, "rt", encoding="utf-8") as f:
            j_raw = f.read()

        json_object = json.loads(j_raw)
        ret = []
        for nowrank in json_object:
            print(nowrank)
            detail = utils.detail_from_ncode(nowrank["ncode"])
            if len(detail) > 0:
                detail["pt"] = nowrank["pt"]
                detail["rank"] = nowrank["rank"]
                ret.append(detail)

        return ret


if __name__ == '__main__':
    print(Ranking().monthly(year=2017, month=9, day=1))
