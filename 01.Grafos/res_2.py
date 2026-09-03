import csv
import json

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

def es_reflexivo(matriz):
    n = len(matriz)
    for i in range(n):
        if matriz[i][i] != 1:
            return False
    return True

def es_simetrico(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def es_antisimetrico(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i != j and matriz[i][j] == 1 and matriz[j][i] == 1:
                return False
    return True

def es_transitivo(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j]:
                for k in range(n):
                    if matriz[j][k] and not matriz[i][k]:
                        return False
    return True

def tipo_relacion(matriz):
    reflexivo = es_reflexivo(matriz)
    simetrico = es_simetrico(matriz)
    antisimetrico = es_antisimetrico(matriz)
    transitivo = es_transitivo(matriz)
    if reflexivo and simetrico and transitivo:
        return "Equivalencia"
    if reflexivo and antisimetrico and transitivo:
        return "Orden"
    return "Ninguna"

matriz, nodos = cargar_json("01.json")
print("Reflexivo:", es_reflexivo(matriz))
print("Simetrico:", es_simetrico(matriz))
print("Antisimetrico:", es_antisimetrico(matriz))
print("Transitivo:", es_transitivo(matriz))
print("Tipo de relacion:", tipo_relacion(matriz))