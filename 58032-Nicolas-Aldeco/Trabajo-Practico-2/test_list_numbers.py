import unittest
from list_numbers import find_max


class TestNumbersFinder(unittest.TestCase):
   def test_find_max_simple_list(self):
       max_number = find_max([1, 2, 3, 4])
       self.assertEqual(max_number, 4)

   def test_find_max_simple_unorder_list(self):
       max_number = find_max([4, 1, 2, 3])
       self.assertEqual(max_number, 4)

   def test_find_max_simple_with_similars_list(self):
       max_number = find_max([8, 8, 8, 8])
       self.assertEqual(max_number, 8)

   def test_find_max_list_with_zero(self):
       max_number = find_max([0])
       self.assertEqual(max_number, 0)

   def test_find_max_empty_list(self):
       max_number = find_max([])
       self.assertIsNone(max_number)


if __name__ == '__main__':
   unittest.main()