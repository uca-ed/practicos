'''
3. Implementar el algoritmo de obtención de paso de un nodo a otro de un grafo.
La aplicación debe soportar leer el grafo desde un archivo de disco y
la salida debe ser una secuencia con los nodos a recorrer para recrear el paso.
'''

import json

# =============================
# Lectura de grafos
# =============================

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

# =============================
# Algoritmo de obtención de paso
# =============================

def obtener_camino_simple(matriz, nodos, origen, destino):
    n = len(nodos)
    idx_origen = nodos.index(origen)
    idx_destino = nodos.index(destino)
    OPEN = [(idx_origen, None)]
    CLOSED = []

    while OPEN:
        actual, padre = OPEN.pop(0)
        CLOSED.append((actual, padre))
        if actual == idx_destino:
            break
        for vecino in range(n):
            if matriz[actual][vecino] == 1 and not any(v == vecino for v, _ in CLOSED) and not any(v == vecino for v, _ in OPEN):
                OPEN.append((vecino, actual))

    camino = []
    actual = idx_destino
    padres = {v: p for v, p in CLOSED}
    if actual not in padres and actual != idx_origen:
        return None
    while actual is not None:
        camino.append(nodos[actual])
        actual = padres.get(actual, None)
    camino.reverse()
    return camino

# =============================
# Ejemplo de uso
# =============================

if __name__ == "__main__":
    
    matriz, nodos = leer_json("esDivisorDe-20000.json")

    origen = 2
    destino = 50

    camino = obtener_camino_simple(matriz, nodos, origen, destino)

    print("\nResultado:")
    if camino:
        print("Secuencia de nodos a recorrer:", " -> ".join(map(str, camino)))
    else:
        print("No existe un camino entre los nodos indicados.")