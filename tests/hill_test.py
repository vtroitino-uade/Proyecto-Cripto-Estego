import unittest
import numpy as np
from encriptado import hill

class PruebasHillFuncionPrincipal(unittest.TestCase):

    def test_cifrado_y_descifrado_2x2(self):
        clave = np.array([[3, 3], [2, 5]])
        mensaje = "MENSAJE"
        cifrado = hill(mensaje, clave)
        descifrado = hill(cifrado, clave, descifrar=True)
        self.assertEqual(descifrado, mensaje.upper())

    def test_cifrado_y_descifrado_3x3(self):
        clave = np.array([[6, 24, 1],
                        [13, 16, 10],
                        [20, 17, 15]])
        mensaje = "CRIPTOGRAFIA"
        cifrado = hill(mensaje, clave)
        descifrado = hill(cifrado, clave, descifrar=True)
        self.assertEqual(descifrado, mensaje.upper())

    def test_clave_invalida_formato(self):
        clave = np.array([[1, 2, 3], [4, 5, 6]])  # No es cuadrada
        mensaje = "TEXTO"
        with self.assertRaises(ValueError):
            hill(mensaje, clave)

    def test_clave_invalida_no_invertible(self):
        clave = np.array([[2, 4], [2, 4]])  # Determinante = 0 → no invertible
        mensaje = "HILL"
        with self.assertRaises(ValueError):
            hill(mensaje, clave)

    def test_mensaje_con_letras_minusculas_y_espacios(self):
        clave = np.array([[3, 3], [2, 5]])
        mensaje = "hola mundo"
        cifrado = hill(mensaje, clave)
        descifrado = hill(cifrado, clave, descifrar=True)
        # Solo compara las letras válidas (sin espacios)
        self.assertEqual(descifrado, "HOLAMUNDO")

if __name__ == "__main__":
    unittest.main()
