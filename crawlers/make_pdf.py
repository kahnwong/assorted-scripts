import os, glob
from PIL import Image
import numpy as np
import img2pdf

# https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python

# # 0 padding dirs
# chapters_rename = glob.glob('*/') # folders only
# for chapter in chapters_rename:
#     if len(chapter) < 5:
#         os.rename(chapter, chapter.zfill(5))

# main

chapters = sorted(glob.glob('*/')) # debug
# print(chapters)
# for chapter in chapters:
#     os.chdir(chapter)
#     images = sorted(glob.glob('*'))
#
#     imgs = [Image.open(i) for i in images]
#     # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
#     # min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
#     # imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
#
#     # # save that beautiful picture
#     # imgs_comb = PIL.Image.fromarray( imgs_comb)
#     # imgs_comb.save( 'Trifecta.jpg' )
#
#     # for a vertical stacking it is simple: use vstack
#     # imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
#     imgs_comb = np.vstack( imgs)
#     imgs_comb = Image.fromarray(imgs_comb)
#
#     os.chdir('..')
#     filename = chapter.strip('/').strip('\\') + '.jpg'
#     print(filename)
#     imgs_comb.save(filename)
#
#
#     # break

def to_pdf(filename, files):
    with open(filename,"wb") as f:
        f.write(img2pdf.convert(files))

comic_name = 'My Giant Nerd Boyfriend'
# start_chapter = 1
# start_chapter = str(start_chapter).zfill(5)
# end_chapter = 123
# end_chapter = str(end_chapter).zfill(5)
year = '2017'
filename_pdf = '{} {}, {}-{}.pdf'.format(comic_name, year, chapters[0].strip('/'), chapters[-1].strip('/'))

merged_images = sorted(glob.glob('*.jpg'))
print(merged_images)
to_pdf(filename_pdf, merged_images)
print('===== {} ====='.format(filename_pdf))
