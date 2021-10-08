import os
from time import sleep
from urllib.parse import urlparse

import requests

# from bs4 import BeautifulSoup

images = [
    "http://image.issuu.com/{}/jpg/page_{}.jpg".format(
        "160727183329-c84513b9ced669b322e6e17f386f1b6d", i
    )
    for i in range(1, 180 + 1)
]
# print(images)
folder = "treats 7"

try:
    os.mkdir(folder)
except:
    pass

for image in images:
    parsed = urlparse(image)
    filename = parsed.path.split("/")[-1]

    full_path = folder + "/" + filename

    r = requests.get(image)
    with open(full_path, "wb") as img_obj:
        img_obj.write(r.content)
        print(filename)
    sleep(0.25)
