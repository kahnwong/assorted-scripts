from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from readability import Document


def get_chapters(url):
    """Get all chapters"""
    source_code = requests.get(url).content
    soup = BeautifulSoup(source_code, "html.parser")

    chapters = []
    for scrape in soup.find_all("div", class_="entry-content"):
        for link in scrape.find_all("a"):
            link = link.get("href")

            try:
                if "chapter" in link:
                    # ~ print(link)
                    chapters.append(link)

            except:
                pass
                # ~ print('nothing to see here')

    # ~ print(chapters)
    print("getting chapters done")
    return chapters


def doc_clean_up(chapter):
    """Scrape"""
    response = requests.get(chapter)
    doc = Document(response.text)
    summary = doc.summary()

    return summary


def chapter_name(chapter):
    parsed = urlparse(chapter)
    chapter_name_raw = parsed.path.replace("/", "").split("-")[1:]

    for index, i in enumerate(chapter_name_raw):
        if "chapter" in i:
            chapter_name_raw[index + 1] += ":"

    chapter_name_joined = " ".join(chapter_name_raw).title()
    # ~ print(chapter_name_joined)
    return chapter_name_joined


# """Filename"""
# parsed = urlparse(url)
# filename = parsed.path.split('/')[-1].split('-')[-1] + '.html'
#
# """Dump"""
# with open(filename, 'a') as f:
#     f.write(summary)


# for chapter in urls:
#     create_html(chapter)
#     print('Download ' + chapter + ' complete!')


def main():
    url = "https://wwyxhqc.wordpress.com/vw/table-of-contents/"
    chapters = get_chapters(url)
    # ~ print(chapters)

    for chapter in chapters:
        summary = doc_clean_up(chapter)
        # ~ print(summary)
        # ~ break

        title = chapter_name(chapter)
        # ~ print(title)

        with open("test.html", "a") as f:
            f.write("<h1>" + title + "</h1>")
            f.write(summary)
            print("----", title, "done ----")


main()
