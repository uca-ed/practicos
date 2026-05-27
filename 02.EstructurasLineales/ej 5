def t_sort(grafo):
    sin_entrada = [nodo for nodo in grafo if len(grafo[nodo]["entrada"]) == 0]
    resultado = []

    while sin_entrada:
        nodo = sin_entrada.pop(0)
        resultado.append(nodo)
        for vecino in grafo[nodo]["salida"]:
            grafo[vecino]["entrada"].remove(nodo)
            if len(grafo[vecino]["entrada"]) == 0:
                sin_entrada.append(vecino)

    if len(resultado) != len(grafo):
        print("El grafo es cíclico, no se puede ordenar")
    else:
        print("T-Sort:", resultado)


# leer grafo desde archivo
# formato: A, B  (significa A -> B)
grafo = {}

with open("grafo.txt") as f:
    for linea in f:
        partes = linea.strip().split(",")
        a = partes[0].strip()
        b = partes[1].strip()
        if a not in grafo:
            grafo[a] = {"entrada": [], "salida": []}
        if b not in grafo:
            grafo[b] = {"entrada": [], "salida": []}
        grafo[a]["salida"].append(b)
        grafo[b]["entrada"].append(a)

t_sort(grafo)
