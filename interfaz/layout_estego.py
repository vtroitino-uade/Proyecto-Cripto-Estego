"""
Módulo de interfaz gráfica para la sección de esteganografía.
"""

import tkinter.filedialog as fd
import tkinter.messagebox as mb
import customtkinter as ctk

from estego.lsb_matching import lsb_matching
from estego.utils import cargar_imagen, guardar_imagen
from log import logger

def _ocultar_mensaje(ruta_imagen: str, mensaje: str):
    """
    Devuelve la imagen con el mensaje oculto en la ruta de la imagen proporcionada.
    Guarda la imagen en la misma carpeta con un nombre modificado.
    """
    imagen = cargar_imagen(ruta_imagen)
    imagen_ocultada = lsb_matching(imagen, mensaje)
    ruta_salida = guardar_imagen(imagen_ocultada, ruta_imagen)
    logger.info("Mensaje oculto con éxito")
    mb.showinfo("Éxito", f"Imagen guardada en: {ruta_salida}")

def _extraer_mensaje(ruta_imagen: str) -> str:
    """
    Devuelve el mensaje oculto en la ruta de la imagen proporcionada.
    """
    imagen = cargar_imagen(ruta_imagen)
    return lsb_matching(imagen)

def _validar(modo: str, ruta: str, mensaje: str, salida: ctk.CTkTextbox):
    try:
        if ruta == "Ninguna imagen seleccionada":
            raise ValueError("Seleccioná una imagen.")

        if modo == "Extraer":
            resultado = _extraer_mensaje(ruta)
            salida.configure(state="normal")
            salida.delete("0.0", "end")
            salida.insert("0.0", resultado)
            salida.configure(state="disabled")
            logger.info("Mensaje extraído con éxito.")
            return

        if not mensaje:
            raise ValueError("Si estás ocultando un mensaje, no puede estar vacío.")

        _ocultar_mensaje(ruta, mensaje)
    except FileNotFoundError as e:
        logger.error("Archivo no encontrado: %s", e)
        mb.showerror("Error", f"Archivo no encontrado: {e}")
    except ValueError as e:
        logger.error(e)
        mb.showerror("Error", f"{e}")

def _seleccionar_imagen(ruta_var: ctk.StringVar):
    ruta = fd.askopenfilename(
        filetypes=[(
            "Imágenes",
            "*.png *.bmp *jpg *.jpeg *.ppm"
        )]
    )
    if ruta:
        logger.info("Imagen cargada: %s", ruta)
        ruta_var.set(f"Imagen cargada: {ruta}")

def _copiar_al_portapapeles(textbox: ctk.CTkTextbox, boton: ctk.CTkButton) -> None:
    contenido = textbox.get("0.0", "end-1c")
    textbox.clipboard_clear()
    textbox.clipboard_append(contenido)
    boton.configure(text="✅", font=("Arial", 15))
    boton.after(2000, lambda: boton.configure(text="📋", font=("Arial", 20)))
    logger.info("Resultado copiado al portapapeles.")

def mostrar_layout_estego(ventana: ctk.CTkFrame):
    """
    Muestra el layout de la sección de esteganografía en la ventana principal.
    """
    frame_principal = ctk.CTkFrame(ventana)
    frame_principal.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
    frame_principal.grid_columnconfigure(0, weight=1)

    ruta_var = ctk.StringVar(value="Ninguna imagen seleccionada")

    ctk.CTkButton(
        frame_principal,
        text="Seleccionar imagen",
        command=lambda: _seleccionar_imagen(ruta_var)
    ).grid(row=1, column=0, padx=20, pady=10, sticky="ew")

    entrada_ruta = ctk.CTkLabel(
        frame_principal,
        textvariable=ruta_var,
        wraplength=400,
        justify="left"
    )
    entrada_ruta.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    entrada_mensaje = ctk.CTkEntry(frame_principal, placeholder_text="Mensaje a ocultar")
    entrada_mensaje.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

    modo_accion = ctk.StringVar(value="Ocultar")
    ctk.CTkRadioButton(
        frame_principal,
        text="Ocultar",
        variable=modo_accion,
        value="Ocultar"
    ).grid(row=3, column=0, padx=20, pady=5, sticky="w")
    ctk.CTkRadioButton(
        frame_principal,
        text="Extraer",
        variable=modo_accion,
        value="Extraer"
    ).grid(row=4, column=0, padx=20, pady=5, sticky="w")

    salida_mensaje = ctk.CTkTextbox(frame_principal, height=100, state="disabled")
    salida_mensaje.grid(row=5, column=0, padx=20, pady=10, sticky="nsew")
    btn_copiar = ctk.CTkButton(
        master=salida_mensaje,
        text="📋",
        width=30,
        font=("Arial", 20),
        fg_color="transparent",
        hover_color="#3a3b3c",
        text_color="#cccccc",
        anchor="center"
    )
    btn_copiar.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
    btn_copiar.configure(command=lambda: _copiar_al_portapapeles(salida_mensaje, btn_copiar))

    boton_ejecutar = ctk.CTkButton(
        frame_principal,
        text="Ejecutar",
        command=lambda: _validar(
            modo_accion.get(),
            ruta_var.get().replace("Imagen cargada: ", ""),
            entrada_mensaje.get(),
            salida_mensaje
        )
    )
    boton_ejecutar.grid(row=6, column=0, padx=20, pady=10, sticky="ew")
