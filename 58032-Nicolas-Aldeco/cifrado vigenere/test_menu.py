import unittest
from menu_vigenere import coder

class TestExpectedErrors(unittest.TestCase):
    def test_SpaceInString(self):
        coder('MECA','Hola Mundo',1)
        self.assertRaises(TypeError)

if __name__ == '__main__':
    unittest.main()