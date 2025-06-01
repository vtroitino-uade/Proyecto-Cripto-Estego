"""
Módulo de la tecnica LSB Matching para ocultar y extraer mensajes en imágenes.
"""

from PIL import Image

def codificar_lsb_matching(imagen: Image.Image, mensaje: str) -> Image.Image:
    """
    Codifica un mensaje en una imagen utilizando la técnica LSB Matching.

    Args:
        imagen (Image): La imagen en la que se ocultará el mensaje. Debe ser un objeto de la clase Image de PIL.
        mensaje (str | None): El mensaje a ocultar en la imagen.

    Returns:
        Image: Devuelve la imagen con el mensaje oculto.

    """

def decodificar_lsb_matching(imagen: Image.Image) -> str:
    """
    Decodifica un mensaje oculto en una imagen utilizando la técnica LSB Matching.

    Args:
        imagen (Image): La imagen en la que se extraerá el mensaje. Debe ser un objeto de la clase Image de PIL.

    Returns:
        str: Devuelve el mensaje extraído de la imagen.
    """

def lsb_matching(imagen: Image.Image, mensaje: str | None = None) -> Image.Image | str:
    """
    Oculta o extrae un mensaje en una imagen utilizando la técnica 
    LSB (Least Significant Bit) Matching.

    Formatos de imagen soportados:
    - JPEG (.jpg, .jpeg)
    - PNG (.png)
    - BMP (.bmp)
    - GIF (.gif)
    - PPM (.ppm)

    Args:
        imagen (Image): La imagen en la que se ocultará o de la que se extraerá el mensaje. Debe ser un objeto de la clase Image de PIL.
        mensaje (str | None): El mensaje a ocultar en la imagen. Si es None, se extraerá el mensaje de la imagen.

    Returns:
        (Image | str): Si se proporciona un mensaje, devuelve la imagen con el mensaje oculto. Si no se proporciona un mensaje, devuelve el mensaje extraído de la imagen.

    Raises:
        ValueError: Si el mensaje es demasiado largo para ocultarlo en la imagen.
    """
