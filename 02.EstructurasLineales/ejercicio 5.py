import csv
from collections import deque

def cargar_grafo_csv_matriz(ruta_csv):
    P = []  # Lista de nodos
    E = {}  # Diccionario de vecindades

    with open(ruta_csv, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)

        matriz = list(reader)
        num_nodos = len(matriz)

        P = [str(i+1) for i in range(num_nodos)]

        for i in range(num_nodos):
            E[P[i]] = [P[j] for j in range(num_nodos) if matriz[i][j] == '1']

    return {"P": P, "E": E}

def t_sort(G):
    P = G["P"][:]
    E = {k: v[:] for k, v in G["E"].items()} 
    ST = []  
    
    indegree = {n: 0 for n in P}
    for vecinos in E.values():
        for v in vecinos:
            indegree[v] += 1

    Q = deque([n for n in P if indegree[n] == 0])

    while Q:
        X = Q.popleft()
        ST.append(X)

        P.remove(X)

        for vecino in E[X]:
            indegree[vecino] -= 1
            if indegree[vecino] == 0:
                Q.append(vecino)

        E.pop(X)

    if P:
        print("El grafo es cíclico, no se puede realizar T-Sort.")
        return None
    else:
        print("Orden topológico:", ST)
        return ST
    
estructura = cargar_grafo_csv_matriz('01.csv')

t_sort(estructura)

estructura = cargar_grafo_csv_matriz('02.csv')

t_sort(estructura)

