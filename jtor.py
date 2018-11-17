from pykakasi import kakasi


def conv_to_roman(text):
    global kakasiObj
    kakasiObj = kakasi()  # Get kakasi instance

    # ひらがなとカタカナで変換結果が違うので一旦ひらがなにする
    kakasiObj.setMode("H", "H")  # Hiragana to ascii
    kakasiObj.setMode("K", "H")  # Katakana to ascii
    kakasiObj.setMode("J", "H")  # Japanese(kanji) to ascii
    convHiragana = kakasiObj.getConverter()
    resultHiragana = convHiragana.do(text)

    kakasiObj.setMode("H", "a")  # Hiragana to ascii
    kakasiObj.setMode("K", "a")  # Katakana to ascii
    kakasiObj.setMode("J", "a")  # Japanese(kanji) to ascii
    kakasiObj.setMode("r", "Hepburn")  # Use Hepburn romanization

    convRoman = kakasiObj.getConverter()
    result = convRoman.do(resultHiragana)
    return result
