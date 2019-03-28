import unittest
from decimal_roman import decimal_to_roman

class TestDecimalNumbers(unittest.TestCase):
    def test_decimal_1_to_roman(self):
        roman_number = decimal_to_roman (1)
        self.assertEqual(roman_number,'I')

if __name__ == '__main__':
   unittest.main()