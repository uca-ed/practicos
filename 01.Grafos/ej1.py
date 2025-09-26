"""
Representar a un grafo utilizando una matriz de adyacencia.
Sobre tal representación, se debe poder ejecutar los
siguientes operadores:
a. Minimales del grafo
b. Maximales del grafo
c. Vecindad derecha de un nodo
d. Vecindad izquierda de un nodo                             """

import numpy as np
import pandas as pd
import json

def min(M):
    return M.columns[(M == 0).all()].tolist()

def max(M):
    return M.index[(M == 0).all(axis=1)].tolist()

def R(n, M):
    return M.loc[n][M.loc[n]==1].index.tolist()

def L(n, M):
    return M[n][M[n]==1].index.tolist()

## EJEMPLOS:

# importo .json
with open("01.json", 'r') as f:
    data = json.load(f)
G_json = {"P":data['P'], "E":data['E']} #matriz json

#importo .cvs
CSVs = {
    "G_csv1": pd.read_csv("01.csv", header=None),
    "G_csv2": pd.read_csv("02.csv", header=None),
    "G_csv3": pd.read_csv("03.csv", header=None),
    "G_csv4": pd.read_csv("04.csv", header=None)}

#función para pasar grafo a matriz
def matrizAdy(G):
    P = G["P"]
    E = G["E"]
    salidas = [n1 for n1, llegada in E.items() for _ in llegada]
    llegadas = [n2 for llegada in E.values() for n2 in llegada]
    M = pd.crosstab(
        index=salidas, columns=llegadas).reindex(
            index=P, columns=P, fill_value=0)
    return M

# prints
ejemplos = {**CSVs, "G_json": matrizAdy(G_json)}
for m in ejemplos:
    print(f"minimales de {m}: {min(ejemplos[m])}, maximales de {m}: {max(ejemplos[m])}")
