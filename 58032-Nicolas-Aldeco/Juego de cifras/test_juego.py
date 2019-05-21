import unittest
from juego_de_numeros import Game,HumanVsComputer,ComputerVsHuman

class TestHumanVComputer(unittest.TestCase):

    def setUp(self):
        self.gameplay = HumanVsComputer()
        self.gameplay.number = '1234'

    def test_advinar4B(self):
        self.assertEqual(self.gameplay.play('9999'),'All Bads try other number.')
        self.assertEqual(self.gameplay.play('1993'),'You have 1G1R')
        self.assertEqual(self.gameplay.tries,2)
        self.assertTrue(self.gameplay.game_status)
    def test_advinar3B1R_then_2B2R(self):
        self.assertEqual(self.gameplay.play('9993'),'You have 1R')
        self.assertEqual(self.gameplay.play('9493'),'You have 2R')
        self.assertEqual(self.gameplay.tries,2)
        self.assertTrue(self.gameplay.game_status)
    def test_advinar_4tries(self):
        self.assertEqual(self.gameplay.play('1245'),'You have 2G1R')
        self.assertEqual(self.gameplay.play('5458'),'You have 1R')
        self.assertEqual(self.gameplay.play('1324'),'You have 2G2R')
        self.assertEqual(self.gameplay.play('1234'),'All Goods, you win!')
        self.assertEqual(self.gameplay.tries,4)
        self.assertFalse(self.gameplay.game_status)
    def test_advinar_win(self):
        self.assertEqual(self.gameplay.play('1234'),'All Goods, you win!')
        self.assertEqual(self.gameplay.tries,1)
        self.assertFalse(self.gameplay.game_status)

class TestComputerVsHuman(unittest.TestCase):

    def setUp(self):
        self.gameplay = ComputerVsHuman()

    def test_computer_playing(self):        #Pensador = 1234
        self.assertEqual(self.gameplay.play(),'Is your number 0000?')
        self.gameplay.clue = '0G0R'
        self.assertEqual(self.gameplay.play(),'Is your number 1111?')
        self.gameplay.clue = '1G3R'
        self.assertEqual(self.gameplay.play(),'Is your number 2222?')
        self.gameplay.clue = '1G3R'
        self.assertEqual(self.gameplay.play(),'Is your number 3333?')
        self.gameplay.clue = '1G3R'
        self.assertEqual(self.gameplay.play(),'Is your number 4444?')
        self.gameplay.clue = '1G3R'
        self.assertEqual(self.gameplay.play(),'Is your number 5555?')
        self.gameplay.clue = '0G0R'
        self.assertEqual(self.gameplay.play(),'Is your number 6666?')
        self.gameplay.clue = '0G0R'
        self.assertEqual(self.gameplay.play(),'Is your number 7777?')
        self.gameplay.clue = '0G0R'
        self.assertEqual(self.gameplay.play(),'Is your number 8888?')
        self.gameplay.clue = '0G0R'
        self.assertEqual(self.gameplay.play(),'Is your number 9999?')
        self.gameplay.clue = '0G0R'
        



if __name__ == "__main__":
    unittest.main()