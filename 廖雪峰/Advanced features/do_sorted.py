#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-19 15:32:52
# @Author  : kris_jiang (kris_jiang@compal.com)
# @Version : $Id$


from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
# reverse默认是false（升序排列）
