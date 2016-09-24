#!/usr/bin/env python
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？
import uuid


def generatorCode(num=0):
    code_list = [str(uuid.uuid4()) for i in range(num)]
    return code_list

if __name__ == '__main__':
    result = generatorCode(200)
    f = open(r'200_generatorCode.txt', 'w')
    for i in result:
        f.write('%s\n' % i)
    f.close()
