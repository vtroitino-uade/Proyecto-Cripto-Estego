import customtkinter as ctk

from interfaz.layout_encriptado import mostrar_layout_encriptado
from interfaz.layout_estego import mostrar_layout_estego

def cargar_layout(nombre_tab: str, ventana: ctk.CTkFrame) -> None:
    """
    Carga el layout correspondiente al nombre del tab.

    Args:
        nombre_tab (str): Nombre del tab a cargar.
        ventana (CTkFrame): Ventana donde se cargará el layout.

    Raises:
        ValueError: Si el nombre del tab no es reconocido.
    """
    if nombre_tab == "Encriptación":
        mostrar_layout_encriptado(ventana)
    elif nombre_tab == "Esteganografía":
        mostrar_layout_estego(ventana)
