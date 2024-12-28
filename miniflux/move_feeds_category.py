import os

from dotenv import load_dotenv

import miniflux

load_dotenv()

# env
MINIFLUX_HOST = os.getenv("MINIFLUX_HOST")
MINIFLUX_TOKEN = os.getenv("MINIFLUX_TOKEN")

# init
client = miniflux.Client(f"https://{MINIFLUX_HOST}", api_key=MINIFLUX_TOKEN)

# get subscribed bluesky accounts
source_category_id = 32
# target_category_id=44 # tech
target_category_id = 12  # culture, news, politics
feeds = client.get_category_feeds(category_id=source_category_id)
for i in feeds:
    client.update_feed(i["id"], category_id=target_category_id)
    print(f"Updated {i["id"]}")
    # break
