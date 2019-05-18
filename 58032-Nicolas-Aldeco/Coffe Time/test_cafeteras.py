import unittest
from cafeteras import MachineForCoffe,BasicCoffeMaker,PremiumCoffeMaker;

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
        self.client.water_level = 0
        self.client.sugar_level = 0
    
    def test_caffe_simple_EMPTY_NoCoffe(self):
        self.client.coffe_level = 0
        self.assertEqual(self.client.pago(True),'Disculpe no tengo mas cafe. Tome su moneda')
        self.assertFalse(self.client.makingCoffe)
        #Estado de la maquina
        self.assertEqual(self.client.coffe_level,0)
        self.assertEqual(self.client.water_level,0)
        self.assertEqual(self.client.sugar_level,0)
        self.assertEqual(self.client.coins,0)

    def test_caffe_simple_EMPTY_NoWater(self):
        self.assertEqual(self.client.pago(True),'-Haciendo Cafe-')
        self.assertEqual(self.client.waterquantity(100),'No tengo mas agua,tome su moneda')
        #Estado de la maquina
        self.assertEqual(self.client.coffe_level,100)
        self.assertEqual(self.client.water_level,0)
        self.assertEqual(self.client.sugar_level,0)
        self.assertEqual(self.client.coins,0)

    def test_caffe_simple_EMPTY_NoSugar(self):
        self.assertEqual(self.client.pago(True),'-Haciendo Cafe-')
        self.assertEqual(self.client.sugarquantity(True),'No tengo mas azucar,tome su moneda')
        #Estado de la maquina
        self.assertEqual(self.client.coffe_level,100)
        self.assertEqual(self.client.water_level,0)
        self.assertEqual(self.client.sugar_level,0)
        self.assertEqual(self.client.coins,0)

class TestPremiumCoffeMakerFULL(unittest.TestCase):

    def setUp(self):
        self.client = PremiumCoffeMaker()

    def test_caffe_premium_sin_leche_sin_azucar(self):
        self.assertEqual(self.client.pago(True),'-Haciendo Cafe-')
        self.assertEqual(self.client.cupcheck(True),'Vaso en compartimiento')
        self.assertEqual(self.client.withmilk(False),'Cafe solo')
        self.assertEqual(self.client.sugarquantity(0),'Cafe con 0 gramos.')
        self.assertEqual(self.client.coffequantity(10),'Cafe con 10 gramos.')
        self.assertEqual(self.client.waterquantity(100),'Cafe con 100 ml de agua')
        #Estado de la maquina
        self.assertEqual(self.client.water_level,900)
        self.assertEqual(self.client.coffe_level,90)
        self.assertEqual(self.client.coins,1)
        self.assertEqual(self.client.milklevel,1000)

    def test_caffe_premium_con_leche_con_3_de_azucar(self):
        self.assertEqual(self.client.pago(True),'-Haciendo Cafe-')
        self.assertEqual(self.client.cupcheck(True),'Vaso en compartimiento')
        self.assertEqual(self.client.withmilk(True),'Cafe con leche')
        self.assertEqual(self.client.sugarquantity(3),'Cafe con leche con 3 gramos.')
        self.assertEqual(self.client.coffequantity(10),'Cafe con leche con 10 gramos.')
        self.assertEqual(self.client.waterquantity(100),'Cafe con leche con 100 ml de agua')
        #Estado de la maquina
        self.assertEqual(self.client.water_level,900)
        self.assertEqual(self.client.coffe_level,90)
        self.assertEqual(self.client.sugar_level,97)
        self.assertEqual(self.client.coins,1)
        self.assertEqual(self.client.milklevel,900)

    def test_no_cup(self):
        self.assertEqual(self.client.cupcheck(False),'Ponga un vaso por favor')

class TestPremiumCoffeMakerEMPTY(unittest.TestCase):

    def setUp(self):
        self.client = PremiumCoffeMaker()
        self.client.water_level = 0
        self.client.sugar_level = 0
        self.client.milklevel = 0

    def test_No_coffe(self):
        self.client.coffe_level = 0
        self.assertEqual(self.client.pago(True),'Disculpe no tengo mas cafe. Tome su moneda')
        self.assertFalse(self.client.makingCoffe)
        #Estado de la maquina
        self.assertEqual(self.client.water_level,0)
        self.assertEqual(self.client.coffe_level,0)
        self.assertEqual(self.client.sugar_level,0)
        self.assertEqual(self.client.coins,0)
        self.assertEqual(self.client.milklevel,0)

if __name__ == "__main__":
    unittest.main()