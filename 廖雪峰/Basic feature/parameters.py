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


def add_end(L=None):  # 防止再次调用时导致默认参数改变
    if L is None:
        L = []
    L.append('END')
    return L


def calc1(numbers):  # 未使用可变参数
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


# print ('sum1 = %d' % calc1([1, 2, 3]))


def calc2(*numbers):  # 使用可变参数,numbers 接受的是一个tuple
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


# print ('sum2 = %d' % calc2(1, 2, 3))


def person1(name, age, **kw):  # name age 必选参数，kw关键字参数；关键字参数扩展函数更多功能
    print('name:', name, 'age:', age, 'other:', kw)  # kw接受的是一个dict


def person2(name, age, *, city, job):  # *后面的参数被视为命名关键字参数
    print(name, age, city, job)



