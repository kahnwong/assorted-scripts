import glob
import os
import shutil

folders = glob.glob("*")

for folder in folders:
    name_new = folder.split("-", 1)[-1].strip()
    os.rename(folder, name_new)

###################

for root, dirs, files in os.walk("."):
    #    for name in files:
    #       print(os.path.join(root, name))
    for name_dir in dirs:
        dir = os.path.join(root, name_dir)
        if dir.endswith(tuple(["\\1", "\\2", "\\3"])):
            print(dir)
            for root2, folder, sub_files in os.walk(dir):
                for f in sub_files:
                    # print('\t' + f)

                    track_new = dir[-1].zfill(2) + "-" + f
                    print("\t" + track_new)

                    new_path = os.path.join(dir, track_new)

                    os.rename(os.path.join(dir, f), new_path)

                    dest_path = os.path.join(dir)[:-2]
                    # print(dest_path)
                    shutil.move(new_path, dest_path)
            # print(dir)
            shutil.rmtree(dir)
