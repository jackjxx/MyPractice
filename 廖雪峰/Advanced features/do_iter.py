#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 16:19:10
# @Author  : kris_jiang (kris_jiang@compal.com)
# @Version : $Id$
'''
迭代器（Iterables）任何可以用 for in 来迭代读取的都是迭代容器，
例如lists,strings,files.这些迭代器非常的便利，因为你可以想取多少
便取多少，但是你得存储所有的值，其中很多值都完全没有必要每次都保持在内存中
>>> mylist = [x*x for x in range(3)]
>>> for i in mylist:
...    print(i)
0
1
4


生成器（Generators） 也是可迭代的，但是你每次只能迭代它们一次，因为不是所
有的迭代器都被一直存储在内存中的，他们临时产生这些值
生成器几乎和迭代器是相同的，除了符号[]变为()
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)
0
1
4
'''
from collections import Iterable, Iterator


def g():  # yield 返回的是生成器
    yield 1
    yield 2
    yield 3


print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
