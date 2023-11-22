#Escribe, en el lenguaje de programación que desees, un programa que muestre en pantalla los números 
#del 1 al 100, sustituyendo los múltiplos de 3 por el palabra “Fizz” y, a su vez, los múltiplos de 5 por “Buzz”. 
#Para los guarismos que, al tiempo, son múltiplos de 3 y 5, utiliza el combinado “FizzBuzz”.
def fizzbuzz(lista):
    for n in lista: 
        if n%3==0 and n%5==0:
            print("FizzBuzz")
        elif n%3 == 0:
            print("Fizz")
        elif n%5 == 0:
            print("Buzz")
        else: 
            print(n)

lista1=list(range(1,31))
fizzbuzz(lista1)
