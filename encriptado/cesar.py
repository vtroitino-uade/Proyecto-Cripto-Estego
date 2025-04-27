def ascii_imprimibles() -> str:
    """
    devuelve la tabla de caracteres  ascii imprimibles  
    """
    return "".join(chr(x) for x in range(32, 127))

def cifrar_caracter(caracter, mayus, clave, alfabeto):
    caracter_mayus = caracter.upper()
    if caracter_mayus in alfabeto:
        nueva_letra = alfabeto[(alfabeto.index(caracter_mayus) + clave) % len(alfabeto)]
        return nueva_letra if mayus else nueva_letra.lower()
    return caracter

def cifrar_ascii(caracter, clave):
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
        return "".join(cifrar_ascii(c, clave) for c in mensaje)
    return "".join(cifrar_caracter(c, c.isupper(), clave, alfabeto) for c in mensaje)
