import urllib.request
import re
from bs4 import BeautifulSoup
import _utils

# FIXME: これconstantsに逃がす
defaultrank_url = "http://api.syosetu.com/rank/rankget/?out=json&gzip=5"


class Naropy:
    def __init__(self):
        pass

    @_utils.ranking_validator
    def ranking_daily(self, year, month, day):
        """
            daily ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        raw_response = urllib.request.urlopen(defaultrank_url + "&rtype=" + date + "-d")
        rank = _utils.json_to_dictionary(raw_response=raw_response)

        return rank

    @_utils.ranking_validator
    def ranking_weekly(self, year, month, day):
        """
            weekly ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        raw_response = urllib.request.urlopen(defaultrank_url + "&rtype=" + date + "-w")
        rank = _utils.json_to_dictionary(raw_response=raw_response)

        return rank

    @_utils.ranking_validator
    def ranking_monthly(self, year, month, day):
        """
            monthly ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        raw_response = urllib.request.urlopen(defaultrank_url + "&rtype=" + date + "-m")
        rank = _utils.json_to_dictionary(raw_response=raw_response)

        return rank

    @_utils.ranking_validator
    def ranking_quarterly(self, year, month, day):
        """
            quaeterly ranking
            :param year    int after 2013
            :param month   int
            :param day     int
        """
        date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
        raw_response = urllib.request.urlopen(defaultrank_url + "&rtype=" + date + "-q")
        rank = _utils.json_to_dictionary(raw_response=raw_response)

        return rank

    def bookmark_get_all(self, userid, category):
        url = ("http://mypage.syosetu.com/mypagefavnovelmain/list/userid/" +
               str(userid) + "index.php?nowcategory=" +
               str(category) + "&p=1")
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, "html.parser")
        all_count_raw = str(soup.find("span", class_="allcount").string)
        total_bookmarks = int(re.search("\d+", all_count_raw).group())

        all_bookmarks = []
        for page in range(int(total_bookmarks / 10)):
            now_bookmarks = self.bookmarks_from_page(userid=userid,
                                                     category=category,
                                                     page=page)
            all_bookmarks.extend(now_bookmarks)

        return all_bookmarks

    def bookmark_get_from_page(self, userid, category, page):
        url = ("http://mypage.syosetu.com/mypagefavnovelmain/list/userid/" +
               str(userid) + "index.php?nowcategory=" +
               str(category) + "&p=" + str(page))
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, "html.parser")

        links = soup.find_all("li", class_="title")

        bookmarks = []
        for link in links:
            full_url = link.find("a").get("href")
            # TODO: ゴミ、ダメ、なんとかする
            ncode = full_url[26:-1]
            bookmarks.append(ncode)

        return bookmarks


if __name__ == '__main__':
    # print(monthly(year=2017, month=9, day=1))
    # print(len(monthly(year=2017, month=9, day=1)))
    naropy = Naropy()
    print(naropy.ranking_monthly(year=2017, month=9, day=5))
    pass
