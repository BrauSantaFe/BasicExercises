# Given two lists, l1 and l2, write a program to find the sum of the largest odd number and the largest 
# even number. 
# If there are only odd elements, write the sum of the largest with zero.
# If there are only even elements, write the sum of the largest with zero.
lista1=[0,1,2,4,22]
def solution(numbers):   
    l3=[]
    l4=[]
    for n in numbers: 
        if n % 2 == 0: 
            l3.append(n)

    for n in numbers:
        if n % 2 != 0:
            l4.append(n)

    if not l3:
        print(max(l4)+0)
    elif not l4:
        print(0+max(l3))
    else:
        print(max(l4)+max(l3))

solution(lista1)