import glob
import os

from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader

dir = "/Users/kahnwong/Downloads/SATW/401-500/converted"
dest_dir = "/Users/kahnwong/Downloads/SATW"

"""List all files"""
os.chdir(dir)
pdfs = sorted(glob.glob("*.pdf"))

# for i in pdfs:
#     print(i)

"""Merge"""
merger = PdfFileMerger()

filename = "SATW 401-500"

for pdf in pdfs:
    merger.append(PdfFileReader(os.path.join(pdf), "rb"))
merger.write(os.path.join(dest_dir + "/" + filename + ".pdf"))
