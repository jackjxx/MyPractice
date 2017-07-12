#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 15:38:23
# @Author  : kris_jiang (kris_jiang@compal.com)
# @Version : $Id$'
'''
计算 n! = 1 x 2 x 3 x ... x n
fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
'''


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print fact(5)
'''
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
'''

# 函数调用通过栈实现，递归调用次数过多，会导致栈溢出
# 解决栈溢出的方法是 尾递归优化
# 尾递归是指 在函数返回的时候，调用自身本身，并且，return语句不能包含表达式


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)  # num - 1 num * product# 调用前就被计算


'''
===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120
'''


## 最尴尬的是：Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。


# Tower of Hanoi #


def move(n, a, b, c):
    if n == 1:
        print ('move', a, '--->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)







