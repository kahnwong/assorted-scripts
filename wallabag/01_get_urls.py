from time import sleep

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

urls = [
    f"https://www.gourmetandcuisine.com/going_out_eating/more?page={i}&txt_search="
    for i in range(1, 105 + 1)
]


with open("urls.txt", "a") as f:
    for url in tqdm(urls):
        # print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        sleep(0.25)

        entries = [
            i.get("href")
            for i in soup.select(
                "div.eating_content_more div.border_content_eatings2.bg_content a"
            )
        ]

        entries = [i for i in entries if "detail" in i]
        f.writelines([i + "\n" for i in entries])

        # break
