def leer_grafo(nombre_archivo):
    grafo = {}
    grado_entrada = {}

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue

            origen, destino = [x.strip() for x in linea.split(",")]

            if origen not in grafo:
                grafo[origen] = []
            if destino not in grafo:
                grafo[destino] = []

            if origen not in grado_entrada:
                grado_entrada[origen] = 0
            if destino not in grado_entrada:
                grado_entrada[destino] = 0

            grafo[origen].append(destino)
            grado_entrada[destino] += 1

    return grafo, grado_entrada


def t_sort(grafo, grado_entrada):
    cola = []

    for nodo in grado_entrada:
        if grado_entrada[nodo] == 0:
            cola.append(nodo)

    resultado = []

    while len(cola) > 0:
        nodo = cola.pop(0)
        resultado.append(nodo)

        for vecino in grafo[nodo]:
            grado_entrada[vecino] -= 1

            if grado_entrada[vecino] == 0:
                cola.append(vecino)

    if len(resultado) != len(grafo):
        return None

    return resultado


grafo, grado = leer_grafo("grafo.txt")
resultado = t_sort(grafo, grado)

if resultado is None:
    print("No es posible calcular T-Sort: la estructura es cíclica.")
else:
    print("Secuencia generada por T-Sort:")
    print(" -> ".join(resultado))
