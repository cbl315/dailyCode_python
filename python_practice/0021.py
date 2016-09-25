#!/usr/bin/env python
# 第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？
# 请使用 Python 对密码加密。
import os
import binascii
from hashlib import sha256
from hmac import HMAC


def encrypt_pwd(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        # hexlify函数返回 二进制bytes类型数据的十六进制bytes类型，
        # 两位十六进制表示一个字节，所以长度是原来数据的两倍
        salt = os.urandom(8)  # 64 bits.

    assert 8 == len(salt)
    assert isinstance(salt, bytes)

    if isinstance(password, str):
        password = password.encode('UTF-8')
    result = password
    # 这里先随机生成 64 bits 的 salt，再选择 SHA-256 算法使用 HMAC 对密码和 salt 进行 10 次叠代混淆
    # 最后将 salt 和 hash 结果一起返回。
    for i in range(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result


def validate_password(hashed, input_password):
    return hashed == encrypt_pwd(input_password, salt=hashed[:8])


if __name__ == '__main__':
    saved_pwd = '123456'
    input_pwd = input('password:')
    hashed = encrypt_pwd(saved_pwd)
    if validate_password(hashed, saved_pwd):
        print('密码正确')
    else:
        print('密码错误')
