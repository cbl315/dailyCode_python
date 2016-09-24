#!/usr/bin/env python
# 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
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
