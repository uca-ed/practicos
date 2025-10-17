def leer_grafo_desde_archivo(nombre_archivo):
    grafo = {}
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            origen, destino = linea.strip().split()
            if origen not in grafo:
                grafo[origen] = []
            grafo[origen].append(destino)
            if destino not in grafo:
                grafo[destino] = []
    return grafo


def calcular_tsort(grafo):
    # Obtener todos los nodos del grafo
    nodos = set(grafo.keys())
    for vecinos in grafo.values():
        for v in vecinos:
            nodos.add(v)

    # Calcular grado de entrada (estructura auxiliar, no modificamos grafo)
    grado_entrada = {nodo: 0 for nodo in nodos}
    for u in grafo:
        for v in grafo[u]:
            grado_entrada[v] += 1

    orden_topologico = []
    usados = set()

    while True:
        minimales = [
            nodo for nodo in nodos
            if grado_entrada[nodo] == 0 and nodo not in usados
        ]

        if not minimales:
            break

        for nodo in minimales:
            orden_topologico.append(nodo)
            usados.add(nodo)
            for vecino in grafo.get(nodo, []):
                grado_entrada[vecino] -= 1

    if len(orden_topologico) != len(nodos):
        print("El grafo es cíclico. No se puede calcular un T-Sort.")
        return None
    else:
        print("Orden topológico (T-Sort):", orden_topologico)
        return orden_topologico

if __name__ == "__main__":
    print("Ejemplo 1: Grafo acíclico")
    grafo_1 = leer_grafo_desde_archivo("Ejercicio_7_Aciclico.txt")
    calcular_tsort(grafo_1)

    print("\nEjemplo 2: Grafo cíclico")
    grafo_2 = leer_grafo_desde_archivo("Ejercicio_7_ciclo.txt")
    calcular_tsort(grafo_2)
