import unittest
from interfaz_factorial import menu


class TestInterfazFactorial(unittest.TestCase):
   def test_interfaz_factorial_5(self):
       result = menu('5')
       self.assertEqual(result,120)

   def test_interfaz_factorial_hola(self):
        result = menu('hola')
        self.assertEqual(result,'Error-No es un numero')

   def test_interfaz_factorial_negative(self):
        result = menu('-5')
        self.assertEqual(result,'Error-No puede ingresar un numero negativo')
       


if __name__ == '__main__':
   unittest.main()