#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-11 13:46:27
# @Author  : kris_jiang (kris_jiang@compal.com)
# @Version : $Id$

# 列表生成式
# L = []
# for x in xrange(1,11):
#     L.append(x * x)


[x * x for x in range(1, 11)]  # 生成的元素x * x
[m + n for m in 'ABC' for n in 'XYZ']  # 全排列
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
import os
[d for d in os.listdir('.')]  # 列出文件和目录