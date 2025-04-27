def cesar(mensaje: str, clave: int = 6, descifrar: bool = False, alfabeto: str = "") -> str:
    """
    Cifrado Cesar.
    """
    mensaje_en_mayusculas = mensaje.upper() #Poner todas las letas en mayusculas

    # Si es para descifrar, invertimos la clave
    if descifrar: 
        clave = -clave #Si la variables es true

    resultado = ""

    for indice, caracter in enumerate(mensaje_en_mayusculas):
        if caracter in alfabeto:
            posicion = alfabeto.index(caracter)
            nueva_posicion = (posicion + clave) % len(alfabeto)  
            nuevo_caracter = alfabeto[nueva_posicion]
            if mensaje[indice].islower(): 
                nuevo_caracter=nuevo_caracter.lower()
            resultado += nuevo_caracter
        else:
            resultado += caracter  

    return resultado

print(cesar("Htrywfwwj0tpzhntrfwnt", 5, descifrar=True, alfabeto="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"))
