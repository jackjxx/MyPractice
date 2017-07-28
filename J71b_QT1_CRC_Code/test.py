#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 14:27:36
# @Author  : kris_jiang (kris_jiang@compal.com)
# @Version : $Id$

import re
dic = {}
RegistersVaule = '/Users/kris/Desktop/1.txt'
poly_ccitt = 0x1021


def str2int(decValue):
    return int(decValue, base=16)


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


txt = open(RegistersVaule)
content = txt.read()
name_register_list = re.findall(r"(\w+)(?= =)", content)
value_register_list = re.findall(r"(?<== )(\w+)", content)
# print value_register_list
dic = dict(zip(name_register_list, value_register_list))
# print dic
dict = sorted(dic.iteritems(), key=lambda d: d[0])
# print dict
# print hex(str2int(value_register_list[1]))
# print dict[0][1]
# print dict[59][1]
# print dict[60][1]
# print hex(64385)
# print name_register_list
# print dict['0x7C']
# print dict['0x7B']
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
    print 'pass'
