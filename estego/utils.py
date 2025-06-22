"""
Módulo de funciones útiles para la esteganografia.
"""

from pathlib import Path
from PIL import Image

def cargar_imagen(ruta: str) -> Image.Image:
    """
    Carga una imagen y la converte a RGB o RGBA según su extensión.

    Args:
        ruta (str): Ruta de la imagen a cargar.
    
    Returns:
        Image.Image: Imagen en modo RGB o RGBA.
    
    Raises:
        FileNotFoundError: Si la ruta especificada no existe.
        ValueError: Si la imagen no es válida o no se puede identificar.
    """
    if not Path.exists(Path(ruta)):
        raise FileNotFoundError(ruta)

    try:
        with Image.open(ruta) as archivo_imagen:
            modo = "".join(archivo_imagen.getbands())
            return archivo_imagen.convert(modo)
    except Image.UnidentifiedImageError as e:
        raise ValueError("La imagen no es válida o no se puede identificar") from e

def guardar_imagen(imagen: Image.Image, ruta_original: str) -> Path:
    """
    Guarda la imagen en la misma carpeta con el mismo formato que tenía originalmente.

    Args:
        imagen (Image.Image): Imagen a guardar. Debe ser un objeto de la clase Image.
        ruta_original (str): Ruta original de la imagen, usada para determinar el formato \
        y nombre del archivo.

    Returns:
        Path: Ruta del archivo guardado.
    """
    ruta = Path(ruta_original)
    formato = (imagen.format or ruta.suffix[1:] or "PNG").upper()

    nombre_salida = f"{ruta.stem}_oculto{ruta.suffix}"
    ruta_salida = ruta.with_name(nombre_salida)

    imagen.save(ruta_salida, format=formato)
    return ruta_salida

def imagen_a_bytes(imagen: Image.Image) -> list[int]:
    """
    Convierte una imagen a una lista de números enteros representando sus bytes.
    
    Args:
        imagen (Image): Imagen a convertir. Debe ser un objeto de la clase Image de PIL.
    
    Returns:
        list[int]: Lista de bytes representando la imagen.
    """
    return [int(byte) for byte in imagen.tobytes()]

def convertir_a_bits(mensaje_bytes: bytes) -> list[int]:
    """
    Convierte un mensaje de bytes a una lista de números enteros representando sus bits.

    Args:
        mensaje_bytes (bytes): El mensaje de bytes a convertir. 

    Returns:
        list[int]: Lista de bits representando la cadena de bytes.
    """
    return [int(bit) for byte in mensaje_bytes for bit in f"{byte:08b}"]
