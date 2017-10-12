import urllib.request
import re
from bs4 import BeautifulSoup


def get_all_bookmarks(userid, category):
    url = ("http://mypage.syosetu.com/mypagefavnovelmain/list/userid/" +
           str(userid) + "index.php?nowcategory=" +
           str(category) + "&p=1")
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, "html.parser")

    page_count_html = str(soup.find("div", class_="pager_kazu"))
    pattern_digit = r"^[0-9]+$"
    m = pattern_digit.search(page_count_html, 0)
    print(page_count_html)
    print(m)
    page_count_num = page_count_html[m.start():m.end()]
    print(page_count_html)
    print(page_count_num)


def bookmarks_from_page(userid, category, page):
    url = ("http://mypage.syosetu.com/mypagefavnovelmain/list/userid/" +
           str(userid) + "index.php?nowcategory=" +
           str(category) + "&p=" + str(page))

    print(url)

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
        ncode = full_url.replace("https://ncode.syosetu.com/", "").replace("/", "")
        bookmarks.append(ncode)

    print(bookmarks)


if __name__ == "__main__":
    # bookmarks_from_page(userid=360743, category=1, page=1)
    get_all_bookmarks(userid=360743, category=1)
