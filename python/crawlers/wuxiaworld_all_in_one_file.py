from time import sleep

import requests
from readability import Document


def chapter_urls(start, end):
    return [
        "http://www.wuxiaworld.com/iras-index/iras-chapter-" + str(i)
        for i in range(start, end + 1)
    ]


# urls = chapter_urls(204, 284)
summaries = []


def get_content(url):
    """Scrape"""
    response = requests.get(url)
    doc = Document(response.text)
    summary = doc.summary()

    return summary


def create_html(filename, summaries):
    summaries = "".join(summaries)

    # """Filename"""
    # parsed = urlparse(url)
    # filename = parsed.path.split('/')[-1].split('-')[-1] + '.html'

    """Dump"""
    with open(filename + ".html", "a") as f:
        f.write('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/>')
        f.write(summaries)


i = 204
# end = 217
end = 284
while i <= end:
    url = "http://www.wuxiaworld.com/iras-index/iras-chapter-" + str(i)
    summaries.append(get_content(url))
    print("Download " + str(i) + " complete!")
    sleep(0.25)
    i += 1

create_html("IRAS #3 - WebTV Arc", summaries)
