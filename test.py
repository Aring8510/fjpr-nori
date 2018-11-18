#!/usr/bin/env python3
import unittest
import jtor
import rtof
import ftok


test_strs = [
    ("いいね", "iine",  "einei",  "エイネイ"),
    ("ダメ",   "dame",  "deimei", "デイメイ"),
    ("酒",     "sake",  "seikei", "セイケイ"),
    ("うんち", "u'n'ti", "ei'n'tei", "エインテイ"),
    ("ほげ", "hoge", "heigei", "ヘイゲイ"),
    ("どう", "dou", "deiei", "デイエイ"),
    ("シャツ", "satu", "seitei", "セイテイ"),
    ("ウーパールーパー", "uparupa", "eipeireipei", "エイペイレイペイ"),
    ("鼻血", "hanadi", "heineidei", "ヘイネイデイ"),
    ("フレロビウム", "hurerobiumu", "heireireibeieimei", "ヘイレイレイベイエイメイ"),
    ("ジェイソン", "jeiso'n'", "jeieisei'n'", "ジェイエイセイン"),
    ("コンピュータ", "ko'n'puta", "kei'n'peitei", "ケインペイテイ"),
    ("業務", "goumu", "geieimei", "ゲイエイメイ"),
    ("般若", "ha'n'na", "hei'n'nei", "ヘインネイ"),
    ("さっき", "saki", "seikei", "セイケイ"),
    ("アイアイ", "aiai", "eiei", "エイエイ"),
    ("本案", "ho'n'a'n'", "hei'n'ei'n'", "ヘインエイン"),
    ("ウィキペディア", "wikipedia", "weikeipeideiei", "ウェイケイペイデイエイ"),
    ("ヴァーチャル", "vataru", "veiteirei", "veiteirei"),
]


class FJPRTest(unittest.TestCase):
    def test_jtor(self):
        for t in test_strs:
            with self.subTest(src=t[0], dst=t[1]):
                self.assertMultiLineEqual(jtor.conv_to_roman(t[0]), t[1])

    def test_rtof(self):
        for t in test_strs:
            with self.subTest(src=t[1], dst=t[2]):
                self.assertMultiLineEqual(rtof.conv_to_fjpr(t[1]), t[2])

    def test_ftok(self):
        for t in test_strs:
            with self.subTest(src=t[2], dst=t[3]):
                self.assertMultiLineEqual(ftok.conv_to_kana(t[2]), t[3])


if __name__ == '__main__':
    unittest.main(verbosity=2)
