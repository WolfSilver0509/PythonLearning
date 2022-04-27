
import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
titres = soup.find_all("a", class_="gem-c-document-list__item-title")
for title in titres: print(title.string)
descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
for p in descriptions: print(p.string)