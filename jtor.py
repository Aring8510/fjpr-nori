from pykakasi import kakasi

def conv_to_roman(text):
    global kakasi
    kakasi = kakasi()  # Generate kakasi instance

    kakasi.setMode("H", "a")  # Hiragana to ascii
    kakasi.setMode("K", "a")  # Katakana to ascii
    kakasi.setMode("J", "a")  # Japanese(kanji) to ascii

    kakasi.setMode("r", "Hepburn")  # Use Hepburn romanization

    conv = kakasi.getConverter()
    result = conv.do(text)
    return result
if __name__ == '__main__':
    print(conv_to_roman("これはひらがなコレハカタカナ漢字"))
