#!/usr/bin/env python3
import jtor
import rtof
import ftok

try:
    import readline
except ImportError:
    pass


# 日本語 -> FJPR
def norify(s):
    # print("原文 " + s)
    s1 = jtor.conv_to_roman(s)
    # print("ローマ字 " + s1)
    s2 = rtof.conv_to_fjpr(s1)
    # print("FJPR " + s2)
    s3 = ftok.conv_to_kana(s2)
    # print("カナ " + s3)
    return s3


if __name__ == '__main__':
    try:
        while True:
            s = input('> ')
            norify(s)
    except (EOFError, KeyboardInterrupt):
        print("\nQuitting...")
