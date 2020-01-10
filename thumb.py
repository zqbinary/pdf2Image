# /usr/bin/python3
import os
import glob
from PIL import Image
from os import walk

# 作用 把 data 下面的的 图片文件夹里的图片
# 1. png-》jpg
# 2. 剪切成 790宽，高按比例来

WIDTH = 790
IN_PATH = 'data/'
OUT_PATH = 'out/'


def execute():
    for (dir, dirs, fileNames) in walk(IN_PATH):
        for dirName in dirs:
            pathIn = IN_PATH + dirName + '/'
            pathOut = pathIn.replace(IN_PATH, OUT_PATH)
            if not os.path.exists(pathOut):
                os.makedirs(pathOut)
            types = ('*.png', '*.jpg')
            for type in types:
                filename = os.path.join(pathIn, type)
                a = glob.glob(filename)
                for path in a:
                    name = os.path.join(path)
                    im = Image.open(name)
                    im = convert_to_jpg(im)
                    im = thumb(im)
                    im.save(os.path.splitext(name.replace(IN_PATH, OUT_PATH))[0] + '.jpg', 'JPEG')
                    print(path, 'Done!')


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
