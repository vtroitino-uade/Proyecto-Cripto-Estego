import customtkinter as ctk
from encriptado import cesar, vigenere

CIFRADOS = ("César", "Vigenère")
ALFABETOS = {
    "Español": "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",
    "Inglés": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Unicode": "",
    "Personalizado": ""
}

def actualizar_alfabeto(seleccion):
    estado = "normal" if seleccion == "Personalizado" else "disabled"
    entry_alfabeto_personalizado.configure(state=estado)
    print(f"Usando alfabeto: {seleccion}")

def validar():
    ALFABETOS["Personalizado"] = entry_alfabeto_personalizado.get()
    opcion = opciones_encriptado.get()
    alfabeto = ALFABETOS[opcion]
    mensaje = entrada_mensaje.get()

    if opcion == "César":
        clave = int(entrada_clave.get())
        resultado = cesar(mensaje, clave, False, alfabeto)

    elif opcion == "Vigenère":
        clave = entrada_clave.get()
        resultado = vigenere(mensaje, clave, False, alfabeto)

    mensaje_resultado.configure(text=f"Resultado: {resultado}")

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Codificador/Decodificador")
    app.geometry("500x500")
    app.grid_columnconfigure(0, weight=1)

    opciones_encriptado = ctk.CTkOptionMenu(app, values=CIFRADOS)
    opciones_encriptado.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

    label_calve = ctk.CTkLabel(app, text="Clave", fg_color="transparent")
    entrada_clave = ctk.CTkEntry(app, placeholder_text="Clave")
    entrada_clave.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

    label_alfabeto = ctk.CTkLabel(app, text="Alfabeto", fg_color="transparent")
    opciones_alfabeto = ctk.CTkOptionMenu(
        app, 
        values=list(ALFABETOS.keys()),
        command=actualizar_alfabeto
    )
    label_alfabeto.grid(row=3, column=0, padx=20, sticky="w")
    opciones_alfabeto.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

    entry_alfabeto_personalizado = ctk.CTkEntry(
        app,
        placeholder_text="Escribí tu alfabeto aquí",
        state="disabled"
    )
    entry_alfabeto_personalizado.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

    label_mensaje = ctk.CTkLabel(app, text="Mensaje", fg_color="transparent")
    entrada_mensaje = ctk.CTkEntry(app, placeholder_text="Escribe tu mensaje aquí")
    entrada_mensaje.grid(row=6, column=0, padx=20, pady=10, sticky="ew")

    boton_encriptar = ctk.CTkButton(app, text="Codificar", command=validar)
    boton_encriptar.grid(row=7, column=0, padx=20, pady=20, sticky="ew")

    mensaje_resultado = ctk.CTkLabel(app, text="")
    mensaje_resultado.grid(row=8, column=0, padx=20, pady=20)

    app.mainloop()
