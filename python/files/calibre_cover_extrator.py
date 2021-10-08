import os
import shutil

book_directory = "/Users/kahnwong/Dropbox/Library/Fiction/Ake Edwardson"
destination_directory = "/Users/kahnwong/Dropbox/"

cover_paths = []

for root, directories, files in os.walk(book_directory):
    for filename in files:
        if filename.endswith(".jpg"):
            filepath = os.path.join(root, filename)
            cover_paths.append(filepath)
            print(filepath)

for index, cover in enumerate(cover_paths):
    shutil.copy(cover, destination_directory + str(index) + ".jpg")
print("----DONE----")
