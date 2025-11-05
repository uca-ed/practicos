"""
1. Dado un arreglo sobre el que está representado un árbol de grado indicado como dato, dar un algoritmo que:
a) detecte la altura del árbol sin hacer recorridos
b) realice un barrido pre-orden
"""

import math

def calcular_altura(arreglo, r):
    """
    Asumo que es un arbol r-ario lleno
    """
    N = len(arreglo)
    print(f"Arbol de grado {r} con {N} nodos.")

    if N == 0:
        print("El arbol es vacio")

    elif N == 1:
        print(f"La altura del arbol es: 0") 

    elif r == 1:
        aux=N-1
        print(f"La altura del arbol es: {aux}") 

    else:
        valor = math.log(N) / math.log(r)
        altura = math.floor(valor)
        print(f"La altura del arbol es: {altura}")

# Ejemplo de Uso
# altura = calcular_altura(arreglo, grado)

calcular_altura([0]*2, 1)
calcular_altura([0]*3, 1)
calcular_altura([0]*15, 2)
calcular_altura([0]*21, 4)
calcular_altura([0]*85, 4)
calcular_altura([0]*40, 3)
print("\n")

def pre_order(arreglo, r):
    print("Resultado Preorden:")
    _pre_order_recursivo(arreglo, r, 0)
    print() 

def _pre_order_recursivo(arreglo, r, i):

    if i >= len(arreglo):
        return
    print(arreglo[i], end=" ")
    for j in range(1, r + 1):
        hijo = r * i + j
        _pre_order_recursivo(arreglo, r, hijo)

# Ejemplo de Uso
arreglo = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
pre_order(arreglo,2)
arreglo = [10, 20, 30, 40]
pre_order(arreglo,3)
arreglo = ['X', 'Y', 'Z', 'W', 'V']
pre_order(arreglo,4)
arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pre_order(arreglo,3)