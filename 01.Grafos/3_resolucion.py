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

def camino(matriz, nodos, desde, hasta):
    n = len(matriz)
    visitado = [False]*n
    padre = [None]*n
    cola = []
    i = nodos.index(desde)
    j = nodos.index(hasta)
    cola.append(i)
    visitado[i] = True
    while cola:
        actual = cola.pop(0)
        if actual == j:
            break
        for k in range(n):
            if matriz[actual][k] and not visitado[k]:
                visitado[k] = True
                padre[k] = actual
                cola.append(k)
    if not visitado[j]:
        return []
    secuencia = []
    x = j
    while x is not None:
        secuencia.append(nodos[x])
        x = padre[x]
    secuencia.reverse()
    return secuencia

matriz, nodos = cargar_json("esDivisorDe-200.json")
print(camino(matriz, nodos, "2", "120"))
print(camino(matriz, nodos, "5", "100"))
print(camino(matriz, nodos, "7", "120"))
print(camino(matriz, nodos, "10", "199"))
