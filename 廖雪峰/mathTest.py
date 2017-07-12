#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 12:42:11
# @Author  : kris_jiang (kris_jiang@compal.com)
# @Version : $Id$


import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return x1, x2


n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

print(quadratic(2, 3, 1))  # => (-0.5, -1.0)
print(quadratic(1, 3, -4))  # => (1.0, -4.0)
