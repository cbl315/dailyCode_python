# coding:utf-8
from PIL import Image
import glob
import os


def resizeToIphoneSize():
    size = (1136, 640)
    for files in glob.glob(r'*.jpg'):
        file_name = files.split('.')[0]
        im = Image.open(files)
        size = (size[1], size[0]) if im.size[1] > im.size[0] else size
        im.thumbnail(size, Image.ANTIALIAS)
        print(im.format, im.size, im.mode)
        result_name = '%s_resize.jpg' % file_name
        im.save(result_name)
    print('done!')

if __name__ == '__main__':
    resizeToIphoneSize()
