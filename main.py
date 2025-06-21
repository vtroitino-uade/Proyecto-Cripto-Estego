import tkinter.filedialog as fd
import customtkinter as ctk
from encriptado import cesar, vigenere

from interfaz import app

CIFRADOS = ("César", "Vigenère")
ALFABETOS = {
    "Español": "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",
    "Inglés": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "ASCII": "",
    "Personalizado": ""
}

def actualizar_alfabeto(seleccion):
    """
    Actualiza el estado del campo de entrada de alfabeto personalizado
    """
    estado = "normal" if seleccion == "Personalizado" else "disabled"
    entrada_alfabeto_personalizado.configure(state=estado)
    print(f"Usando alfabeto: {seleccion}")

def validar():
    """
    Valida la entrada del usuario y ejecuta el cifrado o descifrado
    """
    ALFABETOS["Personalizado"] = entrada_alfabeto_personalizado.get().upper()
    opcion_encriptado = opciones_encriptado.get()
    mensaje = entrada_mensaje.get("0.0", "end-1c")
    clave = entrada_clave.get()
    opcion_descifrado = opcion_accion.get()
    opcion_alfabeto = ALFABETOS[opciones_alfabeto.get()]

    if clave == "":
        print("La clave no puede estar vacía.")
        return

    if opcion_encriptado == "César":
        if not clave.isdigit() and not clave.startswith("-"):
            print("La clave debe ser un número entero.")
            return
        clave = int(entrada_clave.get())
        resultado = cesar(mensaje, clave, opcion_descifrado, opcion_alfabeto)

    elif opcion_encriptado == "Vigenère":
        clave = entrada_clave.get()
        resultado = vigenere(mensaje, clave, opcion_descifrado, opcion_alfabeto)

    mensaje_resultado.configure(state="normal")
    mensaje_resultado.delete("0.0", "end")
    mensaje_resultado.insert("0.0", resultado)
    mensaje_resultado.configure(state="disabled")

def cargar_archivo():
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

if __name__ == "__main__":

    app.mainloop()

    # app = ctk.CTk()
    # app.title("Encriptador")
    # app.geometry("800x400")
    # app.grid_rowconfigure(0, weight=1)
    # app.grid_columnconfigure(0, weight=1)
    # app.grid_columnconfigure(1, weight=0)
    # app.grid_columnconfigure(2, weight=1)

    # frame_principal = ctk.CTkFrame(app)
    # frame_principal.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
    # frame_principal.grid_columnconfigure(0, weight=1)

    # opciones_encriptado = ctk.CTkOptionMenu(frame_principal, values=CIFRADOS)
    # opciones_encriptado.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    # entrada_clave = ctk.CTkEntry(frame_principal, placeholder_text="Clave")
    # entrada_clave.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

    # opciones_alfabeto = ctk.CTkOptionMenu(
    #     frame_principal,
    #     values=list(ALFABETOS.keys()),
    #     command=actualizar_alfabeto
    # )
    # opciones_alfabeto.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

    # entrada_alfabeto_personalizado = ctk.CTkEntry(
    #     frame_principal,
    #     placeholder_text="Alfabeto personalizado",
    #     state="disabled"
    # )
    # entrada_alfabeto_personalizado.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

    # frame_accion = ctk.CTkFrame(frame_principal)
    # frame_accion.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
    # frame_accion.grid_columnconfigure(0, weight=1)
    # frame_accion.grid_columnconfigure(1, weight=1)

    # opcion_accion = ctk.IntVar(value=0)
    # radio_cifrar = ctk.CTkRadioButton(
    #     frame_accion,
    #     text="Cifrar",
    #     variable=opcion_accion,
    #     value=0
    # )
    # radio_cifrar.invoke()
    # radio_cifrar.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    # radio_descifrar = ctk.CTkRadioButton(
    #     frame_accion,
    #     text="Descifrar",
    #     variable=opcion_accion,
    #     value=1
    # )
    # radio_descifrar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    # boton_encriptar = ctk.CTkButton(frame_principal, text="Ejecutar", command=validar)
    # boton_encriptar.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

    # boton_cargar = ctk.CTkButton(frame_principal, text="Cargar archivo", command=cargar_archivo)
    # boton_cargar.grid(row=6, column=0, padx=20, pady=10, sticky="ew")

    # frame_mensaje = ctk.CTkFrame(app)
    # frame_mensaje.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

    # frame_resultado = ctk.CTkFrame(app)
    # frame_resultado.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")

    # label_mensaje = ctk.CTkLabel(frame_mensaje, text="Mensaje Original")
    # label_mensaje.pack(pady=(10,0))

    # label_resultado = ctk.CTkLabel(frame_resultado, text="Resultado")
    # label_resultado.pack(pady=(10,0))

    # entrada_mensaje = ctk.CTkTextbox(
    #     frame_mensaje,
    #     height=200,
    #     fg_color="#343638",
    #     border_color="#565B5E",
    #     border_width=2
    # )
    # entrada_mensaje.pack(expand=True, fill="both", padx=10, pady=10)
    # mensaje_resultado = ctk.CTkTextbox(
    #     frame_resultado,
    #     height=200,
    # )
    # mensaje_resultado.pack(expand=True, fill="both", padx=10, pady=10)
