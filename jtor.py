from pykakasi import kakasi
import re

def conv_to_roman(text):
    global kakasi
    kakasi = kakasi()  # Generate kakasi instance
    kakasi.setMode("J", "H")  # Japanese(kanji) to ascii
    conv = kakasi.getConverter()
    text = conv.do(text)

    text = re.sub(r'[っッー]+',"",text)

    kakasi.setMode("H", "a")  # Hiragana to ascii
    kakasi.setMode("K", "a")  # Katakana to ascii

    kakasi.setMode("r", "Hepburn")  # Use Hepburn romanization

    conv = kakasi.getConverter()
    text = conv.do(text)
    return text
if __name__ == '__main__':
    print(conv_to_roman("楽器"))
