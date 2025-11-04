"""
1. Dado un arreglo sobre el que está representado un árbol de grado indicado como dato, dar un algoritmo que:
a) detecte la altura del árbol sin hacer recorridos
b) realice un barrido pre-orden
"""

def detectar_altura(arreglo, grado):
    cantidad_nodos = len(arreglo)
    altura = 0
    nodos_acumulados = 0
    nodos_nivel = 1

    while nodos_acumulados < cantidad_nodos:
        altura += 1
        nodos_acumulados += nodos_nivel
        nodos_nivel *= grado
    
    return altura


def preorden(arreglo, grado, indice):
    if indice >= len(arreglo):
        return
    
    print(arreglo[indice], end=" ")

    primer_hijo = indice * grado + 1
    for h in range(grado):
        preorden(arreglo, grado, primer_hijo + h)


def ejecutar():
    arreglo = ["A", "B", "C", "D", "E", "F", "G", "H"]
    grado = 3
    
    altura = detectar_altura(arreglo, grado)
    print("Altura del arbol:", altura)

    print("Barrido preorden:", end=" ")
    preorden(arreglo, grado, 0)
    print()


ejecutar()
