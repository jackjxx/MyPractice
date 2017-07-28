#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-19 15:13:14
# @Author  : kris_jiang (kris_jiang@compal.com)
# @Version : $Id$


def is_odd(n):
    return n % 2 == 1


L = range(100)

print(list(filter(is_odd, L)))  # 删掉偶数保留奇数


def not_empty(s):  # 把一个序列中的空字符串删掉
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
