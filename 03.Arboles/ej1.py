import math

def calcular_altura_arreglo(arreglo, grado):
    N = len(arreglo)
    if N == 0:
        return -1  # Árbol vacío
    
    # Si el grado es 1, es una lista lineal
    
    if grado == 1:
        return N - 1

    altura = math.ceil(math.log((N * (grado - 1)) + 1, grado)) - 1
    return altura

def pre_orden_arreglo(arreglo, grado, indice_actual=0):
    
    # Condición de corte: si el índice excede el tamaño del arreglo
    
    if indice_actual >= len(arreglo) or arreglo[indice_actual] is None:
        return

    # 1. Procesar la raíz (nodo actual)
    print(arreglo[indice_actual], end=" ")

    # 2. Procesar todos los hijos en orden de izquierda a derecha
    for k in range(1, grado + 1):
        indice_hijo = (indice_actual * grado) + k
        pre_orden_arreglo(arreglo, grado, indice_hijo)


arbol_ejemplo = ['A', 'B', 'C', 'D', 'E']
grado_ejemplo = 2

print("Barrido Pre-orden:")
pre_orden_arreglo(arbol_ejemplo, grado_ejemplo)
