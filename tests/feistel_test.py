import unittest

from encriptado import feistel

class TestFeistel(unittest.TestCase):

    def test_codificar_mensaje_corto(self):
        mensaje = "Hola"
        clave = "clave"
        rondas = 4
        cifrado = feistel(mensaje, clave, rondas)
        descifrado = feistel(cifrado, clave, rondas, descifrar=True)
        self.assertEqual(mensaje, descifrado)

    def test_codificar_mensaje_largo(self):
        mensaje = "Este es un mensaje largo para probar el cifrado Feistel."
        clave = "clave"
        rondas = 4
        cifrado = feistel(mensaje, clave, rondas)
        descifrado = feistel(cifrado, clave, rondas, descifrar=True)
        self.assertEqual(mensaje, descifrado)

    def test_codificar_mensaje_vacio(self):
        mensaje = ""
        clave = "clave"
        rondas = 4
        cifrado = feistel(mensaje, clave, rondas)
        descifrado = feistel(cifrado, clave, rondas, descifrar=True)
        self.assertEqual(mensaje, descifrado)

    def test_codificar_mensaje_con_caracteres_especiales(self):
        mensaje = "Hola, mundo! @2023"
        clave = "clave"
        rondas = 4
        cifrado = feistel(mensaje, clave, rondas)
        descifrado = feistel(cifrado, clave, rondas, descifrar=True)
        self.assertEqual(mensaje, descifrado)

    def test_codificar_mensaje_con_rondas_cero(self):
        mensaje = "Mensaje con rondas cero"
        clave = "clave"
        rondas = 0
        cifrado = feistel(mensaje, clave, rondas)
        descifrado = feistel(cifrado, clave, rondas, descifrar=True)
        self.assertEqual(mensaje, descifrado)

if __name__ == '__main__':
    unittest.main()
