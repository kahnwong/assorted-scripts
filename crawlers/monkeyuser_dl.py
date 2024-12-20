import requests
from time import sleep
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse

dest_dir = 'Monkeyuser'

try:
    os.mkdir(dest_dir)
except:
    pass

def make_request(url):
    r = requests.get(url)
    r = r.content
    sleep(1)

    return r


def make_soup(html):
    soup = BeautifulSoup(html, 'html.parser')

    return soup


def get_comics_list(archive_html):
    soup = make_soup(archive_html)

    comics = soup.select('div.entry-content a.image-title')
    comics = [i.get('href') for i in comics]
    comics = ['https://www.monkeyuser.com' + i for i in comics]
    comics = comics[::-1] # sort chronologically

    return comics

def download(index, comic):
    r = make_request(comic)
    soup = make_soup(r)

    comic = soup.select('div.content p img')[0]
    comic = comic.get('src')

    sleep(1)

    parsed = urlparse(comic)
    filename = parsed.path.split('/')[-1]
    image_b = requests.get(comic)
    sleep(1)

    with open(dest_dir + '/' + str(index).zfill(4) + ' ' + filename, 'wb') as img_obj:
        img_obj.write(image_b.content)
    print(filename)



def main():
    archive_page = make_request('https://www.monkeyuser.com/toc/')
    comics = get_comics_list(archive_page)

    # for year 2018
    comics = [i for i in comics if '2020' in i]
    print(comics)

    for index, comic in enumerate(comics, 1):
        download(index, comic)

        # break # debug

main()
