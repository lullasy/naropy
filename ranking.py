import gzip
import json
from urllib.request import urlopen
import utils


# FIXME: これconstantsに逃がす
defaultrank_url = "http://api.syosetu.com/rank/rankget/?out=json&gzip=5"


class Ranking:
    """
        get ranking
    """

    def __init__(self):
        pass

    def daily(self, year, month, day):
        """
            daily ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        # TODO: validation 20130501 以降でないとダメ
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        response = urlopen(defaultrank_url + "&rtype=" + date + "-d")

        details = self.__details_from_ranking(ranking_data=response)
        return details

    def weekly(self, year, month, day):
        """
            weekly ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        # TODO: validation 20130501 以降 && 火曜日でないとダメ
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        response = urlopen(defaultrank_url + "&rtype=" + date + "-w")

        details = self.__details_from_ranking(ranking_data=response)
        return details

    def monthly(self, year, month, day):
        """
            monthly ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        # TODO: validation 20130501 以降 && 1日でないとダメ
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        response = urlopen(defaultrank_url + "&rtype=" + date + "-m")

        details = self.__details_from_ranking(ranking_data=response)
        return details

    def quarterly(self, year, month, day):
        """
            quaeterly ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        # TODO: validation 20130501 以降 && 1日でないとダメ
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
