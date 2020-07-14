import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.uol.com.br")
soup = BeautifulSoup(page.content,'html.parser')
div = soup.find(class_='mod-horizontal topo-hibrido grid-row has-banner-970x250')
div2 = div.find_all(class_='chapeu color1')
div3 = div.find_all(class_='titulo color2')
titles = [items.get_text() for items in div2]
hightitles = [coisas.get_text() for coisas in div3]
print(titles,hightitles)
