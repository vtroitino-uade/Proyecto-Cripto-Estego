import customtkinter as ctk
from interfaz.layout import cargar_layout

def _iniciar_app() -> ctk.CTk:    
    app = ctk.CTk()
    app.geometry("800x400")
    app.title("Cripto/Estego")

    tabs = ctk.CTkTabview(
        app,
        command=lambda nombre_tab: cargar_layout(nombre_tab, tabs.tab(nombre_tab))
    )
    tabs.pack(expand=True, fill="both", padx=20, pady=20)

    tabs.add("Encriptación")
    tabs.add("Esteganografía")
    tab_actual = tabs.get()
    ventana_tab = tabs.tab(tab_actual)

    cargar_layout(tab_actual, ventana_tab)

    return app

app = _iniciar_app()
