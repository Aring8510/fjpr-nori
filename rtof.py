import re


def conv_to_fjpr(s):
    print("原文 " + s)
    vowels = "[aiueo]"  # 母音
    cons = "[kstnhmyrwgzdbpvjf]"  # 子音

    s = re.sub("-", "", s)   # 長音を消す
    s = re.sub("jie", "je", s)  # jie を je に変える (pykakasiはジェをjieにしてしまう)
    s = re.sub("ch", "t", s)  # ch を t に変える (どちらもテイになる)
    s = re.sub("ts", "t", s)  # ts を t に変える (どちらもテイになる)
    s = re.sub("sh", "s", s)  # sh を s に変える (どちらもセイになる)
    s = re.sub("ji", "di", s)  # ji を di に変える (どちらもデイになる)
    s = re.sub("fu", "hu", s)  # fu を hu に変える (どちらもヘイになる)
    s = re.sub(f"({cons})y", "\\1", s)  # 子音 + y を子音に変える
    s = re.sub(f"([ksthmyrwgzdbpvjf])\\1", "\\1", s)  # n 以外の子音の連続(「っ」)を消す
    print("前処理 " + s)

    # 子音+母音 を 子音 + "ei" に変換
    # (ただし母音が連続する場合は変換しない)
    # s = re.sub(f"({cons}){vowels}({cons})", "\\1ei\\2", s)
    s = re.sub(f"({cons}){vowels}", "\\1ei", s)
    s = re.sub(f"({cons}){vowels}$", "\\1ei", s)
    print("子音+母音変換 " + s)

    # 母音の連続を"ei"に変換
    s = re.sub(f"({cons}){vowels}{vowels}", "\\1ei", s)
    s = re.sub(f"^{vowels}{vowels}", "ei", s)
    print("母音連続変換 " + s)

    # 孤立した母音を"ei"に変換
    ptrn = f"{cons}|(?:{vowels}{vowels})"
    s = re.sub(f"({ptrn}){vowels}({cons})", "\\1ei\\2", s)
    s = re.sub(f"({ptrn}){vowels}$", "\\1ei", s)
    s = re.sub(f"^{vowels}({cons})", "ei\\1", s)
    print("孤立母音変換 " + s)

    return s
