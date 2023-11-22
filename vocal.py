#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False

vocales=["a","e","i","o","u"]

def esvocal(char):
    vocales=["a","e","i","o","u"]
    for n in vocales:
        if n == char:
            return True
    else: 
        return False


esvocal("b")


