def vignere_unicode(mensaje: str, clave: str, descifrar: bool) -> str:
    resultado = ""
    longitud_unicode = 1_114_112
    for indice, letra in enumerate(mensaje.upper()):
        letra_clave = clave[indice % len(clave)].upper()
        if descifrar:
            indice_resultante = (ord(letra) - ord(letra_clave)) % longitud_unicode
        else:
            indice_resultante = (ord(letra) + ord(letra_clave)) % longitud_unicode
        letra_resultante = chr(indice_resultante)
        resultado += letra_resultante
    return resultado

def vigenere(mensaje: str, clave: str, descifrar: bool = False, alfabeto: str = "") -> str:
    """
    Cifrado Vigenère.
    """

    resultado = ""

    if alfabeto == "":
        return vignere_unicode(mensaje, clave, descifrar)

    for indice, letra in enumerate(mensaje.upper()):
        if letra in alfabeto:

            indice_mensaje = alfabeto.index(letra)
            letra_clave = clave[indice % len(clave)].upper()
            indice_clave = alfabeto.index(letra_clave)

            if descifrar:
                indice_resultante = (indice_mensaje - indice_clave) % len(alfabeto)
            else:
                indice_resultante = (indice_mensaje + indice_clave) % len(alfabeto)

            letra_original = mensaje[indice]
            letra_resultante = alfabeto[indice_resultante]
            if letra_original.islower():
                letra_resultante = letra_resultante.lower()
            resultado += letra_resultante
    return resultado

print(vigenere("HOLA", "CLAVE"))
