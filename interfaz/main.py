import customtkinter as ctk

from interfaz.layout_encriptado import mostrar_layout_encriptado
from interfaz.layout_estego import mostrar_layout_estego

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
        mostrar_layout_encriptado(ventana)
    elif nombre_tab == "Esteganografía":
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
