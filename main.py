import tkinter as tk

ventana = tk.Tk()
ventana.geometry("250x250")
hola_mundo = tk.Label(
    text="¡Hola Mundo!",
    width=10,
    height=5,
    font=("Arial", 25)
)
hola_mundo.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

ventana.mainloop()
