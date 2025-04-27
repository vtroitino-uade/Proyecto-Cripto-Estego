import unittest
from encriptado import vigenere

class TestVigenereASCII(unittest.TestCase):
    """
    Pruebas para el cifrado Vigenère con tabla ASCII.
    """

    def test_cifrar_simple(self):
        self.assertEqual(vigenere("HOLA", "CLAVE"), "ÌÔÑÅ")

    def test_descifrar_simple(self):
        self.assertEqual(vigenere("ÌÔÑÅ", "CLAVE", descifrar=True), "HOLA")

    def test_cifrar_con_espacios(self):
        self.assertEqual(vigenere("HOLA MUNDO", "CLAVE"), "ÌÔÑÅ%ÕÜÑÉÑ")

    def test_descifrar_con_espacios(self):
        self.assertEqual(vigenere("ÌÔÑÅ%ÕÜÑÉÑ", "CLAVE", descifrar=True), "HOLA MUNDO")

    def test_cifrar_con_no_alfabetico(self):
        self.assertEqual(vigenere("HOLA123", "CLAVE"), "ÌÔÑÅ123")

    def test_descifrar_con_no_alfabetico(self):
        self.assertEqual(vigenere("ÌÔÑÅ123", "CLAVE", descifrar=True), "HOLA123")

    def test_cifrar_cadena_vacia(self):
        self.assertEqual(vigenere("", "CLAVE"), "")

    def test_descifrar_cadena_vacia(self):
        self.assertEqual(vigenere("", "CLAVE", descifrar=True), "")

    def test_cifrar_clave_mas_larga_que_texto(self):
        self.assertEqual(vigenere("HI", "CLAVELARGA"), "ÌÔ")

    def test_descifrar_clave_mas_larga_que_texto(self):
        self.assertEqual(vigenere("ÌÔ", "CLAVELARGA", descifrar=True), "HI")

    def test_cifrar_con_caracteres_especiales(self):
        self.assertEqual(vigenere("HOLA!@#", "CLAVE"), "ÌÔÑÅ!@#")

    def test_descifrar_con_caracteres_especiales(self):
        self.assertEqual(vigenere("ÌÔÑÅ!@#", "CLAVE", descifrar=True), "HOLA!@#")

    def test_cifrar_con_caracteres_especiales_mezclados(self):
        self.assertEqual(vigenere("H3LL0!@#", "CLAVE"), "Ì3ÑÑ0!@#")

    def test_descifrar_con_caracteres_especiales_mezclados(self):
        self.assertEqual(vigenere("Ì3ÑÑ0!@#", "CLAVE", descifrar=True), "H3LL0!@#")
