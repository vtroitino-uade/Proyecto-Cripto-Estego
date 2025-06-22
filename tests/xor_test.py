import unittest

from encriptado import xor

class TestXOR(unittest.TestCase):
    def test_codificar_mensaje(self):
        mensaje = "ESTAMOS FRENTE A UN GRAVE PROBLEMA"
        clave = "barcelona"
        cifrado = xor(mensaje, clave)
        descifrado = xor(cifrado, clave, descifrar=True)
        self.assertEqual(descifrado, mensaje)

    def test_codificar_mensaje_corto_con_clave_larga(self):
        mensaje = "abc"
        clave = "clave_larga"
        cifrado = xor(mensaje, clave)
        descifrado = xor(cifrado, clave, descifrar=True)
        self.assertEqual(descifrado, mensaje)

    def test_mensaje_con_caracteres_especiales(self):
        mensaje = "Hola, mundo! @2023"
        clave = "clave123"
        cifrado = xor(mensaje, clave)
        descifrado = xor(cifrado, clave, descifrar=True)
        self.assertEqual(descifrado, mensaje)

    def test_codificar_mensaje_vacio(self):
        mensaje = ""
        clave = "clave123"
        cifrado = xor(mensaje, clave)
        descifrado = xor(cifrado, clave, descifrar=True)
        self.assertEqual(descifrado, mensaje)

    def test_codificar_mensaje_con_clave_vacia(self):
        with self.assertRaises(ValueError):
            mensaje = "Mensaje con clave vacía"
            clave = ""
            xor(mensaje, clave)

if __name__ == '__main__':
    unittest.main()
