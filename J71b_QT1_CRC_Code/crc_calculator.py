#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 09:53:57
# @Author  : kris_jiang (kris_jiang@compal.com)
'''
计算 CRC Code, crc初始值是0xFFFF,从0x40开始
轮个计算CRC Code值放入crc，当前寄存器值放入byte,
除0x7B,0X7C

输入: RegistersValue

输出：PASS or FAIL
'''

from calHandler import Calculator
import re

poly_ccitt = 0x1021
dic = {}


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


def str2int(strValue):
    return int(strValue, base=16)


def catchvaule(regValuekey):
    name_register_list = re.findall(r"(\w+)(?= =)", regValuekey)
    value_register_list = re.findall(r"(?<== )(\w+)", regValuekey)
    return dict(zip(name_register_list, value_register_list))


class crc(Calculator):
    def method(self, x):
        dic = catchvaule(x)  # 返回无序的字典
        # diclist = sorted(dic.iteritems(), key=lambda d: d[0], reverse=False)
        # # 排序字典，返回[{键，值}]列表
        if hex(str2int(dic['0x7B'])) == 0x00 or hex(str2int(dic['0x7B'])) == 0xff or hex(str2int(dic['0x7C'])) == 0x00 or hex(str2int(dic['0x7C'])) == 0xff:
            return 'PASS'
        else:
            re_name_register_list = ['0x40', '0x41', '0x42', '0x43', '0x44',
                                     '0x45', '0x46', '0x47', '0x48', '0x49',
                                     '0x4A', '0x4B', '0x4C', '0x4D', '0x4E',
                                     '0x4F', '0x50', '0x51', '0x52', '0x53',
                                     '0x54', '0x55', '0x56', '0x57', '0x58',
                                     '0x59', '0x5A', '0x5B', '0x5C', '0x5D',
                                     '0x5E', '0x5F', '0x60', '0x61', '0x62',
                                     '0x63', '0x64', '0x65', '0x66', '0x67',
                                     '0x68', '0x69', '0x6A', '0x6B', '0x6C',
                                     '0x6D', '0x6E', '0x6F', '0x70', '0x71',
                                     '0x72', '0x73', '0x74', '0x75', '0x76',
                                     '0x77', '0x78', '0x79', '0x7A', '0x7D',
                                     '0x7E', '0x7F']
            CRC = 65535
            for i in re_name_register_list:
                current_register_value = str2int(dic[i])
                CRC = ccitt_alps(CRC, current_register_value)

            CRC_highbyte = (CRC & 0xff00) >> 8
            CRC_lowbyte = CRC & 0xff
            if str2int(dic['0x7B']) == CRC_highbyte and str2int(dic['0x7C']) == CRC_lowbyte:
                return 'PASS'
            else:
                return 'FAIL'


if __name__ == '__main__':
    crc().doCalculate()
