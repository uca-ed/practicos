"""5. Implementar en un lenguaje de programación el algoritmo de cálculo de T-Sort basado en un grafo. 
De no ser posible calcularlo, indicar que la estructura es cíclica.  """

from collections import deque

def MinUnico(G):
    indeg = {nodo: 0 for nodo in G}
    for origen in G:
        for destino in G[origen]:
            indeg[destino] += 1

    sin_predecesores = [nodo for nodo in indeg if indeg[nodo] == 0]
    
    if not sin_predecesores:
        return None
    
    return min(sin_predecesores)

def T_Sort(G):
    G = {nodo: list(ady) for nodo, ady in G.items()}

    Q = deque()
    OT = []  
    x = MinUnico(G)
    Q.append(x)

    while Q:
        x = Q.popleft()
        OT.append(x)

        if x in G:
            G.pop(x)

        for nodo in G:
            if x in G[nodo]:
                G[nodo].remove(x)

        nuevo = MinUnico(G)
        if nuevo is not None:
            Q.append(nuevo)

    if any(G.values()):
        print("El grafo es ciclico")
        return None

    return OT


def main():
    grafo = {
        'A': ['B', 'C'],
        'B': ['D','A'],
        'C': ['D'],
        'D': []
    }
    G={}
    resultado = T_Sort(grafo)
    if resultado:
        print("Orden topologico:", resultado)


main()

    