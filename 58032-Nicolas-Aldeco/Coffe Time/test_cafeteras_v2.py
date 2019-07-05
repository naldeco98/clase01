import unittest
from cafeteras_v2 import *

class TestMachineState(unittest.TestCase):

    def setUp(self):
        self.cliente = Machine_State()
    def test_agregar_agua(self):    #1
        self.cliente.add_water(1000)
        self.assertEqual(self.cliente.water_level,1000)
    def test_agregar_cafe(self):    #2
        self.cliente.add_coffe(1000)
        self.assertEqual(self.cliente.coffe_level,1000)
    def test_agregar_azucar(self):  #3
        self.cliente.add_sugar(1000)
        self.assertEqual(self.cliente.sugar_level,1000)
    def test_quitar_agua(self):     #4
        self.cliente.add_water(1000)
        self.cliente.remove_water(100)
        self.assertEqual(self.cliente.water_level,900)
    def test_quitar_cafe(self):     #5
        self.cliente.add_coffe(1000)
        self.cliente.remove_coffe(100)
        self.assertEqual(self.cliente.coffe_level,900)
    def test_quitar_azucar(self):   #6
        self.cliente.add_sugar(1000)
        self.cliente.remove_sugar(100)
        self.assertEqual(self.cliente.sugar_level,900)

class TestBaseCoffe(unittest.TestCase):

    def setUp(self):
        self.cliente = BaseCoffe()
    def test_cafe_100water_sin_azucar(self):
        self.cliente.payment(1)
        self.assertEqual(self.cliente.making_coffe(100,False),'Su cafe esta listo.')

if __name__ == '__main__':
    unittest.main()