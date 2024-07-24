import os
from multiprocessing import Pool
from time import sleep

import requests
from tqdm import tqdm


WALLABAG_CLIENT_ID = os.getenv("WALLABAG_CLIENT_ID")
WALLABAG_CLIENT_SECRET = os.getenv("WALLABAG_CLIENT_SECRET")
WALLABAG_USERNAME = os.getenv("WALLABAG_USERNAME")
WALLABAG_PASSWORD = os.getenv("WALLABAG_PASSWORD")


def _get_access_token() -> str:
    payload = {
        "grant_type": "password",
        "client_id": WALLABAG_CLIENT_ID,
        "client_secret": WALLABAG_CLIENT_SECRET,
        "username": WALLABAG_USERNAME,
        "password": WALLABAG_PASSWORD,
    }

    r = requests.post("https://wallabag.karnwong.me/oauth/v2/token", data=payload)

    return r.json()["access_token"]


access_token = _get_access_token()


def add_article(url: str, access_token: str = access_token):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    r = requests.post(
        "https://wallabag.karnwong.me/api/entries.json",
        headers=headers,
        json={"url": url},
    )

    sleep(4)

    if r.status_code != 200:
        raise TypeError


if __name__ == "__main__":
    with open("urls.txt", "r") as f:
        urls = [i.strip() for i in f.readlines()][:40]

    with Pool(4) as p:
        r = list(
            tqdm(
                p.imap(
                    add_article,
                    urls,
                ),
                total=len(urls),
            )
        )
