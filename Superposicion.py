#Definir una función superposicion() que tome dos listas y 
#devuelva True si tienen al menos 1 miembro en común o devuelva False 
#de lo contrario. Escribir la función usando el bucle for anidado.
def superposicion(lista1,lista2):
    for n in lista1:
        for m in lista2:
            if n == m:
                 return True
            else:
                return False
listap1=[1,2,3,4]
listap2=[5,6,7,8]
r= superposicion(listap1,listap2)
print(r)