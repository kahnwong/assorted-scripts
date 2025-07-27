import os

from dotenv import load_dotenv

import miniflux

load_dotenv()

# env
MINIFLUX_HOST = os.getenv("MINIFLUX_HOST")
MINIFLUX_TOKEN = os.getenv("MINIFLUX_TOKEN")

# init
client = miniflux.Client(f"https://{MINIFLUX_HOST}", api_key=MINIFLUX_TOKEN)


feeds = []

for feed in feeds:
    print(feed)
    client.create_feed(feed_url=f"{feed}", category_id=65)
