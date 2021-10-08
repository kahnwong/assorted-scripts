import argparse
import os


parser = argparse.ArgumentParser(description="Type volume name.")
parser.add_argument("tpb_name")
args = parser.parse_args()

tpb_folder = args.tpb_name

"""dir by dir"""
root_path = r"D:\Downloads\z-TAGGING\# COMICS\#to be dated"

if tpb_folder.count(":") == 2:
    # ~ print('found two')
    tpb_folder = tpb_folder.replace(": ", "-", 1)

tpb_folder = tpb_folder.replace("Vol. ", "v").replace(": ", " - ")

print(tpb_folder)

os.mkdir(root_path + "/" + tpb_folder)
