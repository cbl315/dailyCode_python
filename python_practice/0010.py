#!/usr/bin/env python
# 第 0010 题：使用 Python 生成字母验证码图片
import string
import random
from PIL import Image, ImageDraw, ImageFont


def main():
    # Generate random letters
    letters = ''.join([random.choice(string.ascii_letters) for i in range(4)])

    # set image size
    height = 60
    width = height * 4

    # Generate a new image
    im = Image.new('RGB', (width, height), (255, 255, 255))

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('msyh.ttf', int(height * 0.75))
    for i in range(4):
        draw.text((int(width / 4 * i + 5), 5), letters[i], (random.randint(0, 255),
                  random.randint(0, 255), random.randint(0, 255)), font)
    del draw
    # Change the background color
    for x in range(width):
        for y in range(height):
            if im.getpixel((x, y)) == (255, 255, 255):
                im.putpixel((x, y), ((random.randint(0, 255),
                            random.randint(0, 255), random.randint(0, 255))))

    # save the image
    im.save('0010.png')


if __name__ == '__main__':
    main()
    print('success!')
