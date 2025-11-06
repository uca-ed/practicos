'''
Implementacion Arboles-Ejercicio1 
Dado un arreglo sobre el que está representado un árbol de grado indicado como dato,
dar un algoritmo que:
a) detecte la altura del árbol sin hacer recorridos
b) realice un barrido pre-orden
'''
import math


def ultimo_indice_valido(arbol, vacio=None):
    
    #Devuelve el índice del último elemento no vacío.
    #Si todo es vacío, retorna -1.

    for i in range(len(arbol) - 1, -1, -1):
        if arbol[i] != vacio:
            return i
    return -1


def altura_sin_recorridos(arbol, k, vacio=None):
    
    #Altura = niveles - 1
    #Niveles = piso( log_k( n*(k-1) + 1 ) )
    #n = cantidad de nodos realmente presentes
    
    if k < 1:
        raise ValueError("k debe ser >= 1")
    idx = ultimo_indice_valido(arbol, vacio)
    if idx == -1:
        return -1  # árbol vacío
    
    n = idx + 1
    if k == 1:
        return n - 1

    niveles = math.floor(math.log(n * (k - 1) + 1, k))
    return niveles - 1


def preorden(arbol, k, vacio=None):
    res = []

    def _pre(i):
        if i >= len(arbol) or arbol[i] == vacio:
            return
        # Visito el nodo i
        res.append(arbol[i])
       
        base = k * i
        for j in range(1, k + 1):
            _pre(base + j)

    _pre(0)  # raíz en 0
    return res


# Ejemplos

if __name__ == "__main__":
    # Ejemplo 1: 
    #        A
    #      /   \
    #     B     C
    #    / \     \
    #   D   E     F
    # Arreglo por niveles: [A, B, C, D, E, None, F]
    arbol1 = ["A", "B", "C", "D", "E", None, "F"]
    k1 = 2
    print("Preorden 1 :", preorden(arbol1, k1, vacio=None))
    print("Altura 1:", altura_sin_recorridos(arbol1, k1, vacio=None))  # 2

    # Ejemplo 2:
    # Nivel 0:         R
    # Nivel 1:    A        B        C
    # Nivel 2:  D E F    G H I    J K L
    # Arreglo: [R, A, B, C, D, E, F, G, H, I, J, K, L]
    arbol2 = ["R", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    k2 = 3
    print("Preorden 2:", preorden(arbol2, k2, vacio=None))
    print("Altura 2:", altura_sin_recorridos(arbol2, k2, vacio=None))  # 2

    # Ejemplo 3: árbol vacío
    arbol3 = []
    print("Preorden 3:", preorden(arbol3, 2, vacio=None))
    print("Altura 3:", altura_sin_recorridos(arbol3, 2, vacio=None))  # -1
