from collections import defaultdict, deque

# Lee grafo desde archivo
def cargar_grafo(nombre_archivo):
    with open("Archivo para ej/grafo 2.txt", "r") as archivo:
        lineas = archivo.readlines()
        n = int(lineas[0].strip())  # cantidad de nodos
        aristas = [tuple(map(int, linea.strip().split())) for linea in lineas[1:]]
    return n, aristas

# Algoritmo de ordenamiento topológico (Kahn)
def orden_topologico(n, aristas):
    grafo = defaultdict(list)
    grado_entrada = [0] * n

    # Construcción del grafo
    for origen, destino in aristas:
        grafo[origen].append(destino)
        grado_entrada[destino] += 1

    # Cola con nodos sin predecesores
    cola = deque([i for i in range(n) if grado_entrada[i] == 0])
    orden = []

    while cola:
        nodo = cola.popleft()
        orden.append(nodo)
        for vecino in grafo[nodo]:
            grado_entrada[vecino] -= 1
            if grado_entrada[vecino] == 0:
                cola.append(vecino)

    if len(orden) != n:
        return None  # Hay ciclo
    return orden

# Main
def main():
    archivo = "grafo 2.txt"
    n, aristas = cargar_grafo("Archivo para ej/grafo 2.txt")
    resultado = orden_topologico(n, aristas)

    if resultado is None:
        print("El grafo contiene un ciclo. No se puede hacer sort topológico.")
    else:
        print("Orden topológico:")
        print(" -> ".join(map(str, resultado)))

main()