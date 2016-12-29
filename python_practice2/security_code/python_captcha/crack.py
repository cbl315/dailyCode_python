#! usr/bin/env python
# -*- coding:utf-8-*-
from PIL import Image


pic = Image.open('captcha.gif')
# (将图片转换为8位像素模式)
pic.convert('P')
pic2 = Image.new('P', pic.size, 255)
for x in range(pic.size[1]):
    for y in range(pic.size[0]):
        pixel = pic.getpixel((y, x))
        if pixel == 220 or pixel == 227:
            pic2.putpixel((y, x), pixel)
# pic2.show()
inletter = False
foundletter = False
letters = []
for x in range(pic2.size[0]):
    for y in range(pic2.size[1]):
        if pic2.getpixel((x, y)) != 255:
            inletter = True
    if inletter and not foundletter:
        foundletter = True
        start = x

    if foundletter and not inletter:
        foundletter = False
        end = x
        letters.append((start, end))
    inletter = False
print(letters)

# 打印颜色直方图
# print(pic.histogram())
