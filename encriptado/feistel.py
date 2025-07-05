import base64
from config.constantes import TAM_BLOQUE, TAM_MEDIO_BLOQUE, CARACTER_RELLENO

def _xor_feistel(bloque: bytes, subclave: bytes) -> bytes:
    return bytes(c ^ k for c, k in zip(bloque, subclave))

def _generar_bloques(mensaje_bytes: bytes, clave_bytes: bytes, rondas: int) -> tuple[list[bytes], list[bytes], int]:
    bloques_mensaje = []
    bloques_clave = []

    for i in range(0, len(mensaje_bytes), TAM_BLOQUE):
        bloque = mensaje_bytes[i:i+TAM_BLOQUE]
        bloque = bloque.ljust(TAM_BLOQUE, CARACTER_RELLENO.encode())
        bloques_mensaje.append(bloque)

    tam_ultimo_bloque = len(mensaje_bytes) % TAM_BLOQUE
    relleno = TAM_BLOQUE - tam_ultimo_bloque

    for i in range(rondas):
        tam_clave = len(clave_bytes)
        inicio = (i * TAM_MEDIO_BLOQUE) % tam_clave
        fin = inicio + TAM_MEDIO_BLOQUE

        if fin <= tam_clave:
            subclave = clave_bytes[inicio:fin]
        else:
            l = clave_bytes[inicio:]
            r = clave_bytes[:fin - tam_clave]
            subclave = l + r

        subclave = subclave.ljust(TAM_MEDIO_BLOQUE, CARACTER_RELLENO.encode())
        bloques_clave.append(subclave)

    return bloques_mensaje, bloques_clave, relleno

def _feistel_bloque(bloque: bytes, subclaves: list[bytes]) -> bytes:
    l = bloque[:TAM_MEDIO_BLOQUE]
    r = bloque[TAM_MEDIO_BLOQUE:]

    for k in subclaves:
        nuevo_r = _xor_feistel(l, _xor_feistel(r, k))
        l, r = r, nuevo_r

    return r + l

def feistel(mensaje: str, clave: str, rondas: int, descifrar: bool = False) -> str:
    """
    Cifra o descifra un mensaje usando la red Feistel.

    Args:
        mensaje (str): El mensaje a cifrar o descifrar.
        clave (str): La clave para el cifrado o descifrado.
        rondas (int): Número de rondas de cifrado.
    Returns:
        str: El mensaje cifrado o descifrado en formato base64.
    Raises:
        ValueError: Si el mensaje no está en el formato esperado para descifrar.
    """

    if descifrar:
        try:
            mensaje, relleno_a_eliminar = mensaje.rsplit(":", 1)
            relleno_a_eliminar = int(relleno_a_eliminar)
            mensaje_bytes = base64.b64decode(mensaje)
        except ValueError as e:
            raise ValueError("Formato de mensaje inválido para descifrar (esperaba 'base64:relleno')") from e
    else:
        mensaje_bytes = mensaje.encode()

    clave_bytes = clave.encode()
    bloques, subclaves, cant_relleno = _generar_bloques(mensaje_bytes, clave_bytes, rondas)

    if descifrar:
        subclaves = subclaves[::-1]

    bloques_cifrados = [
        _feistel_bloque(bloque, subclaves)
        for bloque in bloques
    ]
    resultado = b''.join(bloques_cifrados)

    if descifrar:
        return resultado[:-relleno_a_eliminar].decode()

    return base64.b64encode(resultado).decode() + f":{cant_relleno}"
