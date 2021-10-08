import json
from time import sleep

import requests
from bs4 import BeautifulSoup

urls = []


def crawler(url):
    def main(url):
        source_code = requests.get(url, allow_redirects=True).content
        soup = BeautifulSoup(source_code, "html.parser")
        sleep(0.25)

        try:  # if next page exists
            # get next page button
            # token = json_data['paging']['next']

            # next page url
            token = soup.select_one("div.nav-next > a").get("href")  # have to use '>'
            print(token)

            # print('')
        except AttributeError:
            token = ""
        finally:
            # print('dummy')

            #  DO SOME SHIT
            """Edit scrape here"""
            articles = [
                i.get("href")
                for i in soup.select("main#site-main > article.post > header > h2 > a")
            ]
            print(articles)

            urls.extend(articles)

            # for scrape in soup.find_all(id='content'):
            #     for a in scrape.select('h2 > a'):
            #         # print(a)
            #         article = a.get('href')
            #         urls.append(article)
            #         print(article)
            """End scrape"""

        return token

    token = main(url)

    while token:  # debug
        token = main(token)

    # urls = urls[::-1]
    # parsed = urlparse(url).netloc.split('.')[0]

    # filename = 'blog'
    #
    # with open(filename + '.json', 'a') as file_object:
    #     json.dump(urls, file_object, indent=4)
    #     print(filename, 'exported!')


blog_links = [
    "https://randomwire.com/cambodia/",
    "https://randomwire.com/architecture/",
    "https://randomwire.com/china/hong-kong/",
    "https://randomwire.com/china/taiwan/",
    "https://randomwire.com/culture/",
    "https://randomwire.com/design/",
    "https://randomwire.com/europe/",
    "https://randomwire.com/food/",
    "https://randomwire.com/general/",
    "https://randomwire.com/history/",
    "https://randomwire.com/tech/",
    "https://randomwire.com/thailand/",
    "https://randomwire.com/travel/hotels/",
    "https://randomwire.com/travel/outdoors/",
    "https://randomwire.com/university/",
]

# crawler()

for i in blog_links:
    crawler(i)

filename = "randomwire"

with open(filename + ".json", "w") as file_object:
    json.dump(urls, file_object, indent=4)
    print(filename, "exported!")
