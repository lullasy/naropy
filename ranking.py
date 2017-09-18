import json
from urllib.request import urlopen
import gzip
import utils


# FIXME: これconstantsに逃がす
defaultrank_url = "http://api.syosetu.com/rank/rankget/?out=json&gzip=5"


class Ranking:
    """
        get ranking
    """

    def daily(self, date):
        """
            daily ranking
            :param after 20130501
        """
        # TODO: validation 20130501 以降でないとダメ
        response = urlopen(defaultrank_url + "&rtype=" + date + "-d")

        with gzip.open(response, "rt", encoding="utf-8") as f:
            j_raw = f.read()

        json_object = json.loads(j_raw)
        ranking_with_details = []
        for nowrank in json_object:
            print(nowrank)
            details = utils.detail_from_ncode(nowrank["ncode"])
            if len(details) > 0:
                details["pt"] = nowrank["pt"]
                details["rank"] = nowrank["rank"]
                ranking_with_details.append(details)

        return ranking_with_details

    def weekly(self, date):
        """
            daily ranking
            :param after 20130501
        """
        # TODO: validation 20130501 以降 && 火曜日でないとダメ
        response = urlopen(defaultrank_url + "&rtype=" + date + "-w")

        with gzip.open(response, "rt", encoding="utf-8") as f:
            j_raw = f.read()

        json_object = json.loads(j_raw)
        ranking_with_details = []
        for nowrank in json_object:
            print(nowrank)
            details = utils.detail_from_ncode(nowrank["ncode"])
            if len(details) > 0:
                details["pt"] = nowrank["pt"]
                details["rank"] = nowrank["rank"]
                ranking_with_details.append(details)

        return ranking_with_details

    def monthly(self, date):
        """
            daily ranking
            :param after 20130501
        """
        # TODO: validation 20130501 以降 && 1日でないとダメ
        response = urlopen(defaultrank_url + "&rtype=" + date + "-m")

        with gzip.open(response, "rt", encoding="utf-8") as f:
            j_raw = f.read()

        json_object = json.loads(j_raw)
        ranking_with_details = []
        for nowrank in json_object:
            print(nowrank)
            details = utils.detail_from_ncode(nowrank["ncode"])
            if len(details) > 0:
                details["pt"] = nowrank["pt"]
                details["rank"] = nowrank["rank"]
                ranking_with_details.append(details)

        return ranking_with_details

    def quarterly(self, date):
        """
            daily ranking
            :param after 20130501
        """
        # TODO: validation 20130501 以降 && 1日でないとダメ
        response = urlopen(defaultrank_url + "&rtype=" + date + "-q")

        with gzip.open(response, "rt", encoding="utf-8") as f:
            j_raw = f.read()

        json_object = json.loads(j_raw)
        ranking_with_details = []
        for nowrank in json_object:
            print(nowrank)
            details = utils.detail_from_ncode(nowrank["ncode"])
            if len(details) > 0:
                details["pt"] = nowrank["pt"]
                details["rank"] = nowrank["rank"]
                ranking_with_details.append(details)

        return ranking_with_details

if __name__ == '__main__':
    print(Ranking().daily(date='20130502'))
