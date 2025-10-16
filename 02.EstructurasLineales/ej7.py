import csv
from collections import deque, defaultdict


def leer_grafo_csv(ruta):
    grafo = defaultdict(list)
    nodos = set()

    with open(ruta, "r", encoding="utf-8") as f:
        lector = csv.reader(f)
        for fila in lector:
            if not fila: 
                continue
            if fila[0].strip().lower() == "origen":  
                continue
            if len(fila) < 2:  
                continue

            origen, destino = fila[0].strip(), fila[1].strip()
            grafo[origen].append(destino)
            nodos.update([origen, destino])

    for n in nodos:
        grafo.setdefault(n, [])
    return dict(grafo)

def t_sort(grafo):
    indeg = {n: 0 for n in grafo}
    for u in grafo:
        for v in grafo[u]:
            indeg[v] += 1

    cola = deque([n for n in grafo if indeg[n] == 0])
    resultado = []

    while cola:
        nodo = cola.popleft()
        resultado.append(nodo)
        for vecino in grafo[nodo]:
            indeg[vecino] -= 1
            if indeg[vecino] == 0:
                cola.append(vecino)

    if len(resultado) != len(grafo):
        print("Estructura cíclica: no se puede calcular T-Sort")
        return None
    return resultado

def main():
    print("T-Sort para archivo 1")
    grafoAciclico = leer_grafo_csv("./ej5sinCiclos.csv")
    print("Orden topológico:", t_sort(grafoAciclico))

    print("\nT-Sort para archivo 2")
    grafoCiclico = leer_grafo_csv("./ej5conCiclos.csv")
    print("Orden topológico:", t_sort(grafoCiclico))

if __name__ == "__main__":
    main()