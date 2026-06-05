def altura(arreglo, grado):
    n = len(arreglo)

    if n == 0:
        return -1

    nivel = 0
    nodos_acumulados = 1
    nodos_en_nivel = 1

    # Se calcula la altura usando la cantidad de nodos
    # y el grado del árbol, sin recorrerlo.
    while nodos_acumulados < n:
        nodos_en_nivel = nodos_en_nivel * grado
        nodos_acumulados += nodos_en_nivel
        nivel += 1

    return nivel


def preorden(arreglo, grado, i=0):
    # caso base: si el grado es 0 o el índice se pasa del arreglo, no hay nada que recorrer
    if grado == 0 or i >= len(arreglo):
        return
    
    print(arreglo[i])  # primero visito la raíz
    
    for k in range(1, grado + 1):
        hijo = grado * i + k  # fórmula para obtener el k-ésimo hijo del nodo i
        preorden(arreglo, grado, hijo)  # recorro cada subárbol

# Prueba
arbol = ["A","B","C","D","E","F","G"]
grado = 2
print("Preorden:")
preorden(arbol, grado)
