"""
5. Implementar en un lenguaje de programación el algoritmo de cálculo de T-Sort basado en un grafo.
De no ser posible calcularlo, indicar que la estructura es cíclica.    
> La aplicación debe soportar leer el grafo desde un archivo de disco y la salida debe ser la secuencia generada por t-sort.  
"""

import json

def leer_json(ruta):
    with open(ruta) as f:
        data = json.load(f)
    nodos = list(map(int, data["P"]))
    n = len(nodos)
    matriz = [[0]*n for _ in range(n)]
    for u, vecinos in data["E"].items():
        u = int(u) - 1
        for v in vecinos:
            v = int(v) - 1
            matriz[u][v] = 1
    return matriz, nodos

def sort(matriz):
    n = len(matriz)
    visitado = [0] * n  
    orden = []

    def dfs(u):
        if visitado[u] == 1:  
            return False
        if visitado[u] == 2:
            return True
        visitado[u] = 1
        for v in range(n):
            if matriz[u][v]:
                if not dfs(v):
                    return False
        visitado[u] = 2
        orden.append(u)
        return True

    for u in range(n):
        if visitado[u] == 0:
            if not dfs(u):
                return None  
    orden.reverse()
    return orden

if __name__ == "__main__":
    matriz, nodos = leer_json("ejemplo5.json")
    resultado = sort(matriz)
    if resultado is None:
        print("El grafo tiene ciclos. No es posible un T-Sort.")
    else:
        secuencia = [nodos[i] for i in resultado]
        print("Secuencia T-Sort:", secuencia)