import os

current_dir = os.getcwd()
dirs = os.listdir()
dirs = [i for i in dirs if ".py" not in i]

# print(artist_directories)

# filepaths = []

# for artist in artist:
#     for root, directories, files in os.walk(artist, topdown=True):
#         for directory in directories:
#             filepath = os.path.join(root, directory).replace('\\', ' - ')
#             print(filepath)
#             filepaths.append(filepath)


with open("audiobooks_list.txt", "w", encoding="utf-8") as file:
    for i in dirs:
        file.write(i + " " + "@audiobook +media" + "\n")


# for root, directories, files in os.walk(current_dir):
#     for directory in directories:
#         filepath = os.path.join(root, directory)
#         print(filepath)


# for filename in files:
#     if filename.endswith('.jpg'):
#         filepath = os.path.join(root, filename)
#         cover_paths.append(filepath)
#         print(filepath)

# for index, cover in enumerate(cover_paths):
#     shutil.copy(cover, destination_directory + str(index) + '.jpg')
# print('----DONE----')
