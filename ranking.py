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

        ranking_with_details = self.__details_from_rankings(ranking_data=response)
        return ranking_with_details

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

        ranking_with_details = self.__details_from_rankings(ranking_data=response)
        return ranking_with_details

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

        ranking_with_details = self.__details_from_rankings(ranking_data=response)
        return ranking_with_details

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

        ranking_with_details = self.__details_from_rankings(ranking_data=response)
        return ranking_with_details

    def __details_from_rankings(self, ranking_data):
        """
            private utils
        """

        with gzip.open(ranking_data, "rt", encoding="utf-8") as f:
            j_raw = f.read()

        json_object = json.loads(j_raw)
        ret = []
        for nowrank in json_object:
            print(nowrank)
            details = utils.detail_from_ncode(nowrank["ncode"])
            if len(details) > 0:
                details["pt"] = nowrank["pt"]
                details["rank"] = nowrank["rank"]
                ret.append(details)

        return ret


if __name__ == '__main__':
    print(Ranking().daily(year=2013, month=5, day=2))
