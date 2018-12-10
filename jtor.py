from pykakasi import kakasi


# ひらがなをローマ字に変換する
# FJPR変換に使えれば十分なのでいらない音は消す

# 1文字の音
# 「を」：「ウェイ」ではなく「エイ」、ただし他の音とは独立して変換
# 「ゔ」：「ヴェイ」ではなく「ベイ」
# 「ん」は区切っておかないとナ行と間違われる
# 「ー」、「っ」はいずれ消えるのでここで消してしまう
d = {
    "あ": "a",  "い": "i",   "う": "u",   "え": "e",  "お": "o",
    "ぁ": "a",  "ぃ": "i",   "ぅ": "u",   "ぇ": "e",  "ぉ": "o",
    "か": "ka", "き": "ki",  "く": "ku",  "け": "ke", "こ": "ko",
    "さ": "sa", "し": "si",  "す": "su",  "せ": "se", "そ": "so",
    "た": "ta", "ち": "ti",  "つ": "tu",  "て": "te", "と": "to",
    "な": "na", "に": "ni",  "ぬ": "nu",  "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi",  "ふ": "hu",  "へ": "he", "ほ": "ho",
    "ま": "ma", "み": "mi",  "む": "mu",  "め": "me", "も": "mo",
    "や": "ya",              "ゆ": "yu",              "よ": "yo",
    "ゃ": "ya",              "ゅ": "yu",              "ょ": "yo",
    "ら": "ra", "り": "ri",  "る": "ru",  "れ": "re", "ろ": "ro",
    "わ": "wa", "を": "'o'", "ん": "'n'", "ー": None, "っ": None,
    "が": "ga", "ぎ": "gi",  "ぐ": "gu",  "げ": "ge", "ご": "go",
    "ざ": "za", "じ": "zi",  "ず": "zu",  "ぜ": "ze", "ぞ": "zo",
    "だ": "da", "ぢ": "di",  "づ": "du",  "で": "de", "ど": "do",
    "ば": "ba", "び": "bi",  "ぶ": "bu",  "べ": "be", "ぼ": "bo",
    "ぱ": "pa", "ぴ": "pi",  "ぷ": "pu",  "ぺ": "pe", "ぽ": "po",
    "ゔ": "bu"
}

# 2文字の音
d2 = {
    # 特有の音
    "いぇ": "ye", "うぃ": "wi", "うぇ": "we", "うぉ": "wo",
    "じゃ": "ja", "じゅ": "ju", "じぇ": "je", "じょ": "jo",
    # FJPR変換で消える音は1文字音相当へ変換
    "きゃ": "ka", "きゅ": "ku", "きぇ": "ke", "きょ": "ko",
    "しゃ": "sa", "しゅ": "su", "しぇ": "se", "しょ": "so",
    "ちゃ": "ta", "ちゅ": "tu", "ちぇ": "te", "ちょ": "to",
    "にゃ": "na", "にゅ": "nu", "にぇ": "ne", "にょ": "no",
    "ひゃ": "ha", "ひゅ": "hu", "ひょ": "ho",
    "みゃ": "ma", "みゅ": "mu", "みぇ": "me", "みょ": "mo",
    "りゃ": "ra", "りゅ": "ru", "りぇ": "re", "りょ": "ro",
    "ぎゃ": "ga", "ぎゅ": "gu", "ぎぇ": "ge", "ぎょ": "go",
    "びゃ": "ba", "びゅ": "bu", "びょ": "bo",
    "ぴゃ": "pa", "ぴゅ": "pu", "ぴょ": "po",
    "ふぁ": "ha", "ふぃ": "hi", "ふぇ": "he",
    "ゔぁ": "ba", "ゔぃ": "bi", "ゔぇ": "be", "ゔぉ": "bo",
    "てぃ": "ti", "でぃ": "di", "でゅ": "du", "とぅ": "tu",
}


def conv_to_roman(text):
    s = conv_to_hiragana(text)
    ls = split_into_list(s)
    return hiragana_list_to_roman(ls)


def conv_to_hiragana(s):
    global kakasiObj
    kakasiObj = kakasi()  # Get kakasi instance

    # 形態素解析した上でひらがなに変換
    kakasiObj.setMode("H", "H")  # Hiragana to hiragana
    kakasiObj.setMode("K", "H")  # Katakana to hiragana
    kakasiObj.setMode("J", "H")  # Japanese(kanji) to hiragana
    conv = kakasiObj.getConverter()
    return conv.do(s)


def split_into_list(s):
    # 文字列を変換できる部分とできない部分に切り分ける
    # 後で役に立つ
    convertible = s[0] in d
    last_changed = 0
    ls = []
    for i, v in enumerate(s):
        tmp = v in d
        if tmp != convertible:
            ls.append([s[last_changed:i], convertible])
            last_changed = i
            convertible = tmp
    ls.append([s[last_changed:], convertible])
    return ls


def hiragana_list_to_roman(ls):
    ret = []
    for item in ls:
        s = item[0]
        if item[1]:
            s = hiragana_to_roman(item[0])
        ret.append([s, item[1]])
    return ret


def hiragana_to_roman(s):
    # 2文字の音を先に変換する
    for k, v in d2.items():
        s = s.replace(k, v)

    s = s.translate(str.maketrans(d))
    return s
