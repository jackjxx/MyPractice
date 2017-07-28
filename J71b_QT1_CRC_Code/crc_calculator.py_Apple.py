#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 09:53:57
# @Author  : kris_jiang (kris_jiang@compal.com)
'''
计算 CRC Code, crc初始值是0xFFFF,从0x40开始
轮个计算CRC Code值放入crc，当前寄存器值放入byte

输入
'''

from calHandler import Calculator


poly_ccitt = 0x1021


class crc_calculator(Calculator):
    def ccitt_alps(crc, byte):
        cc = (crc ^ (byte << 8))
        # print "CRC ^ Byte = {0:#x}".format(cc)
        for i in range(8):
            if cc & 0x8000:
                cc = (cc << 1) ^ poly_ccitt
                # print "(cc << 1) ^ poly = {0:#x}".format(cc)
            else:
                12
                cc <<= 1
                # print "(cc << 1) = {0:#x}".format(cc)
        cc &= 0xFFFF
        return cc

    def dec2hex(decValue):
        return hex(int(decValue))

    def method(self, x, y):
        pass


if __name__ == '__main__':
    crc_calculator().doCaculate()
