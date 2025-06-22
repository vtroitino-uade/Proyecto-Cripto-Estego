"""
Módulo de interfaz gráfica para la sección de encriptación.
"""

import tkinter.filedialog as fd
import tkinter.messagebox as mb
import customtkinter as ctk

from encriptado import cesar, vigenere

CIFRADOS = ("César", "Vigenère")
ALFABETOS = {
    "Español": "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",
    "Inglés": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "ASCII": "",
    "Personalizado": ""
}

def _actualizar_alfabeto(seleccion, entrada_alfabeto_personalizado):
    """
    Actualiza el estado del campo de entrada de alfabeto personalizado
    """
    estado = "normal" if seleccion == "Personalizado" else "disabled"
    entrada_alfabeto_personalizado.configure(state=estado)
    print(f"Usando alfabeto: {seleccion}")

def _procesar_cesar(mensaje: str, clave: str, modo: bool, alfabeto_seleccionado: str):
    """
    Procesa el cifrado o descifrado usando el método César.
    """
    if not clave.isdigit():
        raise ValueError("La clave debe ser un número entero.")

    clave = int(clave)
    alfabeto = ALFABETOS[alfabeto_seleccionado]

    return cesar(mensaje, clave, modo, alfabeto)

def _procesar_encriptados(mensaje: str, clave: str, metodo: str, modo: bool, alfabeto_seleccionado: str):
    """
    Lógica principal de cifrado/descifrado sin interacción con la interfaz.
    """
    if metodo == "César":
        return _procesar_cesar(mensaje, clave, modo, alfabeto_seleccionado)
    elif metodo == "Vigenère":
        return vigenere(mensaje, clave, modo, alfabeto_seleccionado)

def _validar(mensaje: str, clave: str, metodo: str, modo: str, alfabeto_personalizado: str, alfabeto_seleccionado: str, mensaje_resultado: ctk.CTkTextbox):
    """
    Valida la entrada del usuario y ejecuta el cifrado o descifrado
    """
    try:
        if metodo not in CIFRADOS:
            raise ValueError("Método no soportado.")

        if not mensaje or not clave:
            raise ValueError("El mensaje y la clave no pueden estar vacíos.")

        if alfabeto_seleccionado == "Personalizado":
            ALFABETOS["Personalizado"] = alfabeto_personalizado.upper()

        resultado = _procesar_encriptados(
            mensaje,
            clave,
            metodo,
            bool(modo),
            alfabeto_seleccionado
        )
        mensaje_resultado.configure(state="normal")
        mensaje_resultado.delete("0.0", "end")
        mensaje_resultado.insert("0.0", resultado)
        mensaje_resultado.configure(state="disabled")
    except ValueError as e:
        mb.showerror("Error", e)

def cargar_archivo(entrada_mensaje: ctk.CTkTextbox) -> None:
    """
    Carga el contenido de un archivo de texto en el campo de entrada de mensaje.
    """
    ruta_archivo = fd.askopenfilename(
        title="Seleccionar archivo de texto",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if ruta_archivo:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            entrada_mensaje.delete("0.0", "end")
            entrada_mensaje.insert("0.0", contenido)
            print(f"Archivo cargado: {ruta_archivo}")

def mostrar_layout_encriptado(ventana: ctk.CTkFrame) -> None:
    """
    Muestra el layout de la sección de encriptación en la ventana principal.

    Args:
        ventana (CTkFrame): Ventana donde se cargará el layout de encriptación.
    """
    frame_principal = ctk.CTkFrame(ventana)
    frame_principal.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
    frame_principal.grid_columnconfigure(0, weight=1)

    opciones_encriptado = ctk.CTkOptionMenu(frame_principal, values=CIFRADOS)
    opciones_encriptado.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    entrada_clave = ctk.CTkEntry(frame_principal, placeholder_text="Clave")
    entrada_clave.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

    opciones_alfabeto = ctk.CTkOptionMenu(
        frame_principal,
        values=list(ALFABETOS.keys()),
        command=lambda seleccion: _actualizar_alfabeto(
            seleccion,
            entrada_alfabeto_personalizado
        )
    )
    opciones_alfabeto.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

    entrada_alfabeto_personalizado = ctk.CTkEntry(
        frame_principal,
        placeholder_text="Alfabeto personalizado",
        state="disabled"
    )
    entrada_alfabeto_personalizado.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

    frame_accion = ctk.CTkFrame(frame_principal)
    frame_accion.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
    frame_accion.grid_columnconfigure(0, weight=1)
    frame_accion.grid_columnconfigure(1, weight=1)

    opcion_accion = ctk.IntVar(value=0)
    radio_cifrar = ctk.CTkRadioButton(
        frame_accion,
        text="Cifrar",
        variable=opcion_accion,
        value=0
    )
    radio_cifrar.invoke()
    radio_cifrar.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    radio_descifrar = ctk.CTkRadioButton(
        frame_accion,
        text="Descifrar",
        variable=opcion_accion,
        value=1
    )
    radio_descifrar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    frame_mensaje = ctk.CTkFrame(ventana)
    frame_mensaje.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

    label_mensaje = ctk.CTkLabel(frame_mensaje, text="Mensaje Original")
    label_mensaje.pack(pady=(10,0))

    frame_resultado = ctk.CTkFrame(ventana)
    frame_resultado.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")

    label_resultado = ctk.CTkLabel(frame_resultado, text="Resultado")
    label_resultado.pack(pady=(10,0))

    entrada_mensaje = ctk.CTkTextbox(
        frame_mensaje,
        height=200,
        fg_color="#343638",
        border_color="#565B5E",
        border_width=2
    )
    entrada_mensaje.pack(expand=True, fill="both", padx=10, pady=10)
    mensaje_resultado = ctk.CTkTextbox(
        frame_resultado,
        height=200,
    )
    mensaje_resultado.pack(expand=True, fill="both", padx=10, pady=10)

    boton_encriptar = ctk.CTkButton(
        frame_principal,
        text="Ejecutar",
        command=lambda: _validar(
            entrada_mensaje.get("0.0", "end-1c"),
            entrada_clave.get(),
            opciones_encriptado.get(),
            opcion_accion.get(),
            entrada_alfabeto_personalizado.get(),
            ALFABETOS[opciones_alfabeto.get()],
            mensaje_resultado
        )
    )
    boton_encriptar.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

    boton_cargar = ctk.CTkButton(
        frame_principal,
        text="Cargar archivo",
        command=lambda: cargar_archivo(
            entrada_mensaje
        )
    )
    boton_cargar.grid(row=6, column=0, padx=20, pady=10, sticky="ew")
