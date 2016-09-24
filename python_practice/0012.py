#!/usr/bin/env python
#  敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，
#  则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
import re


def main(txt_path):
    f = open(txt_path, 'r')
    filtered_words = set()
    text = f.readlines()
    f.close()
    for line in text:
        filtered_words.add(line)
    a = ''
    while(a != '~'):
        a = input('input your words(\'~\'退出):')
        for i in filtered_words:
            sensitive = False
            i = i.strip()
            b = re.split('%s' % i, a)
            if len(b) > 1:
                c = i
                sensitive = True
            else:
                continue
            if sensitive:
                b = re.split(r'%s' % (c.strip()), a)
                a = ('%s' % (len(i) * '*')).join(b)
            else:
                print(a)
        print(a)


if __name__ == '__main__':
    main('filtered_words.txt')
