def ascii_imprimibles() -> str:
    """
    Devuelve la tabla de caracteres  ascii imprimibles  
    """
    return "".join(chr(x) for x in range(32, 127))

def cifrar_caracter(caracter: str, mayus: bool, clave: int, alfabeto: str) -> str:
    """
    Cifra un caracter usando el cifrado Cesar.
    Si el caracter es una letra, se cifra usando el alfabeto proporcionado.
    Si el caracter no es una letra, se devuelve el caracter sin cambios.
    """
    caracter_mayus = caracter.upper()
    if caracter_mayus in alfabeto:
        nueva_letra = alfabeto[(alfabeto.index(caracter_mayus) + clave) % len(alfabeto)]
        return nueva_letra if mayus else nueva_letra.lower()
    return caracter

def cifrar_ascii(caracter, clave):
    """
    Cifra un caracter usando el alfabeto ascii imprimible.
    """
    alfabeto = ascii_imprimibles()
    if caracter in alfabeto:
        nuevo_caracter = alfabeto[(alfabeto.index(caracter) + clave) % len(alfabeto)]
        return nuevo_caracter
    return caracter

def cesar(mensaje: str, clave: int, descifrar: bool = False, alfabeto: str = "") -> str:
    """
    Cifrado Cesar
    """
    clave = -clave if descifrar else clave
    if alfabeto == "":
        return "".join(cifrar_ascii(caracter, clave) for caracter in mensaje)
    return "".join(cifrar_caracter(caracter, caracter.isupper(), clave, alfabeto) for caracter in mensaje)
