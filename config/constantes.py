"""
Modulo de constantes del proyecto.
"""

BYTE = 8  # Cantidad de bits en un byte
RGB = 3  # Cantidad de canales de color en una imagen RGB
DELIMITADOR = "<F>"  # Delimitador para el final del mensaje oculto en la imagen

# Constantes para el cifrado Hill
TAM_ALFABETO = 26  # Tamaño del alfabeto (A-Z)
CARACTER_RELLENO = "X" # Carácter de relleno para completar bloques en el cifrado Hill

# Constantes para el cifrado Feistel
TAM_BLOQUE = 16 # Tamaño del bloque en bytes para el cifrado Feistel
TAM_MEDIO_BLOQUE = TAM_BLOQUE // 2

ASCII_IMPRIMIBLES = "".join(chr(x) for x in range(32, 127)) # Caracteres ASCII imprimibles
