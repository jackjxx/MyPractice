#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-13 16:19:31
# @Author  : kris_jiang (kris_jiang@compal.com)
# @Version : $Id$

'''
函数名 就是 指向函数的变量
'''
from functools import reduce


# map()函数接收两个参数，一个是函数，一个是Iterable,将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print (list(r))

# ====>['1', '2', '3', '4', '5', '6', '7', '8', '9']
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3)x4)


def add(x, y):  # 可以用sum()
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))  # ====>25


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))  # ===>13579

# ==================


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

# lambda简化


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

    CHAR_TO_FLOAT = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '.': -1
    }


def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)
