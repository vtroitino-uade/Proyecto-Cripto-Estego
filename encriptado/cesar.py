def ascii_imprimibles() -> str:
    """
    Devuelve la tabla de caracteres  ascii imprimibles  
    """
    return "".join(chr(x) for x in range(32, 127))

def cifrar_ascii(caracter, clave):
    """
    Cifra un caracter usando el alfabeto ascii imprimible.
    Si el caracter no es un ascii imprimible, se devuelve el caracter sin cambios.
    """
    alfabeto = ascii_imprimibles()
    if caracter in alfabeto:
        nuevo_caracter = alfabeto[(alfabeto.index(caracter) + clave) % len(alfabeto)]
        return nuevo_caracter
    return caracter

def cifrar_caracter(caracter, mayus, clave, alfabeto):
    """
    Cifra un caracter usando el cifrado César.
    Si el caracter está en el alfabeto proporcionado, se cifra.
    Si no, se devuelve el caracter sin cambios.
    """
    caracter_mayus = caracter.upper()
    if caracter_mayus in alfabeto:
        nueva_letra = alfabeto[(alfabeto.index(caracter_mayus) + clave) % len(alfabeto)]
        return nueva_letra if mayus else nueva_letra.lower()
    return caracter

def cesar(mensaje: str, clave: int, descifrar: bool = False, alfabeto: str = "") -> str:
    """
    Cifrado Cesar.
    La clave es un número entero que indica el desplazamiento.
    Si el alfabeto está vacío, se usa el alfabeto ascii imprimible.
    Si el alfabeto no está vacío, se usa el alfabeto proporcionado.
    Si el mensaje contiene caracteres que no están en el alfabeto, se devuelven sin cambios.
    """
    clave = -clave if descifrar else clave
    if alfabeto == "":
        return "".join(cifrar_ascii(c, clave) for c in mensaje)
    return "".join(cifrar_caracter(c, c.isupper(), clave, alfabeto) for c in mensaje)
