#Dada una funcion imprime el menor de los valores que no se encuentran en la lista
def solucion(lista1):
    listar=[]
    for value in range(min(lista1),max(lista1)):
        if value not in lista1:
            listar.append(value)
    print(min(listar))

listaprueba=[1,2,4,5,8]
solucion(listaprueba)   