#!/usr/bin/env python3
import jtor
import rtof
import ftok

try:
    import readline
except ImportError:
    pass


# 日本語 -> FJPR
def norify(s, debug=False):
    s_debug = f"原文: {s}\n"
    s1 = jtor.conv_to_roman(s)
    s_debug += f"ローマ字: {s1}\n"
    s2 = rtof.conv_to_fjpr(s1)
    s_debug += f"FJPR: {s2}\n"
    s3 = ftok.conv_to_kana(s2)
    s_debug += f"カナ: {s3}"
    if debug:
        return s_debug
    else:
        return s3


if __name__ == '__main__':
    try:
        while True:
            s = input('> ')
            print(norify(s, debug=True))
    except (EOFError, KeyboardInterrupt):
        print("\nQuitting...")
