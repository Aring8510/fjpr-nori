#!/usr/bin/env python3
import unittest
import jtor
import rtof
import ftok


test_strs = [
    ("いいね",           [["iine", True]],        [["einei", True]],             "エイネイ"),
    ("ダメ",             [["dame", True]],        [["deimei", True]],            "デイメイ"),
    ("酒",               [["sake", True]],        [["seikei", True]],            "セイケイ"),
    ("うんち",           [["u'n'ti", True]],      [["ei'n'tei", True]],          "エインテイ"),
    ("ほげ",             [["hoge", True]],        [["heigei", True]],            "ヘイゲイ"),
    ("どう",             [["dou", True]],         [["deiei", True]],             "デイエイ"),
    ("シャツ",           [["satu", True]],        [["seitei", True]],            "セイテイ"),
    ("ウーパールーパー", [["uparupa", True]],     [["eipeireipei", True]],       "エイペイレイペイ"),
    ("鼻血",             [["hanadi", True]],      [["heineidei", True]],         "ヘイネイデイ"),
    ("フレロビウム",     [["hurerobiumu", True]], [["heireireibeieimei", True]], "ヘイレイレイベイエイメイ"),
    ("ジェイソン",       [["jeiso'n'", True]],    [["jeieisei'n'", True]],       "ジェイエイセイン"),
    ("コンピュータ",     [["ko'n'puta", True]],   [["kei'n'peitei", True]],      "ケインペイテイ"),
    ("業務",             [["goumu", True]],       [["geieimei", True]],          "ゲイエイメイ"),
    ("般若",             [["ha'n'na", True]],     [["hei'n'nei", True]],         "ヘインネイ"),
    ("さっき",           [["saki", True]],        [["seikei", True]],            "セイケイ"),
    ("アイアイ",         [["aiai", True]],        [["eiei", True]],              "エイエイ"),
    ("本案",             [["ho'n'a'n'", True]],   [["hei'n'ei'n'", True]],       "ヘインエイン"),
    ("ウィキペディア",   [["wikipedia", True]],   [["weikeipeideiei", True]],    "ウェイケイペイデイエイ"),
    ("ヴァーチャル",     [["bataru", True]],      [["beiteirei", True]],         "ベイテイレイ"),
    ("空海さ",           [["kuukaisa", True]],    [["keieikeieisei", True]],     "ケイエイケイエイセイ"),
    ("んをい",           [["'n''o'i", True]],     [["'n'eiei", True]],           "ンエイエイ")
]


class FJPRTest(unittest.TestCase):
    def test_jtor(self):
        for t in test_strs:
            with self.subTest(src=t[0], dst=t[1]):
                self.assertEqual(jtor.conv_to_roman(t[0]), t[1])

    def test_rtof(self):
        for t in test_strs:
            with self.subTest(src=t[1], dst=t[2]):
                self.assertEqual(rtof.conv_to_fjpr(t[1]), t[2])

    def test_ftok(self):
        for t in test_strs:
            with self.subTest(src=t[2], dst=t[3]):
                self.assertEqual(ftok.conv_to_kana(t[2]), t[3])


if __name__ == '__main__':
    unittest.main(verbosity=2)
