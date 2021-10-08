# adapted from https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python, dhobbs
import argparse
import os

parser = argparse.ArgumentParser(
    description="Type dir path that you want to list files."
)
parser.add_argument("startpath")
parser.add_argument("filename")
args = parser.parse_args()


startpath = args.startpath
filename = args.filename

text = ""
for root, dirs, files in os.walk(startpath):
    files = [f for f in files if not f[0] == "."]
    dirs[:] = [d for d in dirs if not d[0] == "."]

    level = root.replace(startpath, "").count(os.sep)
    indent = "│   " * (level) + "├── "
    text += "{}{}".format(indent, os.path.basename(root)) + "\n"
    subindent = "│   " * (level + 1) + "├── "
    for f in files:
        text += "{}{}".format(subindent, f) + "\n"


with open(filename + ".txt", "wb") as f:
    f.write(text.encode("UTF-8"))
