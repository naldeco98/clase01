import unittest
from clases import Calculator

class TestCalculador(unittest.TestCase):
    def test_resul_calculator_1_add_1_(self):
        calc = Calculator()
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('1')
        calc.ingresar('=')

        self.assertEqual(calc.display(),'2')

    def test_resul_calculator_2_add_2_(self):
        calc = Calculator()
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('=')

        self.assertEqual(calc.display(),'4')

    def test_resul_calculator_11_add_4_(self):
        calc = Calculator()
        calc.ingresar('1')
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('4')
        calc.ingresar('=')

        self.assertEqual(calc.display(),'15')

    def test_resul_calculator_1_add_2_add_3(self):
        calc = Calculator()
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('3')
        calc.ingresar('=')

        self.assertEqual(calc.display(),'6')

    def test_resul_calculator_1_add_2_times_3(self):
        calc = Calculator()
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('*')
        calc.ingresar('3')
        calc.ingresar('=')

        self.assertEqual(calc.display(),'9')

    def test_resul_calculator_click_C(self):
        calc = Calculator()
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('3')
        calc.ingresar('C')

        self.assertEqual(calc.display(),'0')


if __name__ == "__main__":
    unittest.main()