import unittest
from juego_de_numeros import Game,HumanVsComputer

class TestHumanVComputer(unittest.TestCase):

    def setUp(self):
        self.gameplay = HumanVsComputer()
        self.gameplay.number = '1234'

    def test_advinar4B(self):
        self.assertEqual(self.gameplay.play('9999'),'4B')
        self.assertEqual(self.gameplay.tries,1)
        self.assertTrue(self.gameplay.game_status)
    def test_advinar3B1R_then_2B2R(self):
        self.assertEqual(self.gameplay.play('9993'),'3B1R')
        self.assertEqual(self.gameplay.play('9493'),'2B2R')
        self.assertEqual(self.gameplay.tries,2)
        self.assertTrue(self.gameplay.game_status)
    def test_advinar_4tries(self):
        self.assertEqual(self.gameplay.play('1245'),'1B2G1R')
        self.assertEqual(self.gameplay.play('5458'),'3B1R')
        self.assertEqual(self.gameplay.play('1324'),'2G2R')
        self.assertEqual(self.gameplay.play('1234'),'4G')
        self.assertEqual(self.gameplay.tries,4)
        self.assertFalse(self.gameplay.game_status)
    def test_advinar_win(self):
        self.assertEqual(self.gameplay.play('1234'),'4G')
        self.assertEqual(self.gameplay.tries,1)
        self.assertFalse(self.gameplay.game_status)


if __name__ == "__main__":
    unittest.main()