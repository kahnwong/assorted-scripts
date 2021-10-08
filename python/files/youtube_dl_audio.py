from __future__ import unicode_literals

import glob
import os
import shutil

import youtube_dl

source_dir = "/Users/kahnwong/Music/Audio"
os.chdir(source_dir)
dest_dir = "/Users/kahnwong/Nextcloud/Audio"


def my_hook(d):
    if d["status"] == "finished":
        print("Done downloading")


ydl_opts = {
    # 'format': 'bestaudio/best',
    "format": "bestaudio[ext!=webm]/best[ext!=webm]",
    # 'format': 'bestvideo[ext!=webm]+bestaudio[ext!=webm]/best[ext!=webm]',
    # 'logger': MyLogger(),
    "progress_hooks": [my_hook],
}

with open("/Users/kahnwong/Nextcloud/youtube_urls.txt", "r") as f:
    # with open('youtube_urls.txt', 'r') as f:
    urls = [i.strip().split("&list=")[0] for i in f]

i = 0
for url in urls[:]:
    urls.pop(i)
    i -= 1

    # do something cool with x or just print x
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    i += 1

    with open("/Users/kahnwong/Nextcloud/youtube_urls.txt", "w") as f:
        for text in urls:
            f.write(text)
            f.write("\n")

files = glob.glob("*.m4a")
for i in files:
    shutil.move(i, dest_dir)
