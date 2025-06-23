import numpy as np
from config.constantes import TAM_ALFABETO, CARACTER_RELLENO

def inverso_modular(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def validar_clave(matriz: np.ndarray):
    if matriz.shape[0] != matriz.shape[1]:
        return False, "La matriz clave no es cuadrada."
    determinante = int(round(np.linalg.det(matriz))) % TAM_ALFABETO
    if inverso_modular(determinante, TAM_ALFABETO) is None:
        return False, "La matriz no es invertible módulo 26."
    return True, "Clave válida."

def texto_a_numeros(texto):
    return [ord(c.upper()) - ord('A') for c in texto if c.isalpha()]

def numeros_a_texto(numeros):
    return ''.join(chr(n % TAM_ALFABETO + ord('A')) for n in numeros)

def rellenar_texto(texto, tam_bloque):
    resto = len(texto) % tam_bloque
    if resto != 0:
        texto += CARACTER_RELLENO * (tam_bloque - resto)
    return texto

def cifrar_hill(texto, clave):
    es_valida, mensaje = validar_clave(clave)
    if not es_valida:
        raise ValueError(mensaje)

    tam_bloque = clave.shape[0]
    texto = ''.join(filter(str.isalpha, texto.upper()))
    largo_original = len(texto)
    texto = rellenar_texto(texto, tam_bloque)
    numeros = texto_a_numeros(texto)

    texto_cifrado = []
    for i in range(0, len(numeros), tam_bloque):
        bloque = numeros[i:i+tam_bloque]
        if len(bloque) < tam_bloque:
            bloque += [ord(CARACTER_RELLENO) - ord('A')] * (tam_bloque - len(bloque))
        bloque = np.array(bloque).reshape((tam_bloque, 1))
        resultado = np.dot(clave, bloque) % TAM_ALFABETO
        texto_cifrado.extend(resultado.flatten())

    texto_cifrado = numeros_a_texto(texto_cifrado)
    largo_str = str(largo_original).zfill(3)
    return largo_str + texto_cifrado

def descifrar_hill(texto_cifrado, clave):
    es_valida, mensaje = validar_clave(clave)
    if not es_valida:
        raise ValueError(mensaje)

    try:
        largo_original = int(texto_cifrado[:3])
        texto_cifrado = texto_cifrado[3:]
    except ValueError:
        raise ValueError("El texto cifrado no contiene información del largo original.")

    determinante = int(round(np.linalg.det(clave))) % TAM_ALFABETO
    inverso = inverso_modular(determinante, TAM_ALFABETO)

    adjunta = np.round(np.linalg.inv(clave) * np.linalg.det(clave)).astype(int)
    clave_inversa = (inverso * adjunta) % TAM_ALFABETO

    tam_bloque = clave.shape[0]
    numeros = texto_a_numeros(texto_cifrado)

    texto_descifrado = []
    for i in range(0, len(numeros), tam_bloque):
        bloque = np.array(numeros[i:i+tam_bloque]).reshape((tam_bloque, 1))
        resultado = np.dot(clave_inversa, bloque) % TAM_ALFABETO
        texto_descifrado.extend(resultado.flatten())

    texto_final = numeros_a_texto(texto_descifrado)
    return texto_final[:largo_original]

def hill(mensaje: str, clave: np.ndarray, descifrar: bool = False) -> str:
    """
    Cifra o descifra un mensaje usando el cifrado Hill con la clave proporcionada.
    El largo original del mensaje se codifica dentro del mensaje cifrado.

    Args:
        mensaje (str): El mensaje a cifrar o descifrar.
        clave (np.ndarray): La matriz clave para el cifrado/descifrado.
        descifrar (bool): Si es True, se descifra el mensaje; si es False, se cifra.

    Returns:
        str: El mensaje cifrado o descifrado.
    """
    if descifrar:
        return descifrar_hill(mensaje, clave)
    return cifrar_hill(mensaje, clave)
