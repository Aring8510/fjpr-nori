import re


def conv_to_kana(s):
    # 辞書
    d = {
        "kei": "ケイ",
        "sei": "セイ",
        "tei": "テイ",
        "nei": "ネイ",
        "hei": "へイ",
        "mei": "メイ",
        "yei": "イェイ",
        "rei": "レイ",
        "wei": "ウェイ",
        "gei": "ゲイ",
        "zei": "ゼイ",
        "dei": "デイ",
        "jei": "ジェイ",
        "vei": "ヴェイ",
    }

    # 辞書を参照して変換
    for k, v in d.items():
        s = re.sub(k, v, s)

    # ei, e, nは最後に変換
    s = re.sub("ei", "エイ", s)
    s = re.sub("e", "エ", s)
    s = re.sub("n", "ン", s)

    return s
