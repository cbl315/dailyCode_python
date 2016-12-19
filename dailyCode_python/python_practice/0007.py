#!/usr/bin/env python
# 第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
# coding:utf-8
import os
from os.path import join
import codecs


def count_code_line(single_program_path):
    f = codecs.open(single_program_path, 'r', 'utf-8')
    empty_line = 0
    code_line = 0
    comment_line = 0
    isComment = False
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0:
            empty_line += 1
            continue
        elif line.startswith('#') or isComment:
            comment_line += 1
        elif line.startswith('\'\'\'') or line.endswith('\'\'\''):
            isComment = not isComment
        else:
            code_line += 1
    # print(code_line, comment_line, empty_line)
    return (code_line, comment_line, empty_line)


def main(program_path):
    if not os.path.exists(program_path):
        return 'No such path!'
    result = {'code_line': 0, 'comment_line': 0, 'empty_line': 0}
    for root, dirs, files in os.walk(program_path):
        for file_name in files:
            if file_name.endswith('.py'):
                single_program_path = join(root, file_name)
                (a, b, c) = count_code_line(single_program_path)
                result['code_line'] += a
                result['comment_line'] += b
                result['empty_line'] += c
    return result

if __name__ == '__main__':
    path = 'G:\code\python\dailyCode'
    result = main(path)
    print('codeLine:%d, commentLine:%d, emptyLine:%d'
          % ((result['code_line']), result['comment_line'],
              result['empty_line']))
