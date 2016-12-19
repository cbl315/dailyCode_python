#!/usr/bin/env python
# 第 0009 题：一个HTML文件，找出里面的链接。
import re
import codecs


def getAttribute(xmlStr, attribute):
    try:
        # 得到start=attribute的 " 所在index的endIndex
        endIndex = (xmlStr.index('\"',
                    xmlStr.index('\"', xmlStr.index(attribute)) + 1))
        startIndex = xmlStr.index('\"', xmlStr.index(attribute)) + 1
        tmp = (xmlStr[startIndex:endIndex])
        return tmp
    except Exception as e:
        print(e)
        return ''


def main(html):
    f = codecs.open(html, 'r', encoding='utf-8')
    content = f.readlines()
    f.close()
    links = []
    result = []
    for line in content:
        if line.find('href') != -1:
            links.append(line)
    for i in links:
        result.append(getAttribute(i, 'href'))
    f = open('result.txt', 'w')
    for i in result:
        f.write(i + '\n')
    f.close()
    # print(result)


if __name__ == '__main__':
    main('0009.html')
    print('success!')
