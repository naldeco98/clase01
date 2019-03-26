import unittest
from ronam_numbers import roman_to_decimal



class TestRomanNumbers(unittest.TestCase):
    def test_roman_I_to_decimal(self):
       decimal_number = roman_to_decimal('I')
       self.assertEqual(decimal_number, 1)
    def test_roman_II_to_decimal(self):
        decimal_number = roman_to_decimal('II')
        self.assertEqual(decimal_number,2)
    def test_roman_III_to_decimal(self):
        decimal_number = roman_to_decimal('III')
        self.assertEqual(decimal_number,3)
    def test_roman_V_to_decimal(self):
        decimal_number = roman_to_decimal('V')
        self.assertEqual (decimal_number,5)
    def test_roman_IV_to_decimal(self):
        decimal_number = roman_to_decimal('IV')
        self.assertEqual (decimal_number,4)
    def test_roman_XXIV_to_decimal(self):
        decimal_number = roman_to_decimal('XXIV')
        self.assertEqual (decimal_number,24)

if __name__ == '__main__':
   unittest.main()