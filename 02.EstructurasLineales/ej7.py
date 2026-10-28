# El punto 7 solicita nuevamente un ordenamiento topológico
# sobre un grafo leído desde archivo. Se implementa de forma
# independiente para que el punto pueda ejecutarse por separado.

def leer_grafo(nombre_archivo):
    grafo = {}
    grado = {}

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if not linea or linea.startswith("#"):
                continue

            origen, destino = [x.strip() for x in linea.split(",")]

            if origen not in grafo:
                grafo[origen] = []
                grado[origen] = 0

            if destino not in grafo:
                grafo[destino] = []
                grado[destino] = 0

            grafo[origen].append(destino)
            grado[destino] += 1

    return grafo, grado


def sort_topologico(grafo, grado):
    cola = []

    for vertice in grado:
        if grado[vertice] == 0:
            cola.append(vertice)

    orden = []

    while cola:
        vertice = cola.pop(0)
        orden.append(vertice)

        for adyacente in grafo[vertice]:
            grado[adyacente] -= 1

            if grado[adyacente] == 0:
                cola.append(adyacente)

    if len(orden) != len(grafo):
        return None

    return orden


grafo, grado = leer_grafo("grafo.txt")
orden = sort_topologico(grafo, grado)

if orden is None:
    print("El grafo es cíclico. No existe un orden topológico.")
else:
    print("Orden topológico:")
    print(" -> ".join(orden))
