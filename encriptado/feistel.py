def texto_a_binario(text):
    """Convierte texto a binario"""
    return ''.join(format(ord(c), '08b') for c in text)

def binario_a_texto(binary):
    """Convierte binario a texto"""
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def xor(bin_str1, bin_str2):
    """Realiza XOR entre dos cadenas binarias del mismo tamaño"""
    return ''.join('1' if a != b else '0' for a, b in zip(bin_str1, bin_str2))

def ronda_feistel(left, right, key):
    """Aplica una ronda Feistel"""
    f_output = xor(right, key)  
    new_left = right
    new_right = xor(left, f_output)
    return new_left, new_right

def feistel_cifra_binarios(binary_data, rounds, keys):
    """Cifra datos binarios usando red Feistel"""
    half = len(binary_data) // 2
    left, right = binary_data[:half], binary_data[half:]

    for i in range(rounds):
        left, right = ronda_feistel(left, right, keys[i])
    return left + right  

def feistel_descifra_binarios(cipher_binary, rounds, keys):
    """Descifra datos binarios cifrados con red Feistel"""
    half = len(cipher_binary) // 2
    left, right = cipher_binary[:half], cipher_binary[half:]

    for i in reversed(range(rounds)):
        right, left = ronda_feistel(right, left, keys[i])
    return left + right

def generar_keys(rounds, key_length=8):
    """Genera claves simples (aleatorias o fijas) para cada ronda"""
    import random
    return [format(random.randint(0, 2**key_length - 1), f'0{key_length}b') for _ in range(rounds)]