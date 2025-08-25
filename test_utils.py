import unittest
from utils import intToRoman

class TestRomanNumeral(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(intToRoman(0), "")

    def test_one(self):
        self.assertEqual(intToRoman(1), "I")

    def test_three_nine_nine_nine(self):
        self.assertEqual(intToRoman(3999), "MMMCMXCIX")
    
if __name__ == '__main__':
    unittest.main()
