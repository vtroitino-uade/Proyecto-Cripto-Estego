"""
Módulo para cifrado y descifrado XOR.
"""

import base64

def xor(mensaje: str, clave: str, descifrar: bool = False) -> str:
    """
    Cifra o descifra un mensaje usando el cifrado XOR.
    El mensaje se codifica o decodifica en formato base64 para asegurar \
    que todos los caracteres sean imprimibles.

    Args:
        mensaje (str): El mensaje a cifrar o descifrar.
        clave (str): La clave para el cifrado o descifrado.
        descifrar (bool): Si es True, descifra el mensaje; si es False, lo cifra.

    Returns:
        str: El mensaje cifrado en o descifrado en formato base64.

    Raises:
        ValueError: Si la clave está vacía.
    """
    if not clave:
        raise ValueError("La clave no puede estar vacía.")

    if descifrar:
        mensaje_bytes = base64.b64decode(mensaje)
    else:
        mensaje_bytes = mensaje.encode('utf-8')

    clave_bytes = clave.encode('utf-8')
    resultado_bytes = bytes([m ^ clave_bytes[i % len(clave_bytes)] for i, m in enumerate(mensaje_bytes)])
    return resultado_bytes.decode('utf-8') if descifrar else base64.b64encode(resultado_bytes).decode('utf-8')
