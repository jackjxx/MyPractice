#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 12:59:06
# @Author  : kris_jiang (kris_jiang@compal.com)
# @Version : $Id$


def power1(x, n):  # x n位置参数
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


# print power(3, 3)


def power2(x, n=2):  # n默认参数
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


def enroll(name, gender, age=6, city='Beijing'):  # age city 默认参数
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


def add_end(L=None):  # 
    if L is None:
        L = []
    L.append('END')
    return L