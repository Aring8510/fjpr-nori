from pykakasi import kakasi


def conv_to_roman(text):
    global kakasiObj
    kakasiObj = kakasi()  # Generate kakasi instance

    kakasiObj.setMode("H", "a")  # Hiragana to ascii
    kakasiObj.setMode("K", "a")  # Katakana to ascii
    kakasiObj.setMode("J", "a")  # Japanese(kanji) to ascii

    kakasiObj.setMode("r", "Hepburn")  # Use Hepburn romanization

    conv = kakasiObj.getConverter()
    result = conv.do(text)
    return result
