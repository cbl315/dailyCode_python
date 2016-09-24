#!/usr/bin/env python
# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，
# 则打印出 Freedom，否则打印出 Human Rights。

'''
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
'''
import re


f = open('filtered_words.txt', r'r')
filtered_words = set()
text = f.readlines()
for line in text:
    filtered_words.add(line)
print(filtered_words)
a = input('input a word or a sentence:')
isOutput = False
for i in filtered_words:
    if a.find(i):
        print('Freedom !')
        isOutput = True
        break
if not isOutput:
    print('Human Rights !')
f.close()
