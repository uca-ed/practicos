#Dado un arreglo sobre el que está representado un árbol de grado indicado como dato, dar un algoritmo que: 
#a) detecte la altura del árbol sin hacer recorridos 
#b) realice un barrido pre-orden

#barrido pre orden:
#r raiz del APD
#S<-(r,0)
#mientras S no vacia:
#x<-S
#visitar(x)
#para i = Grado(G);i>0;i--{S<-R^i(x)

import math

#a
def calcular_altura(arreglo, grado): #grado=maximo de hijos que puede tener un nodo
    N=len(arreglo)
    if N==0:
        return 0
    if N==1:
        return 1
    
    numerador=math.log((N*(grado-1))+1)
    denominador=math.log(grado)
    
    altura=math.ceil(numerador/denominador)-1
    return altura

#b
def preorden(arreglo, grado):
    if not arreglo:
        return

    pila=[0] 
    while len(pila) > 0:
        x=pila.pop()
        if x<len(arreglo):
            if arreglo[x] is not None and arreglo[x]!="None":
                print(f"Posición {x}: {arreglo[x]}")
            for i in range(grado,0,-1):
                hijo=(grado*x)+i
                if hijo<len(arreglo):
                    pila.append(hijo)

def main():
    with open(r"C:\Users\danie\OneDrive\Documentos\estructura de datos\practica3\ej1.txt") as f:
        datos=f.read().split(",")
        print(f"Altura del árbol: {calcular_altura(datos, 2)}\n")
        print("Barrido pre-orden:")
        preorden(datos, 2)


main()