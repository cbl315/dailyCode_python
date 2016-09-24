#!/usr/bin/env python
# 第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，
# 为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# coding:utf-8
import re
import glob
from collections import Counter


def get_word_num(txt_path):
    path = '%s/*.txt' % txt_path
    # 忽视的词的标准不好判断
    stop_word = (['the', 'in', 'of', 'and', 'to', 'has', 'that', 'this', 's',
                 'is', 'are', 'a', 'with', 'as', 'an', 'i', 'his', 'it', 'he',
                  'she', 'you', 'for', 'was', 'have', 'from', 'had', 'my',
                  'at', 'upon', 'but', 'which', 'not', 'be', 'by', 'their',
                  'him', 'sir', 'there', 'who', 'they', 'said', 'on',
                  'so', 'them', 'all', 'we', 'were'])
    for files in glob.glob(path):
        f = open(files, 'r')
        content = f.read().lower()
        pattern = '[a-z0-9\']+'
        words = re.findall(pattern, content)
        wordList = Counter(words)
        for i in stop_word:
            if i in wordList:
                wordList[i] = 0
        f.close()
        # print(wordList.most_common())
        return wordList.most_common()[0]


if __name__ == '__main__':
    txt_path = 'G:\code\python\dailyCode\\0006'
    result = get_word_num(txt_path)
    print(result)
