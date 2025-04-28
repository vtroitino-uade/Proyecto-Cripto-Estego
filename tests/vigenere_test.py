import unittest
from encriptado import vigenere

class TestVigenereASCII(unittest.TestCase):
    """
    Pruebas para el cifrado Vigenère con tabla ASCII.
    """

    def test_cifrar_simple(self):
        self.assertEqual(vigenere("Hola", "CLAVE"), "k<.8")

    def test_descifrar_simple(self):
        self.assertEqual(vigenere("k<.8", "CLAVE", descifrar=True), "Hola")

    def test_cifrar_con_espacios(self):
        self.assertEqual(vigenere("Hola Mundo", "CLAVE"), "k<.8EpB0;5")

    def test_descifrar_con_espacios(self):
        self.assertEqual(vigenere("k<.8EpB0;5", "CLAVE", descifrar=True), "Hola Mundo")

    def test_cifrar_con_no_alfabetico(self):
        self.assertEqual(vigenere("HOLA123", "CLAVE"), "k{mwVU_")

    def test_descifrar_con_no_alfabetico(self):
        self.assertEqual(vigenere("k{mwVU_", "CLAVE", descifrar=True), "HOLA123")

    def test_cifrar_cadena_vacia(self):
        self.assertEqual(vigenere("", "CLAVE"), "")

    def test_descifrar_cadena_vacia(self):
        self.assertEqual(vigenere("", "CLAVE", descifrar=True), "")

    def test_cifrar_clave_mas_larga_que_texto(self):
        self.assertEqual(vigenere("HI", "CLAVELARGA"), "ku")

    def test_descifrar_clave_mas_larga_que_texto(self):
        self.assertEqual(vigenere("ku", "CLAVELARGA", descifrar=True), "HI")

    def test_cifrar_con_caracteres_especiales(self):
        self.assertEqual(vigenere("HOLA!@#", "CLAVE"), "k{mwFcO")

    def test_descifrar_con_caracteres_especiales(self):
        self.assertEqual(vigenere("k{mwFcO", "CLAVE", descifrar=True), "HOLA!@#")
