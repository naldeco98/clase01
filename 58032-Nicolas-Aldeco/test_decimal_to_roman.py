import unittest
from decimal_roman import decimal_to_roman

class TestDecimalNumbers(unittest.TestCase):
    def test_decimal_1_to_roman(self):
        roman_number = decimal_to_roman (1)
        self.assertEqual(roman_number,'I')
    def test_decimal_2_to_roman(self):
        roman_number = decimal_to_roman (2)
        self.assertEqual(roman_number,'II')
#    def test_decimal_3_to_roman(self):
#        roman_number = decimal_to_roman (3)
#        self.assertEqual(roman_number,'III')
#    def test_decimal_4_to_roman(self):
#        roman_number = decimal_to_roman (4)
#        self.assertEqual(roman_number,'IV')    

if __name__ == '__main__':
   unittest.main()