import re


def conv_to_fjpr(s):
    #print("RTOF 原文 " + s)
    vowels = "[aiueo]"  # 母音
    cons = "[kstnhmyrwgzdbpvjf]"  # 子音
    unit = f"{cons}?ei"  # 変換後のひとまとまり (ei または 子音 + ei)

    # 子音+母音 を 子音 + "ei" に変換
    # (ただし母音が連続する場合は変換しない)
    # s = re.sub(f"({cons}){vowels}({cons})", "\\1ei\\2", s)
    s = re.sub(f"({cons}){vowels}", "\\1ei", s)
    s = re.sub(f"({cons}){vowels}$", "\\1ei", s)
    #print("RTOF 子音+母音変換 " + s)

    # 母音の連続を"ei"に変換
    ptrn = f"(?:{unit})|(?:{vowels}{vowels})"
    s = re.sub(f"({ptrn}){vowels}{vowels}", "\\1ei", s)
    s = re.sub(f"^{vowels}{vowels}", "ei", s)
    #print("RTOF 母音連続変換 " + s)

    # 孤立した母音を"ei"に変換
    ptrn = f"(?:{unit})|n|'"
    s = re.sub(f"({ptrn}){vowels}({ptrn})", "\\1ei\\2", s)
    s = re.sub(f"({ptrn}){vowels}$", "\\1ei", s)
    s = re.sub(f"^{vowels}({ptrn})", "ei\\1", s)
    #print("RTOF 孤立母音変換 " + s)

    return s
