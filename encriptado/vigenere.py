def ascii_imprimibles() -> str:
    """
    Devuelve la tabla de caracteres  ascii imprimibles  
    """
    return "".join(chr(x) for x in range(32, 127))

def cifrar_ascii(caracter: str, caracter_clave: str, descifrar: bool) -> str:
    """
    Cifra un caracter usando el alfabeto ascii imprimible.
    Si el caracter no es un ascii imprimible, se devuelve el caracter sin cambios.
    """
    alfabeto = ascii_imprimibles()
    if caracter not in alfabeto or caracter_clave not in alfabeto:
        return caracter
    indice_clave = -alfabeto.index(caracter_clave) if descifrar else alfabeto.index(caracter_clave)
    return alfabeto[(alfabeto.index(caracter) + indice_clave) % len(alfabeto)]

def cifrar_caracter(caracter: str, mayus: bool, caracter_clave: str, descifrar: bool, alfabeto: str) -> str:
    """
    Cifra un caracter usando el cifrado Vigenère.
    Si el caracter está en el alfabeto proporcionado, se cifra.
    Si no, se devuelve el caracter sin cambios.
    """
    caracter_mayus = caracter.upper()
    if caracter_mayus not in alfabeto or caracter_clave not in alfabeto:
        return caracter
    indice_clave = -alfabeto.index(caracter_clave) if descifrar else alfabeto.index(caracter_clave)
    nueva_letra = alfabeto[(alfabeto.index(caracter_mayus) + indice_clave) % len(alfabeto)]
    return nueva_letra if mayus else nueva_letra.lower()

def vigenere(mensaje: str, clave: str, descifrar: bool = False, alfabeto: str = "") -> str:
    """
    Cifrado Vigenère.
    La clave es una cadena de caracteres que indica el desplazamiento.
    Si el alfabeto está vacío, se usa el alfabeto ascii imprimible.
    Si el alfabeto no está vacío, se usa el alfabeto proporcionado.
    Si el mensaje contiene caracteres que no están en el alfabeto, se devuelven sin cambios.
    """
    if alfabeto == "":
        return "".join(
            cifrar_ascii(
                caracter,
                clave[indice % len(clave)],
                descifrar
            ) for indice, caracter in enumerate(mensaje)
        )
    return "".join(
        cifrar_caracter(
            caracter,
            caracter.isupper(),
            clave[indice % len(clave)].upper(),
            descifrar,
            alfabeto
        ) for indice, caracter in enumerate(mensaje)
    )
