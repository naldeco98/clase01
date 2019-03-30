import unittest
from decimal_roman import decimal_to_roman

class TestDecimalNumbers(unittest.TestCase):
    def test_decimal_1_to_roman(self):
        roman_number = decimal_to_roman (1)
        self.assertEqual(roman_number,'I')
    def test_decimal_2_to_roman(self):
        roman_number = decimal_to_roman (2)
        self.assertEqual(roman_number,'II')
    def test_decimal_3_to_roman(self):
        roman_number = decimal_to_roman (3)
        self.assertEqual(roman_number,'III')
    def test_decimal_4_to_roman(self):
        roman_number = decimal_to_roman (4)
        self.assertEqual(roman_number,'IV') 
    def test_decimal_5_to_roman(self):
        roman_number = decimal_to_roman (5)
        self.assertEqual(roman_number,'V')   
    def test_decimal_10_to_roman(self):
        roman_number = decimal_to_roman (10)
        self.assertEqual(roman_number,'X')
    def test_decimal_12_to_roman(self):
        roman_number = decimal_to_roman (12)
        self.assertEqual(roman_number,'XII')   
    def test_decimal_15_to_roman(self):
        roman_number = decimal_to_roman (15)
        self.assertEqual(roman_number,'XV') 
    def test_decimal_36_to_roman(self):
        roman_number = decimal_to_roman (36)
        self.assertEqual(roman_number,'XXXVI')
    def test_decimal_54_to_roman(self):
        roman_number = decimal_to_roman (54)
        self.assertEqual(roman_number,'LIV')
    def test_decimal_174_to_roman(self):
        roman_number = decimal_to_roman (174)
        self.assertEqual(roman_number,'CLXXIV')
    def test_decimal_525_to_roman(self):
        roman_number = decimal_to_roman (525)
        self.assertEqual(roman_number,'DXXV')
    def test_decimal_793_to_roman(self):
        roman_number = decimal_to_roman (793)
        self.assertEqual(roman_number,'DCCXCIII')
    def test_decimal_999_to_roman(self):
        roman_number = decimal_to_roman (999)
        self.assertEqual(roman_number,'CMXCIX')
    def test_decimal_1045_to_roman(self):
        roman_number = decimal_to_roman (1045)
        self.assertEqual(roman_number,'MXLV')
    def test_decimal_1436_to_roman(self):
        roman_number = decimal_to_roman (1436)
        self.assertEqual(roman_number,'MCDXXXVI')
    def test_decimal_2061_to_roman(self):
        roman_number = decimal_to_roman (2061)
        self.assertEqual(roman_number,'MMLXI')
    def test_decimal_3578_to_roman(self):
        roman_number = decimal_to_roman (3578)
        self.assertEqual(roman_number,'MMMDLXXVIII')
    def test_decimal_3999_to_roman(self):
        roman_number = decimal_to_roman (3999)
        self.assertEqual(roman_number,'MMMCMXCIX')

if __name__ == '__main__':
   unittest.main()