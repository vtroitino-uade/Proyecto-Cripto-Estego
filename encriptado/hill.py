import numpy as np

from config.constantes import TAM_ALFABETO, CARACTER_RELLENO

def inverso_modular(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def validar_clave(matriz):
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

def cifrar(texto, clave):
    es_valida, mensaje = validar_clave(clave)
    if not es_valida:
        raise ValueError(mensaje)

    tam_bloque = clave.shape[0]
    texto = rellenar_texto(texto, tam_bloque)
    numeros = texto_a_numeros(texto)

    texto_cifrado = []
    for i in range(0, len(numeros), tam_bloque):
        bloque = np.array(numeros[i:i+tam_bloque]).reshape((tam_bloque, 1))
        resultado = np.dot(clave, bloque) % TAM_ALFABETO
        texto_cifrado.extend(resultado.flatten())

    return numeros_a_texto(texto_cifrado)

def descifrar(texto_cifrado, clave, largo_original=None):
    es_valida, mensaje = validar_clave(clave)
    if not es_valida:
        raise ValueError(mensaje)

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
    return texto_final if largo_original is None else texto_final[:largo_original]

def hill(mensaje: str, clave: np.ndarray, descifrar: bool = False) -> str:
    """
    Cifra o descifra un mensaje usando el cifrado Hill con la clave proporcionada.

    Args:
        mensaje (str): El mensaje a cifrar o descifrar.
        clave (np.ndarray): La matriz clave para el cifrado/descifrado.
        descifrar (bool): Si es True, se descifra el mensaje; si es False, se cifra.

    Returns:
        str: El mensaje cifrado o descifrado.
    """

# ---------------------------------------
# FUNCIÓN PRINCIPAL PARA USO INTERACTIVO
# ---------------------------------------
# def main():
#     import sys

#     print("=== CIFRADO HILL ===")
#     opcion = input("¿Desea cifrar (C) o descifrar (D)? ").strip().upper()

#     if opcion not in ('C', 'D'):
#         print("Opción inválida.")
#         sys.exit()

#     texto = input("Ingrese el texto: ").strip()

#     tipo = int(input("¿Clave 2x2 (2) o 3x3 (3)?: ").strip())
#     if tipo == 2:
#         print("Ingrese la clave 2x2 (4 números en total):")
#         valores = [int(input(f"Elemento {i+1}: ")) for i in range(4)]
#         clave = np.array(valores).reshape((2, 2))
#     elif tipo == 3:
#         print("Ingrese la clave 3x3 (9 números en total):")
#         valores = [int(input(f"Elemento {i+1}: ")) for i in range(9)]
#         clave = np.array(valores).reshape((3, 3))
#     else:
#         print("Tamaño de matriz no válido.")
#         sys.exit()

#     if opcion == 'C':
#         resultado = cifrar(texto, clave)
#         print(" Texto cifrado:", resultado)
#     else:
#         resultado = descifrar(texto, clave)
#         print(" Texto descifrado:", resultado)