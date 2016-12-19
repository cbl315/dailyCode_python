#!/usr/bin/env python
# 第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
# link:http://tieba.baidu.com/p/2166231880
import urllib.request
import re
import os


def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    # 返回的文件是'byte'类型的
    return html


def get_img(html):
    reg = r'src="(http://imgsrc.baidu.com/forum/.*?)"'
    imgre = re.compile(reg)
    html = html.decode('utf-8')
    img_list = re.findall(imgre, html)
    print(len(img_list))
    result_path = 'img'
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    for index in range(len(img_list)):
        (urllib.request.urlretrieve(img_list[index],
                                    r'%s\%s.jpg' % (result_path, index)))


if __name__ == '__main__':
    html = get_html(r'http://tieba.baidu.com/p/2166231880')
    get_img(html)
    print('success!')
