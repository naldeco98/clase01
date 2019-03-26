import unittest                                         #Nicolas Aldeco 26/03/19
from ronam_numbers import roman_to_decimal



class TestRomanNumbers(unittest.TestCase):
    def test_roman_I_to_decimal(self):      #1
       decimal_number = roman_to_decimal('I')
       self.assertEqual(decimal_number, 1)
    def test_roman_II_to_decimal(self):     #2
        decimal_number = roman_to_decimal('II')
        self.assertEqual(decimal_number,2)
    def test_roman_III_to_decimal(self):    #3
        decimal_number = roman_to_decimal('III')
        self.assertEqual(decimal_number,3)
    def test_roman_V_to_decimal(self):      #5
        decimal_number = roman_to_decimal('V')
        self.assertEqual (decimal_number,5)
    def test_roman_IV_to_decimal(self):     #4
        decimal_number = roman_to_decimal('IV')
        self.assertEqual (decimal_number,4)
    def test_roman_XXIV_to_decimal(self):       #24
        decimal_number = roman_to_decimal('XXIV')
        self.assertEqual (decimal_number,24)
    def test_roman_XLIII_to_decimal(self):      #43
        decimal_number = roman_to_decimal('XLIII')
        self.assertEqual (decimal_number,43)
    def test_roman_LVIII_to_decimal(self):      #58
        decimal_number = roman_to_decimal('LVIII')
        self.assertEqual (decimal_number,58)
    def test_roman_LXXII_to_decimal(self):      #72
        decimal_number = roman_to_decimal('LXXII')
        self.assertEqual (decimal_number,72)
    def test_roman_LXXXVII_to_decimal(self):      #87
        decimal_number = roman_to_decimal('LXXXVII')
        self.assertEqual (decimal_number,87)
    def test_roman_XCI_to_decimal(self):      #91
        decimal_number = roman_to_decimal('XCI')
        self.assertEqual (decimal_number,91)
    def test_roman_XCIX_to_decimal(self):      #99
        decimal_number = roman_to_decimal('XCIX')
        self.assertEqual (decimal_number,99)
    def test_roman_CI_to_decimal(self):      #101
        decimal_number = roman_to_decimal('CI')
        self.assertEqual (decimal_number,101)
    def test_roman_CXLIX_to_decimal(self):      #149
        decimal_number = roman_to_decimal('CXLIX')
        self.assertEqual (decimal_number,149)
    def test_roman_CDLXXVIII_to_decimal(self):      #478
        decimal_number = roman_to_decimal('CDLXXVIII')
        self.assertEqual (decimal_number,478)
    def test_roman_DCXCIII_to_decimal(self):      #693
        decimal_number = roman_to_decimal('DCXCIII')
        self.assertEqual (decimal_number,693)
    def test_roman_CMLVIII_to_decimal(self):      #958
        decimal_number = roman_to_decimal('CMLVIII')
        self.assertEqual (decimal_number,958)  
    def test_roman_MMCMLIV_to_decimal(self):      #2954
        decimal_number = roman_to_decimal('MMCMLIV')
        self.assertEqual (decimal_number,2954) 
    def test_roman_MMMCDLXIX_to_decimal(self):      #3469
        decimal_number = roman_to_decimal('MMMCDLXIX')
        self.assertEqual (decimal_number,3469)  
    def test_roman_MMMCMXCIX_to_decimal(self):      #3999
        decimal_number = roman_to_decimal('MMMCMXCIX')
        self.assertEqual (decimal_number,3999)  

if __name__ == '__main__':
   unittest.main()