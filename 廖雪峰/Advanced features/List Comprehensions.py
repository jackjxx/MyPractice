#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-11 13:46:27
# @Author  : kris_jiang (kris_jiang@compal.com)
# @Version : $Id$

# 列表生成式
# L = []
# for x in xrange(1,11):
#     L.append(x * x)


import os


[x * x for x in range(1, 11)]  # 生成的元素x * x

[x * x for x in range(1, 11) if x % 2 == 0]  # 筛选出仅有偶数的平方
[m + n for m in 'ABC' for n in 'XYZ']  # 全排列
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]


[d for d in os.listdir('.')]  # 列出文件和目录


d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)


