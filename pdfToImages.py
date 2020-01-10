# /usr/bin/python3

import os
import glob
from pdf2image import convert_from_path

# 1. 遍历 pdf_data,作为输入源头
# 2. 转换成 images
# 3. 把 images 放入 同名文件夹

WIDTH = 790
IN_PATH = 'pdf_data/'
OUT_PATH = 'pdf_out/'

def execute():
    types = ('*.pdf')
    for type in types:
        filename = os.path.join(IN_PATH, type)
        a = glob.glob(filename)
        # file list
        for path in a:
            name = path.replace(IN_PATH, '').replace('.pdf', '')
            outPut = path.replace(IN_PATH, OUT_PATH).replace('.pdf', '') + '/'
            if not os.path.exists(outPut):
                os.makedirs(outPut)
            else:
                continue

            # 这里需要置空 不然会报错
            images = []
            images = convert_from_path(path)
            index = 0
            for im in images:
                im = convert_to_jpg(im)
                im = thumb(im)
                nameNew = name + '_' + str(index).zfill(2) + '.jpg'
                index += 1
                im.save(outPut + nameNew, 'JPEG')

            print(name + ' is done!')
    print('all is ok!')


def convert_to_jpg(im):
    im = im.convert('RGB')
    return im


def thumb(im):
    width = im.size[0]
    height = im.size[1]
    radio = WIDTH / width
    im.thumbnail((WIDTH, height * radio))
    return im


if __name__ == '__main__':
    execute()
