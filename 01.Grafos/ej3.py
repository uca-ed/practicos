
import os
import json
import pandas as pd
from collections import deque

def paso(M, ini, fin):
    if ini == fin:
        return [ini]

    queue = deque([[ini]])
    visitados = {ini}

    while queue:
        paso_actual = queue.popleft()
        ultimo_nodo = paso_actual[-1]

        vecinos = M.loc[ultimo_nodo][M.loc[ultimo_nodo] == 1].index

        for vecino in vecinos:
            if vecino not in visitados:
                if vecino == fin:
                    return paso_actual + [vecino]
                
                visitados.add(vecino)
                queue.append(paso_actual + [vecino])
                
    return None


## EJEMLPOS

def matrizAdy(G):
    P = G["P"]
    E = G["E"]
    salidas = [n1 for n1, llegada in E.items() for _ in llegada]
    llegadas = [n2 for llegada in E.values() for n2 in llegada]
    M = pd.crosstab(
        index=salidas, columns=llegadas).reindex(
            index=P, columns=P, fill_value=0)
    return M

ejemplos = {}

for nombre_archivo in os.listdir("archivos_ej3"):
    if nombre_archivo.endswith('.json'):
        ruta_completa = os.path.join("archivos_ej3", nombre_archivo)
        with open(ruta_completa, 'r') as f:
            data = json.load(f)
        
        G = {"P": data['P'], "E": data['E']}
        ejemplos[nombre_archivo.replace('.json', '')] = matrizAdy(G)

