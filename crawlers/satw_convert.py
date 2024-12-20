import glob, os
import img2pdf
import pypandoc
#~ from wkhtmltopdf import wkhtmltopdf



"""Convert image to pdf"""

os.chdir("/Users/kahnwong/Downloads/SATW/401-500/HTML")

# jpgs = glob.glob('*.jpg')
# pngs = glob.glob('*.png')
#
# def jpg2pdf(filename, extension):
#     with open(filename + ".pdf","wb") as f:
#         f.write(img2pdf.convert(filename + extension))
#
#
# for jpg in jpgs:
#     filename = jpg[:-4]
#     jpg2pdf(filename, '.jpg')
#     print('Convert', filename, 'complete!')
#
# for png in pngs:
#     filename = png[:-4]
#     jpg2pdf(filename, '.png')
#     print('Convert', filename, 'complete!')


"""Convert html to pdf"""

htmls = sorted(glob.glob('*.html'))

#~ # pandoc
for html in htmls[62:70]: # start 61 - 70
    hFileName = html[:-5]
    pypandoc.convert_file(html, 'pdf', outputfile=hFileName + ".pdf",
        extra_args = ['-V', 'geometry:paperwidth=210mm', '-V', 'geometry:paperheight=297mm', '-V', 'geometry:margin=.5cm'])
    print('Convert', html, 'complete!')
