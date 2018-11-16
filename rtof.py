import re


def conv_to_fjpr(s):
    vowels = "[aiueo]"  # 母音
    cons = "[kstnhmyrwgzdb]"  # 子音
    s = re.sub("chi", "ti", s)  # chi を ti に変える

    # 子音+母音 を 子音 + "ei" に変換
    s = re.sub(f"({cons}){vowels}", "\\1ei", s)

    # 母音の連続を"ei"に変換
    vowel_seq = [
        "aa", "ai", "au", "ae", "ao",
        "ia", "ii", "iu", "ie", "io",
        "ua", "ui", "uu", "ue", "uo",
        "ea",       "eu", "ee", "eo",
        "oa", "oi", "ou", "oe", "oo"
    ]
    for p in vowel_seq:
        s = re.sub(p, "ei", s)

    # 孤立した母音を"ei"に変換
    s = re.sub(f"[^aiueo]{vowels}({cons})", "ei\\1", s)
    s = re.sub(f"^{vowels}({cons})", "ei\\1", s)

    return s
