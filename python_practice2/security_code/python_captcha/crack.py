#! usr/bin/env python
# -*- coding:utf-8-*-
from PIL import Image
import time
import hashlib
import math
import os


class VectorCompare:
    def magnitude(self, concordance):
        total = 0
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    def relation(self, concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


def build_vector(pic):
    dic1 = {}
    count = 0
    for i in pic.getdata():
        dic1[count] = i
        count += 1
    return dic1

v = VectorCompare()

iconset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

image_set = []

for letter in iconset:
    for img in os.listdir('./iconset/%s/'%(letter)):
        temp = []
        if img != "Thumbs.db" and img != ".DS_Store":  # windows check...
            temp.append(build_vector(Image.open("./iconset/%s/%s"%(letter,img))))
        image_set.append({letter:temp})

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
count = 0
for letter in letters:
    m = hashlib.md5()
    print(letter, pic2.size[1])
    pic3 = pic2.crop((letter[0], 0, letter[1], pic2.size[1]))
    # pic3.save('{0}.gif'.format(count))
    guess = []
    for pic in image_set:
        for x, y in pic.items():
            if len(y) != 0:
                guess.append( (v.relation(y[0], build_vector(pic3)), x) )
    guess.sort(reverse=False)
    print("", guess[0])
    count += 1

# 打印颜色直方图
# print(pic.histogram())
