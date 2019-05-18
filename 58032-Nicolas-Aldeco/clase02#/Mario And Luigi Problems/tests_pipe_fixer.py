import unittest
from pipe_fixer import pipe_fix


class TestPipeFixing(unittest.TestCase):
   def test_fix_simple_pipe(self):
       fixed_pipe = pipe_fix([1, 2, 3, 5, 6, 8, 9])
       self.assertEqual(
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           fixed_pipe
       )

   def test_fix_complex_pipe(self):
       fixed_pipe = pipe_fix([1, 2, 3, 12])
       self.assertEqual(
           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
           fixed_pipe
       )

   def test_fix_short_from_6_pipe(self):
       fixed_pipe = pipe_fix([6, 9])
       self.assertEqual(
           [6, 7, 8, 9],
           fixed_pipe
       )

   def test_fix_simple_and_negative_pipe(self):
       fixed_pipe = pipe_fix([-1, 4])
       self.assertEqual(
           [-1, 0, 1, 2, 3, 4],
           fixed_pipe
       )

   def test_fix_already_fixed_pipe(self):
       fixed_pipe = pipe_fix([1, 2, 3])
       self.assertEqual(
           [1, 2, 3],
           fixed_pipe
       )


if __name__ == '__main__':
   unittest.main()