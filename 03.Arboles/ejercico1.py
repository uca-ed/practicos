#Árboles
#1. Dado un arreglo sobre el que está representado un árbol de grado indicado como dato, dar un algoritmo que:
#a) detecte la altura del árbol sin hacer recorridos
#b) realice un barrido pre-orden


import math

#a) Altura de un arbol sin recorrer
def alturaArbol(A,k):
    n = len(A)
    if n==0:
        return -1     # --> árbol vacío
    if k==1:
        return n - 1
    
    i=n-1   
    h=0
    while i>0:
        i=(i-1)//k
        h+=1
    return h
    
#Aclaracion: no estoy recorriendo el arreglo, solo estoy contando los niveles para hallar la altura.

#b) Barrido de pre-orden
def preorden(A,k,i):
    if i >= len(A) or A[i] is None:
        return "Termina"
    
    print(A[i], end=" ")
    for j in range(k):
        hijo = k*i + j + 1
        preorden(A, k, hijo)

A=["A","B","C","D","E","F","G"]
k=3

print("Altura del árbol:",alturaArbol(A,k))
print("Barrido preorden:")
i=0
preorden(A,k,i)