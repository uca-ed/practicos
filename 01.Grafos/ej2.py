import numpy as np
import pandas as pd
import json

def esReflexiva(M):
    return (np.diag(M) == 1).all()

def esSim(M):
    return (M.values == M.T.values).all()

def esAntisim(M):
    return not (M & M.T & ~np.identity(M.shape[0], dtype=bool)).any().any()

def esTransitiva(M):
    return (((M @ M) > 0) <= M).values.all()

def esOrden(M):
    return esReflexiva(M) and esAntisim(M) and esTransitiva(M)

def esEquivalencia(M):
    return esReflexiva(M) and esSim(M) and esTransitiva(M)

## EJEMPLOS:

with open("01.json", 'r') as f:
    data = json.load(f)
G_json1 = {"P":data['P'], "E":data['E']} #matriz json
with open("02.json", 'r') as f:
    data = json.load(f)
G_json2 = {"P":data['P'], "E":data['E']} #matriz json
with open("03.json", 'r') as f:
    data = json.load(f)
G_json3 = {"P":data['P'], "E":data['E']} #matriz json

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
ejemplos = {"G_json1": matrizAdy(G_json1),
            "G_json2": matrizAdy(G_json2),
            "G_json3": matrizAdy(G_json3)}

for n, m in ejemplos.items():
    print(f"Vemos {n}:")
    print(f"Propiedades: Reflexiva={esReflexiva(m)}, Simétrica={esSim(m)}, Antisimétrica={esAntisim(m)}, Transitiva={esTransitiva(m)}")
    print(f"Clasificación: ¿Es Orden?={esOrden(m)}, ¿Es Equivalencia?={esEquivalencia(m)}\n")