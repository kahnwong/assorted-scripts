import urllib.request

import requests
from bs4 import BeautifulSoup

# import json


def phdcomics_dl(int_page, max_pages):
    actual_comics = []
    page = int_page
    while page <= max_pages:
        url = "http://www.phdcomics.com/comics/archive.php?comicid=" + str(page)
        source_code = requests.get(url, allow_redirects=True)
        plain_text = source_code.text.encode("ascii", "replace")
        soup = BeautifulSoup(plain_text, "html5lib")
        urls = []
        for link in soup.find_all("img", class_="img-responsive"):
            src = link.get("src")
            urls.append(src)
        page += 1
        actual_comics.append(urls[0])
    # ~ print(actual_comics)

    # with open ('phdcomics_images ' + str(int_page) + '-' + str(max_pages)
    #             + '.json', 'w') as file_object:
    #     json.dump(actual_comics, file_object)
    #     print('completed')
    #
    # return actual_comics

    for index, comic in enumerate(actual_comics, int_page):
        urllib.request.urlretrieve(comic, str(index) + ".gif")
        print("Download", comic, "completed!")


phdcomics_dl(401, 402)
