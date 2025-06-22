import unittest
from encriptado import (
    texto_a_binario,
    binario_a_texto,
    xor,
    ronda_feistel,
    feistel_cifra_binarios,
    feistel_descifra_binarios,
    generar_keys
)

class TestFuncionesFeistel(unittest.TestCase):

    def test_texto_a_binario_y_viceversa(self):
        texto = "Hola"
        binario = texto_a_binario(texto)
        self.assertEqual(binario_a_texto(binario), texto)

    def test_xor_basico(self):
        a = "1100"
        b = "1010"
        esperado = "0110"
        self.assertEqual(xor(a, b), esperado)

    def test_ronda_feistel(self):
        left = "10101010"
        right = "01010101"
        key = "11110000"
        new_left, new_right = ronda_feistel(left, right, key)
        self.assertEqual(new_left, right)
        self.assertEqual(new_right, xor(left, xor(right, key)))

    def test_feistel_cifra_y_descifra(self):
        texto = "Test"
        binary_data = texto_a_binario(texto)
        rounds = 4
        keys = generar_keys(rounds)
        cifrado = feistel_cifra_binarios(binary_data, rounds, keys)
        descifrado = feistel_descifra_binarios(cifrado, rounds, keys)
        self.assertEqual(descifrado, binary_data)
        self.assertEqual(binario_a_texto(descifrado), texto)

    def test_generar_keys_formato(self):
        keys = generar_keys(3, key_length=8)
        self.assertEqual(len(keys), 3)
        for key in keys:
            self.assertTrue(len(key) == 8)
            self.assertTrue(all(bit in "01" for bit in key))

if __name__ == '__main__':
    unittest.main()
