import math

def altura_arbol(n_nodos, d):
    if d == 1:
        return n_nodos - 1  # Árbol lineal
    return math.ceil(math.log(n_nodos * (d - 1) + 1, d)) - 1

def preorden(arbol, d, indice=0):
    if indice >= len(arbol):
        return []

    resultado = [arbol[indice]] 
    for j in range(1, d + 1):
        hijo = d * indice + j
        resultado += preorden(arbol, d, hijo)
    return resultado


# Árbol representado como arreglo y el grado del arbol
arbol = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
grado = 3 

# La altura del arbol
altura = altura_arbol(len(arbol), grado)
print("Altura del árbol:", altura)

# Recorrido Pre-orden
res_preorden = preorden(arbol, grado)
print("Recorrido en preorden:", res_preorden)
