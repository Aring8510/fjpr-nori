import re


def conv_to_kana(ls):
    ret = []
    for item in ls:
        s = item[0]
        if item[1]:
            s = fjpr_to_katakana(item[0])
        ret.append(s)
    return ''.join(ret)


def fjpr_to_katakana(s):
    d2 = {
        "chei": "チェイ",
    }
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

    # 辞書を参照して変換(長い音)
    for k, v in d2.items():
        s = re.sub(k, v, s)

    # 辞書を参照して変換(普通の音)
    for k, v in d.items():
        s = re.sub(k, v, s)

    # ei, e, nは最後に変換
    s = re.sub("ei", "エイ", s)

    s = re.sub("n", "ン", s)

    # 残された謎の母音はエイになってもらう
    for v in ['a', 'i', 'u', 'e', 'o']:
        s = re.sub(v, "エイ", s)

    # 母音 + n の区切り文字 ' を削除
    s = re.sub("'", "", s)

    return s
