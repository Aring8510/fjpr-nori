import unittest
import jtor
#import rtof
import ftok


class FJPRTest(unittest.TestCase):
    def test_jtor(self):
        d = {
            "いいね" : "iine",
            "ダメ"   : "dame",
            "酒"     : "sake"
        }
        for k, v in d.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(jtor.conv_to_roman(k), v)

    def test_rtof(self):
        pass

    def test_ftok(self):
        d = {
            "einei" : "エイネイ",
            "deimei": "デイメイ",
            "seikei": "セイケイ"
        }
        for k, v in d.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(ftok.conv_to_kana(k), v)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
