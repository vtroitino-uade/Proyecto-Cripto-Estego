"""
Módulo de la tecnica LSB Matching para ocultar y extraer mensajes en imágenes.
"""

import random
from PIL import Image
from config.constantes import BYTE, DELIMITADOR
from estego.utils import convertir_a_bits, imagen_a_bytes

def _codificar_lsb(imagen: Image.Image, mensaje_bits: list[int]) -> Image.Image:
    """
    Codifica un mensaje en una imagen utilizando la técnica LSB Matching.

    Args:
        imagen (Image): La imagen en la que se ocultará el mensaje. \
        Debe ser un objeto de la clase Image de PIL.
        mensaje_bits (list[int]): El mensaje a ocultar en la imagen.

    Returns:
        Image: Devuelve la imagen con el mensaje oculto.
    """
    imagen_bytes = imagen_a_bytes(imagen)
    imagen_bytes_estego = imagen_bytes.copy()

    for i, mensaje_bit in enumerate(mensaje_bits):
        imagen_byte = imagen_bytes[i]
        if imagen_byte % 2 != mensaje_bit:
            if imagen_byte == 255:
                imagen_byte -= 1
            elif imagen_byte == 0:
                imagen_byte += 1
            else:
                imagen_byte += random.choice((1, -1))

            imagen_bytes_estego[i] = imagen_byte

    return Image.frombytes(
        mode=imagen.mode,
        size=imagen.size,
        data=bytes(imagen_bytes_estego)
    )

def _decodificar_lsb(imagen: Image.Image) -> str:
    """
    Decodifica un mensaje oculto en una imagen utilizando la técnica LSB Matching.

    Args:
        imagen (Image): La imagen en la que se extraerá el mensaje. \
        Debe ser un objeto de la clase Image de PIL.

    Returns:
        str: Devuelve el mensaje extraído de la imagen.

    Raises:
        ValueError: Si no se encuentra el delimitador de fin de mensaje.
        UnicodeDecodeError: Si la conversión de bytes a texto falla.
    """
    imagen_bytes = imagen_a_bytes(imagen)
    mensaje_lsb = [byte % 2 for byte in imagen_bytes]
    mensaje_util = bytearray()
    delimitador_bytes = DELIMITADOR.encode("utf-8")

    for i in range(0, len(mensaje_lsb), BYTE):
        byte_bits = mensaje_lsb[i:i + BYTE]
        if len(byte_bits) < BYTE:
            break

        byte = int("".join(map(str, byte_bits)), base=2)
        mensaje_util.append(byte)

        if mensaje_util[-len(delimitador_bytes):] == delimitador_bytes:
            return mensaje_util[:-len(delimitador_bytes)].decode("utf-8")

    raise ValueError(
        "La imagen no contiene un mensaje oculto detectable. "
        "Verifique que la imagen haya sido previamente codificada con LSB Matching "
        "y que no haya sido alterada."
    )

def lsb_matching(imagen: Image.Image, mensaje: str | None = None) -> str | Image.Image:
    """
    Oculta o extrae un mensaje en una imagen utilizando la técnica 
    LSB (Least Significant Bit) Matching.

    Formatos de imagen soportados:
    - JPEG (.jpg, .jpeg)
    - PNG (.png)
    - BMP (.bmp)
    - PPM (.ppm)

    Args:
        imagen (Image): La imagen en la que se ocultará o de la que se extraerá el mensaje. \
        Debe ser un objeto de la clase Image de PIL.
        mensaje (str | None): El mensaje a ocultar en la imagen. \
        Si es None, se extraerá el mensaje de la imagen.

    Returns:
        (str | Image): Si no se proporciona un mensaje, devuelve el mensaje extraído de la imagen. \
        Si se proporciona un mensaje, devuelve la imagen con el mensaje oculto.

    Raises:
        ValueError: Si el mensaje es demasiado largo para ocultarlo en la imagen.
    """

    if mensaje is None:
        return _decodificar_lsb(imagen)

    mensaje = " ".join(parte.strip() for parte in mensaje.split(DELIMITADOR)).strip()

    ancho, alto = imagen.size
    cantidad_bandas = len(imagen.getbands())
    longitud_maxima = (ancho * alto * cantidad_bandas) // BYTE
    mensaje += DELIMITADOR
    mensaje_bytes = mensaje.encode('utf-8')
    longitud_mensaje = len(mensaje_bytes)

    if longitud_mensaje > longitud_maxima:
        raise ValueError(
            f"El mensaje debe ser menor o igual a {longitud_maxima} caracteres."
            "O la imagen es demasiado pequeña para ocultar el mensaje."
        )

    mensaje_bits = convertir_a_bits(mensaje_bytes)
    return _codificar_lsb(imagen, mensaje_bits)
