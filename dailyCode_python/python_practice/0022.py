#!/usr/bin/env python
# 第 0022 题： iPhone 6、iPhone 6 Plus 早已上市开卖。
# 请查看你写得 第 0005 题的代码是否可以复用。
# coding:utf-8
from PIL import Image
import glob
import os


def resizeToIphone6Size():
    size = (1334, 750)
    for files in glob.glob(r'*.jpg'):
        file_name = files.split('.')[0]
        im = Image.open(files)
        size = (size[1], size[0]) if im.size[1] > im.size[0] else size
        im.thumbnail(size, Image.ANTIALIAS)
        print(im.format, im.size, im.mode)
        result_name = '%s_resize.jpg' % file_name
        im.save(result_name)
    print('done!')


def resizeToIphone6pLusSize():
    size = (2208, 1242)
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
    resizeToIphone6Size()
