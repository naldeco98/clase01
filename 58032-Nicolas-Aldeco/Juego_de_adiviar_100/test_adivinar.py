import unittest
from gng import (
    ComputerAgainstHumanGame,
    HumanAgainstComputerGame
)


class TestHumanAgainstComputerGame(unittest.TestCase):
    def setUp(self):
        self.game = HumanAgainstComputerGame()
        self.game.secret_number = 78

    def test_play_small(self):
        self.assertEquals(self.game.play(50), 'My number is bigger')
        self.assertTrue(self.game.is_playing)

    def test_play_big(self):
        self.assertEquals(self.game.play(80), 'My number is smaller')
        self.assertTrue(self.game.is_playing)

    def test_play_win(self):
        self.assertEquals(self.game.play(78), 'You win')
        self.assertFalse(self.game.is_playing)


class TestComputerAgainstHuman(unittest.TestCase):
    def setUp(self):
        self.game = ComputerAgainstHumanGame()

    def test_guess_number(self):    #77
        self.assertEquals(self.game.input_text(), 'Is it your number 50?')
        self.game.play('+')
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.input_text(), 'Is it your number 75?')
        self.game.play('+')
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.input_text(), 'Is it your number 87?')
        self.game.play('-')
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.input_text(), 'Is it your number 81?')
        self.game.play('-')
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.input_text(), 'Is it your number 78?')
        self.game.play('-')
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.input_text(), 'Is it your number 77?')
        self.game.play('=')
        self.assertFalse(self.game.is_playing)

    def test_guess_number2(self):   #34
        self.assertEquals(self.game.input_text(), 'Is it your number 50?')
        self.game.play('-')
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.input_text(), 'Is it your number 25?')
        self.game.play('+')
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.input_text(), 'Is it your number 37?')
        self.game.play('-')
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.input_text(), 'Is it your number 31?')
        self.game.play('+')
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.input_text(), 'Is it your number 34?')
        self.game.play('=')
        self.assertFalse(self.game.is_playing)

if __name__ == "__main__":
    unittest.main()