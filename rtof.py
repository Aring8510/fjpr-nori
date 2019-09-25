import re


def conv_to_fjpr(ls):
    ret = []
    for item in ls:
        s = item[0]
        if item[1]:
            s = roman_to_fjpr(item[0])
        ret.append([s, item[1]])
    return ret


def roman_to_fjpr(s):
    #print("RTOF 原文 " + s)
    vowels = "[aiueo]"  # 母音
    cons = "[kstnhmyrwgzdbpvjf]"  # 子音
    unit = f"{cons}?ei"  # 変換後のひとまとまり (ei または 子音 + ei)

    # 冪等性を確保するため 子音+ei は 子音+e にする
    s = re.sub(f"({cons}?)ei", "\\1e", s)
    #print("RTOF ユニット削除 " + s)

    # 子音+母音 を 子音 + "ei" に変換
    # (ただし母音が連続する場合は変換しない)
    # s = re.sub(f"({cons}){vowels}({cons})", "\\1ei\\2", s)
    s = re.sub(f"({cons}){vowels}", "\\1ei", s)
    #print("RTOF 子音+母音変換 " + s)

    # 母音の連続を"ei"に変換
    ptrn = f"(?:{unit})|(?:{vowels}{vowels})"
    s = re.sub(f"({ptrn}){vowels}{vowels}", "\\1ei", s)
    s = re.sub(f"^{vowels}{vowels}", "ei", s)
    #print("RTOF 母音連続変換 " + s)

    # 「を」を変換
    s = re.sub("'o'", "ei", s)

    # 孤立した母音を"ei"に変換
    ptrn = f"(?:{unit})|n|'"
    while True:
        s2 = re.sub(f"({ptrn}){vowels}({ptrn})", "\\1ei\\2", s)
        if s == s2:
            break
        s = s2
    s = re.sub(f"({ptrn}){vowels}$", "\\1ei", s)
    s = re.sub(f"^{vowels}({ptrn})", "ei\\1", s)
    #print("RTOF 孤立母音変換 " + s)

    return s
