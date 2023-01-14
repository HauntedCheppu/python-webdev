import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.google.com/")

soup = BeautifulSoup(res.content, 'html.parser')
# print(soup.title.parent)
for i in soup.find_all('a', class_="WwrzSb"):
    print("\n",i['aria-label'])
    print("https://news.googlei.com/"+i.get('href'))
