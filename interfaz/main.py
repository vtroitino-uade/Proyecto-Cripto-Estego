import customtkinter as ctk

from interfaz.layout_encriptado import mostrar_layout_encriptado
from interfaz.layout_estego import mostrar_layout_estego
from log import logging

def _cargar_layout(nombre_tab: str, ventana: ctk.CTkFrame) -> None:
    """
    Carga el layout correspondiente al nombre del tab.

    Args:
        nombre_tab (str): Nombre del tab a cargar.
        ventana (CTkFrame): Ventana donde se cargará el layout.

    Raises:
        ValueError: Si el nombre del tab no es reconocido.
    """
    if nombre_tab == "Encriptación":
        logging.info("Seleccionando layout de Encriptación")
        mostrar_layout_encriptado(ventana)
    elif nombre_tab == "Esteganografía":
        logging.info("Seleccionando layout de Esteganografía")
        ventana.grid_rowconfigure(0, weight=1)
        ventana.grid_columnconfigure(0, weight=1)
        mostrar_layout_estego(ventana)

def _cargar_interfaz() -> ctk.CTk:
    """
    Crea y configura la ventana principal de la aplicación.

    Returns:
        CTk: Ventana principal de la aplicación.
    """
    interfaz = ctk.CTk()
    interfaz.title("Cripto/Estego")

    tabs = ctk.CTkTabview(interfaz)
    tabs.pack(expand=True, fill="both", padx=20, pady=20)

    tabs.add("Encriptación")
    tabs.add("Esteganografía")

    tabs.configure(
        command=lambda: _cargar_layout(
            tabs.get(),
            tabs.tab(tabs.get())
        )
    )

    tab_actual = tabs.get()
    _cargar_layout(tab_actual, tabs.tab(tab_actual))

    return interfaz

app = _cargar_interfaz()
