import urllib.request
import re
from bs4 import BeautifulSoup

userid = 360743
ncategory = 1
url = ("http://mypage.syosetu.com/mypagefavnovelmain/list/userid/" +
       str(userid)+ "/?nowcategory=" +
       str(ncategory))

response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "lxml")

# bookmarks = soup.find_all("div", id="novellist")
# print(bookmarks)
# print(type(bookmarks))

# links = bookmarks.find_all("li", class_="title")

all_count_raw = str(soup.find("span", class_="allcount").string)
total_bookmarks = re.search("\d+", all_count_raw).group()
print(total_bookmarks)

# TODO: 全ページにやる。
# TODO: さすがにゴミみたいなスライスをなんとかする。
re_novel_id = re.compile("https://ncode.syosetu.com/[a-z0-9]+/")
links = str(soup.find_all("li", class_="title"))
list_bookmarks = re_novel_id.findall(links)
print(list_bookmarks)
for bookmark in list_bookmarks:
    print (bookmark[26:-1])
