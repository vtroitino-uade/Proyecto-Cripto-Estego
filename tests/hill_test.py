import unittest
import numpy as np
from encriptado import cifrar, descifrar, validar_clave

class PruebasCifradoHill(unittest.TestCase):

    def test_cifrado_y_descifrado_2x2(self):
        clave = np.array([[3, 3], [2, 5]])
        texto = "HOLA"
        cifrado = cifrar(texto, clave)
        descifrado = descifrar(cifrado, clave, largo_original=len(texto))
        self.assertEqual(descifrado, texto.upper())

    def test_cifrado_y_descifrado_3x3(self):
        clave = np.array([[6, 24, 1],
                        [13, 16, 10],
                        [20, 17, 15]])
        texto = "PRUEBAHILL"
        cifrado = cifrar(texto, clave)
        descifrado = descifrar(cifrado, clave, largo_original=len(texto))
        self.assertEqual(descifrado, texto.upper())

    def test_clave_no_invertible(self):
        clave = np.array([[2, 4], [2, 4]])  # Determinante 0
        texto = "PRUEBA"
        with self.assertRaises(ValueError):
            cifrar(texto, clave)

    def test_validar_clave_valida(self):
        clave = np.array([[3, 3], [2, 5]])
        es_valida, _ = validar_clave(clave)
        self.assertTrue(es_valida)

    def test_validar_clave_invalida(self):
        clave = np.array([[2, 4], [2, 4]])
        es_valida, _ = validar_clave(clave)
        self.assertFalse(es_valida)

if __name__ == "__main__":
    unittest.main()