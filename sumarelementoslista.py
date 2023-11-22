#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
lista=[2]
if len(lista)==1:
    print(f"el resultado es: {lista}")
multiplicacion=1
suma=0
for n in range(0,len(lista)):
    multiplicacion*=lista[n]
    suma+=lista[n]
print(f"la multiplicacion es:{multiplicacion}", f"la suma es {suma}")
    