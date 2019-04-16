import unittest
from factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial_1(self):
        result = factorial(1)
        self.assertEqual(result, 1)

    def test_factorial_2(self):
        result = factorial(2)
        self.assertEqual(result, 2)

    def test_factorial_3(self):
        result = factorial(3)
        self.assertEqual(result, 6)

    def test_factorial_4(self):
        result = factorial(4)
        self.assertEqual(result, 24)

    def test_factorial_5(self):
        result = factorial(5)
        self.assertEqual(result, 120)

    def test_factorial_6(self):
        result = factorial(6)
        self.assertEqual(result, 720)

    def test_factorial_7(self):
        result = factorial(7)
        self.assertEqual(result, 5040)

    def test_factorial_8(self):
        result = factorial(8)
        self.assertEqual(result, 40320)

    def test_factorial_9(self):
        result = factorial(9)
        self.assertEqual(result, 362880)


if __name__ == '__main__':
    unittest.main()
