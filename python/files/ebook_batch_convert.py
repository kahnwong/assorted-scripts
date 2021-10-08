# by Kovid Goyal and edited a bit by me
import glob
import os
import subprocess
import time

files = glob.glob("*.html")

workers = []
while files or workers:
    while len(workers) < 4 and files:
        f = files[0]
        files = files[1:]
        w = subprocess.Popen(["ebook-convert", f, os.path.splitext(f)[0] + ".epub"])
        workers.append(w)
    for w in list(workers):
        if w.poll() is not None:
            workers.remove(w)
    time.sleep(0.1)
