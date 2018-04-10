import datetime
from urllib.request import urlopen
from functools import wraps
import _utils


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


class Ranking():
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
        raw_response = urlopen(defaultrank_url + "&rtype=" + date + "-d")
        rank = _utils.json_to_dictionary(raw_response=raw_response)

        return rank

    @validator
    def weekly(self, year, month, day):
        """
            weekly ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        raw_response = urlopen(defaultrank_url + "&rtype=" + date + "-w")
        rank = _utils.json_to_dictionary(raw_response=raw_response)

        return rank

    @validator
    def monthly(self, year, month, day):
        """
            monthly ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        raw_response = urlopen(defaultrank_url + "&rtype=" + date + "-m")
        rank = _utils.json_to_dictionary(raw_response=raw_response)

        return rank

    @validator
    def quarterly(self, year, month, day):
        """
            quaeterly ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        raw_response = urlopen(defaultrank_url + "&rtype=" + date + "-q")
        rank = _utils.json_to_dictionary(raw_response=raw_response)

        return rank


if __name__ == '__main__':
    # print(monthly(year=2017, month=9, day=1))
    # print(len(monthly(year=2017, month=9, day=1)))
    rank = Ranking()
    print(rank.monthly(year=2017, month=9, day=1))
    pass
