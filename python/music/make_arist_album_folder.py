import glob
import os
import shutil

folders = glob.glob("*")

for folder in folders:
    if not folder.endswith(".py"):
        artist, album = folder.split(" - ", 1)
        print(artist)
        print("\t" + album)

        os.rename(folder, album)

        try:
            os.mkdir(artist)
        except:
            pass

        shutil.move(album, artist)
