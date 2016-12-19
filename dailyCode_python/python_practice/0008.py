#!/usr/bin/env python
# 一个HTML文件，找出里面的正文。
import re
import codecs


def cmpSize(list1, list2):
    s1 = s2 = ''
    for i in list1:
        s1 += i
    for i in list2:
        s2 += i
    return list1 if len(s1) > len(s2) else list2


def getContentOfHtml(html):
    f = codecs.open(html, 'r', encoding="UTF-8")
    text = f.read()
    f.close()
    divs = re.findall(r'<div[^/]+>[\s\S]+?</div>', text)
    result = []
    for single_div in divs:
        tmp = re.findall(r'>[^<]+?<', single_div)
        result = cmpSize(tmp, result)
    for index in range(len(result)):
        result[index] = result[index][1:len(result[index]) - 1].strip()
    return result


if __name__ == "__main__":
    result = getContentOfHtml('0008.html')
    f = open('正文.txt', 'w')
    for i in result:
        if i != '':
            f.write('%s\n' % i)
    f.close()
    print(result)
