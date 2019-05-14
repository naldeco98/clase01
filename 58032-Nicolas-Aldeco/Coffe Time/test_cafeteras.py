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
    def test_caffe_simple_con_azucar_y_200ml(self):
        self.assertEqual(self.client.pago(True),'-Haciendo Cafe-')
        self.assertEqual(self.client.coffequantity(10),'Cafe con 10 gramos.')
        self.assertEqual(self.client.waterquantity(200),'Cafe con 200 ml de agua')
        self.assertEqual(self.client.sugarquantity(True),'Con azucar')
        #Estado de la maquina
        self.assertEqual(self.client.coffe_level,90)
        self.assertEqual(self.client.water_level,800)
        self.assertEqual(self.client.sugar_level,95)
        self.assertEqual(self.client.coins,1)
    def test_caffe_simple_con_azucar_y_20gr(self):
        self.assertEqual(self.client.pago(True),'-Haciendo Cafe-')
        self.assertEqual(self.client.coffequantity(20),'Cafe con 20 gramos.')
        self.assertEqual(self.client.waterquantity(100),'Cafe con 100 ml de agua')
        self.assertEqual(self.client.sugarquantity(True),'Con azucar')
        #Estado de la maquina
        self.assertEqual(self.client.coffe_level,80)
        self.assertEqual(self.client.water_level,900)
        self.assertEqual(self.client.sugar_level,95)
        self.assertEqual(self.client.coins,1)

class TestBasicCoffeMakerEMPTY(unittest.TestCase):

    def setUp(self):
        self.client = BasicCoffeMaker()
        self.client.coffe_level = 0
        self.client.water_level = 0
        self.client.sugar_level = 0
    
    def test_caffe_simple_EMPTY(self):
        self.assertEqual(self.client.pago(True),'-Haciendo Cafe-')
        self.assertEqual(self.client.coffequantity(10),'No tengo mas cafe,tome su moneda')
        self.assertEqual(self.client.waterquantity(100),'No tengo mas agua,tome su moneda')
        self.assertEqual(self.client.sugarquantity(False),'Sin azucar')
        #Estado de la maquina
        self.assertEqual(self.client.coffe_level,0)
        self.assertEqual(self.client.water_level,0)
        self.assertEqual(self.client.sugar_level,0)
        self.assertEqual(self.client.coins,0)

if __name__ == "__main__":
    unittest.main()