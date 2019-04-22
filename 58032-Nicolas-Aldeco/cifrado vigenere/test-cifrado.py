import unittest
from cifrado_vigenere import encode,decode

class TestEncyption(unittest.TestCase):
    def test_word_HOLAMUNDO_key_MECA(self):
        code = encode('MECA','HOLAMUNDO')
        self.assertEqual(code,'TSNAYYPDA')
    def test_word_HOLAMUNDO_key_LIME(self):
        code = encode('LIME','HOLAMUNDO')
        self.assertEqual(code,'SWXEXCZHZ')
    def test_TURINERAUNCAPO_key_MASTER(self):
        code = encode('MASTER','TURINERAUNCAPO')
        self.assertEqual(code,'FUJBRVDAMGGRBO')
    def test_MAGIA_key_LOCOS(self):     #Largo de palabra igual a clave
        code = encode('LOCOS','MAGIA')
        self.assertEqual(code,'XOIWS')

class TestDecryption(unittest.TestCase):
    def test_code_TSNAYYPDA_key_MECA(self):
        word = decode('TSNAYYPDA','MECA')
        self.assertEqual(word,'HOLAMUNDO')
    def test_code_SWXEXCZHZ_key_LIME(self):
        word = decode('SWXEXCZHZ','LIME')
        self.assertEqual(word,'HOLAMUNDO')
    def test_code_FUJBRVDAMGGRBO_key_MASTER(self):
        word = decode('FUJBRVDAMGGRBO','MASTER')
        self.assertEqual(word,'TURINERAUNCAPO')
    def test_code_XOIWS_key_LOCOS(self):     #Largo de palabra igual a clave
        word = decode('XOIWS','LOCOS')
        self.assertEqual(word,'MAGIA')

if __name__ == '__main__':
   unittest.main()