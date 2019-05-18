import unittest
from list_numbers_2 import find_max


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
   def test_find_max_list_is_not_a_list_UGLY(self):
       try:
           find_max(1234)
           self.fail()
       except Exception:
           pass
   def test_find_max_list_is_not_a_list_UGLY_2(self):
       try:
           find_max([1234, 'hola'])
           self.fail()
       except Exception:
           pass
   def test_find_max_list_is_not_a_list_UGLY_3(self):
       from list_numbers_2 import NotAListException
       from list_numbers_2 import NotAllNumberInListException
       try:
           find_max(1234)
           self.fail()
       except NotAListException:
           pass
       except NotAllNumberInListException:
           self.fail()

   def test_find_max_list_not_all_number_in_list_UGLY(self):
       from list_numbers_2 import NotAListException
       from list_numbers_2 import NotAllNumberInListException
       try:
           find_max([1, 2, 3, 4, 'HOLA'])
           self.fail()
       except NotAListException:
           self.fail()
       except NotAllNumberInListException:
           pass


if __name__ == '__main__':
   unittest.main()