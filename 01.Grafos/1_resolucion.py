
import csv
import json

def cargar_csv(path):
    matriz = []
    with open(path, newline='', encoding='utf-8') as f:
        lector = csv.reader(f)
        for fila in lector:
            if fila:
                matriz.append([int(x) for x in fila])
    nodos = list(range(len(matriz)))
    return matriz, nodos

def cargar_json(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    nodos = data["P"]
    n = len(nodos)
    matriz = [[0]*n for _ in range(n)]
    pos = {etq: i for i, etq in enumerate(nodos)}
    for origen, destinos in data["E"].items():
        i = pos[origen]
        for destino in destinos:
            j = pos[destino]
            matriz[i][j] = 1
    return matriz, nodos

def minimales(matriz, nodos):
    n = len(matriz)
    res = []
    for j in range(n):
        es_minimal = True
        for i in range(n):
            if matriz[i][j] == 1:
                es_minimal = False
                break
        if es_minimal:
            res.append(nodos[j])
    return res

def maximales(matriz, nodos):
    n = len(matriz)
    res = []
    for i in range(n):
        es_maximal = True
        for j in range(n):
            if matriz[i][j] == 1:
                es_maximal = False
                break
        if es_maximal:
            res.append(nodos[i])
    return res

def vecindad_derecha(matriz, nodos, nodo):
    n = len(matriz)
    i = nodos.index(nodo)
    vecinos = []
    for j in range(n):
        if matriz[i][j] == 1:
            vecinos.append(nodos[j])
    return vecinos

def vecindad_izquierda(matriz, nodos, nodo):
    n = len(matriz)
    j = nodos.index(nodo)
    vecinos = []
    for i in range(n):
        if matriz[i][j] == 1:
            vecinos.append(nodos[i])
    return vecinos

matriz1, nodos1 = cargar_csv("01.csv")
print("Minimales (CSV):", minimales(matriz1, nodos1))
print("Maximales (CSV):", maximales(matriz1, nodos1))
print("Vec. derecha de 0:", vecindad_derecha(matriz1, nodos1, 0))
print("Vec. izquierda de 0:", vecindad_izquierda(matriz1, nodos1, 0))

matriz2, nodos2 = cargar_json("01.json")
un_nodo = nodos2[0]
print("Minimales (JSON):", minimales(matriz2, nodos2))
print("Maximales (JSON):", maximales(matriz2, nodos2))
print("Vec. derecha de", un_nodo, ":", vecindad_derecha(matriz2, nodos2, un_nodo))
print("Vec. izquierda de", un_nodo, ":", vecindad_izquierda(matriz2, nodos2, un_nodo))
