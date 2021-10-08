import os

dest_dir = r"c:\Users\kahnw\Downloads\zzzz-tagging\comics\Crossed (2008)"

folders = list(range(1, 3 + 1))
prefix = "Crossed-+100 v"
# ~ dash = ' -'
dash = ""


for folder in folders:
    os.mkdir(dest_dir + "/" + prefix + str(folder) + dash)
