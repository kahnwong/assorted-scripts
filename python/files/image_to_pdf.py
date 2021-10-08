import glob
import os

source_dir = r"/Users/kahnwong/Nextcloud/z-treats/treats 5"
dest_dir = r"/Users/kahnwong/Nextcloud/"

os.chdir(source_dir)
images = glob.glob("*.jpg")
images = sorted(images)
filename = "Treats #5"

print(images)
#
# multiple inputs (variant 2)
# with open(filename + '.pdf',"wb") as f:
#     f.write(img2pdf.convert(images))
#
# print('Done')
