import re


def conv_to_kana(s):
    # 辞書
    d = {
        "kei": "ケイ",
        "sei": "セイ",
        "tei": "テイ",
        "nei": "ネイ",
        "hei": "ヘイ",
        "mei": "メイ",
        "yei": "イェイ",
        "rei": "レイ",
        "wei": "ウェイ",
        "gei": "ゲイ",
        "zei": "ゼイ",
        "dei": "デイ",
        "jei": "ジェイ",
        "vei": "ヴェイ",
        "bei": "ベイ",
        "pei": "ペイ",
        "fei": "フェイ",
    }

    # 辞書を参照して変換
    for k, v in d.items():
        s = re.sub(k, v, s)

    # ei, e, nは最後に変換
    s = re.sub("ei", "エイ", s)
    s = re.sub("e", "エ", s)
    s = re.sub("n", "ン", s)

    # 母音 + n の区切り文字 ' を削除
    s = re.sub("'", "", s)

    return s
