import urllib.request
from bs4 import BeautifulSoup

userid = 360743
ncategory = 1
url = ("http://mypage.syosetu.com/mypagefavnovelmain/list/userid/" +
       str(userid)+ "/?nowcategory=" +
       str(ncategory))

response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")

# bookmarks = soup.find_all("div", id="novellist")
# print(bookmarks)
# print(type(bookmarks))

# links = bookmarks.find_all("li", class_="title")

links = soup.find_all("li", class_="title")
# print(links)

for link in links:
    print (link.find("a").get("href"))
