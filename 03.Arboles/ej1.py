import math

def altura_sin_recorrer(arbol, grado):
    n = len(arbol)
    if n == 0:
        return 0
    return math.ceil(math.log((n * (grado - 1)) + 1, grado))


def preorden(arbol, grado, indice=0):
    if indice >= len(arbol):
        return []
    
    recorrido = [arbol[indice]]
    
    for k in range(1, grado + 1):
        hijo = grado * indice + k
        recorrido += preorden(arbol, grado, hijo)
    
    return recorrido


def main():
    arbol = [1, 2, 3, 4, 5, 6, 7]
    grado = 2

    print("Altura:", altura_sin_recorrer(arbol, grado))
    print("Preorden:", preorden(arbol, grado))
    print()
    
    arbol = [1, 2, 3, 4, 5, 6, 7, 8]
    grado = 2

    print("Altura:", altura_sin_recorrer(arbol, grado))
    print("Preorden:", preorden(arbol, grado))
    print()

main()