# https://hunterxhuntermanga.online/
import requests
import os 
from bs4 import BeautifulSoup

 
 
url = 'https://hunterxhuntermanga.online/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

data = soup.find_all('li', 'ceo_latest_comics_widget')

chapter = []
for div in data:
    chapter.extend(div.find_all('a'))

chapter_links = []
for link in chapter:
    chapter_links.append(link.get('href'))

for x in range(56, 58):
    print(f'Chapter {x} Downloading....')
    reqs = requests.get(chapter_links[x])
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    data = soup.find_all('div', 'entry-inner')

    image = []
    for y in data:
        image.extend(y.find_all('img'))

    image_urls = []
    for z in image:
        image_urls.append(z.get('src'))
    
    ch = 'Chapter '+ str(x)
    file_location = os.path.join( "Manga",ch)
    os.makedirs(file_location)
        
    for link in image_urls:
        with open( os.path.join(file_location, os.path.basename(link)), "wb") as f:
            f.write(requests.get(link).content)
    