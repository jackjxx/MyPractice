#!/usr/bin/env python
# -*- coding: utf-8 -*-
poly_ccitt = 0x1021


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


print ccitt_alps(0xFFFF, 0x54)
