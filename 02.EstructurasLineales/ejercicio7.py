"""7. Implementar Sort topológico sobre un grafo dado como dato en un archivo. """
def leer_grafo(nombre_archivo):
    grafo = {}
    with open(nombre_archivo, "r") as f:
        for linea in f:
            # Convertir la línea en una lista de palabras, separadas por espacios
            partes = []
            palabra = ""

            for c in linea:
                if c != " " and c != "\n":     # si no es espacio ni salto de línea
                    palabra = palabra + c
                else:
                    if palabra != "":
                        partes.append(palabra)
                        palabra = ""
            if palabra != "":
                partes.append(palabra)

            if len(partes) == 0:
                continue

            # Primer elemento = origen, resto = destinos
            origen = partes[0]
            destinos = partes[1:]
            grafo[origen] = destinos

            # Asegurar que los destinos existan en el grafo
            for d in destinos:
                if d not in grafo:
                    grafo[d] = []
    return grafo


def min_unico(grafo, grado_entrada):
    for v in grafo:
        if grado_entrada[v] == 0:
            return v
    return None


def t_sort(grafo):
    # Calcular el grado de entrada de cada vértice
    grado_entrada = {}
    for v in grafo:
        grado_entrada[v] = 0
    for v in grafo:
        for w in grafo[v]:
            grado_entrada[w] = grado_entrada[w] + 1

    OT = []  # lista de salida
    Q = []   # cola de vértices

    v = min_unico(grafo, grado_entrada)
    if v != None:
        Q.append(v)

    while len(Q) > 0:
        x = Q[0]
        Q = Q[1:]     # sacar el primero
        OT.append(x)

        for w in grafo[x]:
            grado_entrada[w] = grado_entrada[w] - 1
        grado_entrada[x] = -1  # eliminado

        v = min_unico(grafo, grado_entrada)
        if v != None and (v not in Q) and (v not in OT):
            Q.append(v)

    if len(OT) != len(grafo):
        print("El grafo tiene un ciclo.")
        return None
    return OT


# Programa principal
archivo = "C:/Users/Puerto Digital/Documents/GitHub/practicos_ed/02.EstructurasLineales/grafo.txt"
grafo = leer_grafo(archivo)

print("Grafo leído:")
for k in grafo:
    print(k, "->", grafo[k])

orden = t_sort(grafo)
if orden != None:
    print("\nOrden topológico:", orden)
