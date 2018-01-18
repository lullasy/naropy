import urllib.request
import re
from bs4 import BeautifulSoup


def get_all_bookmarks(userid, category):
    url = ("http://mypage.syosetu.com/mypagefavnovelmain/list/userid/" +
           str(userid) + "index.php?nowcategory=" +
           str(category) + "&p=1")
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, "html.parser")
    all_count_raw = str(soup.find("span", class_="allcount").string)
    total_bookmarks = int(re.search("\d+", all_count_raw).group())

    # TODO: 全部のブクマ数がわかるので、10で割ってpager_kazuを無視する！
    all_bookmarks = []
    for page in range(int(total_bookmarks / 10)):
        now_bookmarks = bookmarks_from_page(userid=userid,
                                            category=category,
                                            page=page)
        all_bookmarks.extend(now_bookmarks)

    return all_bookmarks


def bookmarks_from_page(userid, category, page):
    url = ("http://mypage.syosetu.com/mypagefavnovelmain/list/userid/" +
           str(userid) + "index.php?nowcategory=" +
           str(category) + "&p=" + str(page))
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, "html.parser")

    # bookmarks = soup.find_all("div", id="novellist")
    # print(bookmarks)
    # print(type(bookmarks))

    # links = bookmarks.find_all("li", class_="title")

    links = soup.find_all("li", class_="title")
    # print(links)

    bookmarks = []
    for link in links:
        full_url = link.find("a").get("href")
        # TODO: ゴミ、ダメ、直す
        ncode = full_url[26:-1]
        bookmarks.append(ncode)

    # print(bookmarks)
    return bookmarks


if __name__ == "__main__":
    # bookmarks_from_page(userid=360743, category=1, page=1)
    get_all_bookmarks(userid=360743, category=1)
    bookmarks_from_page(userid=360743, category=1, page=1)
