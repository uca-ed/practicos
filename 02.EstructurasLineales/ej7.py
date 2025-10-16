def leer_grafo(nombre_archivo):
    grafo = {}
    nodos = set()

    with open(nombre_archivo, "r") as f:
        for linea in f:
            if not linea.strip():
                continue
            origen, destino = linea.strip().split()

            if origen not in grafo:
                grafo[origen] = []
            grafo[origen].append(destino)

            nodos.add(origen)
            nodos.add(destino)

    
    for n in nodos:
        if n not in grafo:
            grafo[n] = []

    return grafo, list(nodos)


def topological_sort(grafo, nodos):
    
    in_degree = {}
    for n in nodos:
        in_degree[n] = 0

    for origen in grafo:
        for destino in grafo[origen]:
            in_degree[destino] += 1

    
    cola = []
    for n in nodos:
        if in_degree[n] == 0:
            cola.append(n)

    orden = []

    while cola:
        
        nodo = cola.pop(0)
        orden.append(nodo)

        
        for vecino in grafo[nodo]:
            in_degree[vecino] -= 1
            if in_degree[vecino] == 0:
                cola.append(vecino)

   
    if len(orden) != len(nodos):
        print("El grafo tiene un ciclo. No se puede ordenar topológicamente.")
        return None
    else:
        return orden


def main():
    archivo = "grafo.txt"  
    grafo, nodos = leer_grafo(archivo)

    print("Grafo leído:")
    for n in grafo:
        print(f"{n} -> {grafo[n]}")

    resultado = topological_sort(grafo, nodos)
    if resultado:
        print("\nOrden topológico:")
        print(" -> ".join(resultado))



main()