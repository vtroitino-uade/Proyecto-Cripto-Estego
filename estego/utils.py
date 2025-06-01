"""
Módulo de funciones útiles para la esteganografia.
"""

from PIL import Image

def cargar_imagen(ruta: str) -> Image.Image:
    """
    Carga una imagen y la converte a RGB o RGBA según su extensión.

    Args:
        ruta (str): Ruta de la imagen a cargar.
    
    Returns:
        Image.Image: Imagen en modo RGB o RGBA.
    """
    with Image.open(ruta) as archivo_imagen:
        modo = "".join(archivo_imagen.getbands())
        return archivo_imagen.convert(modo)

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
