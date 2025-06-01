"""
Módulo de la tecnica LSB Matching para ocultar y extraer mensajes en imágenes.
"""

from PIL import Image
from config.constantes import BYTE, DELIMITADOR

def convertir_a_bits(mensaje_bytes: bytes) -> list[int]:
    """
    Convierte un mensaje de bytes a una lista de números enteros representando sus bits.

    Args:
        mensaje_bytes (bytes): El mensaje de bytes a convertir. 

    Returns:
        list[int]: Lista de bits representando la cadena de bytes.
    """
    return [int(bit) for byte in mensaje_bytes for bit in f"{byte:08b}"]

def _codificar_lsb(imagen: Image.Image, mensaje_bytes: bytes) -> Image.Image:
    """
    Codifica un mensaje en una imagen utilizando la técnica LSB Matching.

    Args:
        imagen (Image): La imagen en la que se ocultará el mensaje. \
        Debe ser un objeto de la clase Image de PIL.
        mensaje_bytes (bytes): El mensaje a ocultar en la imagen.

    Returns:
        Image: Devuelve la imagen con el mensaje oculto.
    """

def _decodificar_lsb(imagen: Image.Image) -> str:
    """
    Decodifica un mensaje oculto en una imagen utilizando la técnica LSB Matching.

    Args:
        imagen (Image): La imagen en la que se extraerá el mensaje. \
        Debe ser un objeto de la clase Image de PIL.

    Returns:
        str: Devuelve el mensaje extraído de la imagen.
    """

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

    if DELIMITADOR in mensaje:
        mensaje = mensaje.replace(DELIMITADOR, '')

    ancho, alto = imagen.size
    cantidad_canales = len(imagen.getbands())
    longitud_maxima = (ancho * alto * cantidad_canales) // BYTE
    mensaje = mensaje + DELIMITADOR
    mensaje_bytes = mensaje.encode('utf-8')
    longitud_mensaje = len(mensaje_bytes)

    if longitud_mensaje > longitud_maxima:
        raise ValueError(f"El mensaje debe ser menor o igual a {longitud_maxima} caracteres. \
                         O la imagen es demasiado pequeña para ocultar el mensaje.")

    return _codificar_lsb(imagen, mensaje_bytes)
