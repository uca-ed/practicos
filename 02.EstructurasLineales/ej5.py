from collections import defaultdict, deque

def cargar_grafo(nombre_archivo):
    grafo = defaultdict(list)
    nodos = set()

    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue

                partes = linea.split(",")
                origen = partes[0].strip()
                nodos.add(origen)

                if len(partes) > 1 and partes[1].strip():
                    destino = partes[1].strip()
                    grafo[origen].append(destino)
                    nodos.add(destino)

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{nombre_archivo}'")
        return None, None

    return grafo, nodos


def topological_sort(grafo, nodos):
    # Calcular grado de entrada de cada nodo
    grado_entrada = {nodo: 0 for nodo in nodos}

    for origen in grafo:
        for destino in grafo[origen]:
            grado_entrada[destino] += 1

    # Agregar a la cola todos los nodos con grado de entrada 0
    cola = deque()
    for nodo in sorted(nodos):  
        if grado_entrada[nodo] == 0:
            cola.append(nodo)

    resultado = []

    while cola:
        nodo = cola.popleft()
        resultado.append(nodo)

        # Reducir grado de entrada de los vecinos
        for vecino in sorted(grafo[nodo]):
            grado_entrada[vecino] -= 1
            if grado_entrada[vecino] == 0:
                cola.append(vecino)

    # Si no se procesaron todos los nodos, hay un ciclo
    if len(resultado) != len(nodos):
        return None

    return resultado


def main():
    grafo, nodos = cargar_grafo("grafo_ej5.txt")

    if grafo is None:
        return

    print("Grafo cargado:")
    for nodo in sorted(nodos):
        if grafo[nodo]:
            print(f"  {nodo} -> {', '.join(grafo[nodo])}")
        else:
            print(f"  {nodo} (sin salidas)")

    print()
    resultado = topological_sort(grafo, nodos)

    if resultado is None:
        print("El grafo es CÍCLICO, no es posible calcular el T-Sort.")
    else:
        print("T-Sort (orden topológico):")
        print(" -> ".join(resultado))


if __name__ == "__main__":
    main()
