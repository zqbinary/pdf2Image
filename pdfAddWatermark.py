import os
import tempfile
from os import walk
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image

"""
本来想自己加水印的，但是加的水印特别，特别，特别发育不良的样子
脚本还没有调试好

"""
IN_PATH = 'pdf/'
OUT_PATH = 'pdf-out/'

WATERMARK_PATH = 'resource/watermark.png'


def execute():
    for (dir, dirs, filenames) in walk(IN_PATH):
        for filename in filenames:
            pdf_reader = PdfFileReader(IN_PATH + filename)
            pdf_writer = PdfFileWriter()
            for page in range(pdf_reader.getNumPages()):
                pageObj = pdf_reader.getPage(page)
                im = Image.open(WATERMARK_PATH)

                # pageObj.mergePage(im)
                pdf_writer.addPage(pageObj)
            if not os.path.exists(OUT_PATH):
                os.makedirs(OUT_PATH)
            with open(os.path.join(OUT_PATH, 'hi.pdf'), 'wb') as out:
                pdf_writer.write(out)


if __name__ == '__main__':
    execute()
