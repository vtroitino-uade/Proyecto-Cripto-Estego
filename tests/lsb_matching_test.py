import unittest

from PIL import Image

from config.rutas import DIR_TEST_RECURSOS
from estego.lsb_matching import lsb_matching
from estego.utils import cargar_imagen

IMAGEN_PRUEBA = cargar_imagen(DIR_TEST_RECURSOS / "imagen_prueba.png")

class TestLsbCodificar(unittest.TestCase):
    def test_codificar_mensaje(self):
        mensaje = "Hola"
        imagen_codificada = lsb_matching(IMAGEN_PRUEBA, mensaje)
        self.assertIsInstance(imagen_codificada, Image.Image)

    def test_mensaje_demasiado_largo(self):
        imagen_chica = Image.new("RGB", (10, 10), color="white")
        mensaje_demasiado_largo = "a" * 1000

        with self.assertRaises(ValueError):
            lsb_matching(imagen_chica, mensaje_demasiado_largo)

    def test_mensaje_vacio(self):
        mensaje_vacio = ""
        imagen_codificada = lsb_matching(IMAGEN_PRUEBA, mensaje_vacio)
        self.assertIsInstance(imagen_codificada, Image.Image)

    def test_mensaje_caracteres_especiales(self):
        mensaje_con_salto = "Hol@,\nmundo!"
        imagen_codificada = lsb_matching(IMAGEN_PRUEBA, mensaje_con_salto)
        self.assertIsInstance(imagen_codificada, Image.Image)

class TestLsbDecodificar(unittest.TestCase):
    def test_decodificar_mensaje(self):
        mensaje = "Hola"
        imagen_codificada = lsb_matching(IMAGEN_PRUEBA, mensaje)
        mensaje_extraido = lsb_matching(imagen_codificada)
        self.assertEqual(mensaje, mensaje_extraido)

    def test_decodificar_mensaje_vacio(self):
        imagen_codificada = lsb_matching(IMAGEN_PRUEBA, "")
        mensaje_extraido = lsb_matching(imagen_codificada)
        self.assertEqual("", mensaje_extraido)

    def test_decodificar_mensaje_caracteres_especiales(self):
        mensaje_con_salto = "Hol@,\nmundo!"
        imagen_codificada = lsb_matching(IMAGEN_PRUEBA, mensaje_con_salto)
        mensaje_extraido = lsb_matching(imagen_codificada)
        self.assertEqual(mensaje_con_salto, mensaje_extraido)

if __name__ == '__main__':
    unittest.main()
