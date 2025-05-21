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

    # Lista de nodos sin entrada (calculado al inicio)
    orden_topologico = []
    usados = set()

    while True:
        # Buscar minimales actuales (no usados, con grado de entrada 0)
        minimales = [
            nodo for nodo in nodos
            if grado_entrada[nodo] == 0 and nodo not in usados
        ]

        if not minimales:
            break  # Ya no hay más nodos sin entrada

        for nodo in minimales:
            orden_topologico.append(nodo)
            usados.add(nodo)

            # Crear una copia temporal de grado_entrada solo para actualizar este paso, no modificamos el grafo
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
    grafo_1 = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['H', 'F'],
        'F': ['G'],
        'G': [],
        'H': []
    }
    calcular_tsort(grafo_1)

    print("\nEjemplo 2: Grafo con ciclo")
    grafo_2 = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']  # Ciclo A → B → C → A
    }
    calcular_tsort(grafo_2)
