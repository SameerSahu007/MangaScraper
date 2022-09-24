# https://hunterxhuntermanga.online/


import requests
from bs4 import BeautifulSoup
 
 
url = 'https://hunterxhuntermanga.online/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
data = soup.find_all('li', 'ceo_latest_comics_widget')

chapter = []
for div in data:
    chapter.extend(div.find_all('a'))

chapter_links = []
for link in chapter:
    chapter_links.append(link.get('href'))

# print(chapter_links[55])



