import os
import shutil


sorce_dir = r"D:\gPodder"
dest_dir = "E:\Podcasts\VA"
# dest_dir = r'D:\Podcasts_test'

os.makedirs(dest_dir, exist_ok=True)

for root, dirs, files in os.walk(sorce_dir):
    #    for name in files:
    #       print(os.path.join(root, name))
    for name_dir in dirs:  # podcast folders
        dir = os.path.join(root, name_dir)

        for root2, folder, sub_files in os.walk(dir):
            episodes = len(sub_files) - 1  # to ignore cover.jpg
            if episodes < 10:  # not long podcasts, like only a few eps
                for i in sub_files:
                    if i.endswith("mp3"):
                        ep_full_path = os.path.join(dir, i)
                        print(ep_full_path)

                        shutil.copy(ep_full_path, dest_dir)
