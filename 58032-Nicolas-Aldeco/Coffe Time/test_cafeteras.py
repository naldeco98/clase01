import unittest
from cafeteras import Machine,BasicCoffeMaker;

class TestBasicCoffeMakerFULL(unittest.TestCase):

    def setUp(self):
        self.client = BasicCoffeMaker()

    def test_caffe_simple_sin_azucar(self):
        self.assertEqual(self.client.pago(True),'-Haciendo Cafe-')
        self.assertEqual(self.client.coffequantity(10),'Cafe con 10 gramos.')
        self.assertEqual(self.client.waterquantity(100),'Cafe con 100 ml de agua')
        self.assertEqual(self.client.sugarquantity(False),'Sin azucar')
        #Estado de la maquina
        self.assertEqual(self.client.coffe_level,90)
        self.assertEqual(self.client.water_level,900)
        self.assertEqual(self.client.sugar_level,100)
        self.assertEqual(self.client.coins,1)
    def test_caffe_simple_con_azucar(self):
        self.assertEqual(self.client.pago(True),'-Haciendo Cafe-')
        self.assertEqual(self.client.coffequantity(10),'Cafe con 10 gramos.')
        self.assertEqual(self.client.waterquantity(100),'Cafe con 100 ml de agua')
        self.assertEqual(self.client.sugarquantity(True),'Con azucar')
        #Estado de la maquina
        self.assertEqual(self.client.coffe_level,90)
        self.assertEqual(self.client.water_level,900)
        self.assertEqual(self.client.sugar_level,95)
        self.assertEqual(self.client.coins,1)


if __name__ == "__main__":
    unittest.main()