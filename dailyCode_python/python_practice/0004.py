#!/usr/bin/env python
# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
import re


def countWords(txt_path):
    f = open(txt_path, 'r')
    txt = f.read()
    result = re.findall(r'[\w\-\.\']', txt)
    f.close()
    return len(result)

if __name__ == "__main__":
    txt_path = "The White Company.txt"
    result = countWords(txt_path)
    print(result)
