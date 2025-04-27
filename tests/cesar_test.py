import unittest
from encriptado import cesar

class TestCesarASCII(unittest.TestCase):
    """
    Pruebas para el cifrado César con tabla ASCII.
    """
    def test_clave_positiva(self):
        self.assertEqual(cesar("ñxyz1234", 3), "ñ{|}4567")
        self.assertEqual(cesar("hola", 5), "mtqf")

    def test_clave_negativa(self):
        self.assertEqual(cesar("abcd", -3), "^_`a")
        self.assertEqual(cesar("mtqf", -5), "hola")

    def test_clave_cero(self):
        self.assertEqual(cesar("abcñ", 0), "abcñ")
        self.assertEqual(cesar("hola", 0), "hola")

    def test_mensaje_vacio(self):
        self.assertEqual(cesar("", 5), "")
        self.assertEqual(cesar("", -5), "")

    def test_clave_positiva_grande(self):
        self.assertEqual(cesar("abcñ", 30), ' !"ñ')
        self.assertEqual(cesar("hola", 190), "hola")

    def test_calve_negativa_grande(self):
        self.assertEqual(cesar(' !"ñ', -30), "abcñ")
        self.assertEqual(cesar("hola", -190), "hola")

    def test_descifrar(self):
        self.assertEqual(cesar("Htsywfwwj{tqzhntsfwnt", 5, descifrar=True), "Contrarrevolucionario")

class TestCesarAlfabetoEspanolYNumeros(unittest.TestCase):
    """
    Pruebas para el cifrado César con el alfabeto español y números.
    """
    ESP_NUM = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"

    def test_clave_positiva(self):
        self.assertEqual(cesar("xyzñ", 2, alfabeto=self.ESP_NUM), "z01p")
        self.assertEqual(cesar("hola", 5, alfabeto=self.ESP_NUM), "mtpf")

    def test_clave_negativa(self):
        self.assertEqual(cesar("zabñ", -2, alfabeto=self.ESP_NUM), "x89m")
        self.assertEqual(cesar("mtpf", -5, alfabeto=self.ESP_NUM), "hola")

    def test_clave_cero(self):
        self.assertEqual(cesar("abcñ", 0, alfabeto=self.ESP_NUM), "abcñ")
        self.assertEqual(cesar("hola", 0, alfabeto=self.ESP_NUM), "hola")

    def test_caracteres_no_alfabeticos(self):
        self.assertEqual(cesar("@abcñ123", 3, alfabeto=self.ESP_NUM), "@defq456")
        self.assertEqual(cesar("hola, mundo!", 5, alfabeto=self.ESP_NUM), "mtpf, qzrit!")
        self.assertEqual(cesar("xyzñ!", -2, alfabeto=self.ESP_NUM), "vwxm!")

    def test_mensaje_vacio(self):
        self.assertEqual(cesar("", 5, alfabeto=self.ESP_NUM), "")
        self.assertEqual(cesar("", -5, alfabeto=self.ESP_NUM), "")

    def test_clave_positiva_grande(self):
        self.assertEqual(cesar("abcñ", 30, alfabeto=self.ESP_NUM), "345h")
        self.assertEqual(cesar("hola", 54, alfabeto=self.ESP_NUM), "x51q")

    def test_calve_negativa_grande(self):
        self.assertEqual(cesar("defo", -30, alfabeto=self.ESP_NUM), "klmv")
        self.assertEqual(cesar("hola", -54, alfabeto=self.ESP_NUM), "084t")

    def test_descifrar(self):
        self.assertEqual(cesar("Htrywfwwj0tpzhntrfwnt", 5, descifrar=True, alfabeto=self.ESP_NUM), "Contrarrevolucionario")
