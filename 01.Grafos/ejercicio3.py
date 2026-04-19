import json
from collections import deque


def obtener_camino(estructura, origen, destino):
    origen = str(origen)
    destino = str(destino)

    if origen not in estructura['P'] or destino not in estructura['P']:
        return None

    cola = deque()
    cola.append(origen)
    padre = {origen: None}

    while len(cola) > 0:
        actual = cola.popleft()
        if actual == destino:
            break
        for vecino in estructura['E'].get(actual, []):
            vecino = str(vecino)
            if vecino not in padre:
                padre[vecino] = actual
                cola.append(vecino)

    if destino not in padre:
        return None

    # reconstruyo el camino yendo para atras
    camino = []
    nodo = destino
    while nodo is not None:
        camino.append(nodo)
        nodo = padre[nodo]
    camino.reverse()
    return camino


f = open('ed.json', 'r', encoding='utf-8')
estructura = json.load(f)
f.close()

origen = input("Ingrese el nodo de origen: ")
destino = input("Ingrese el nodo de destino: ")

camino = obtener_camino(estructura, origen, destino)

if camino is None:
    print("No existe paso desde", origen, "hasta", destino)
else:
    print("Paso desde", origen, "hasta", destino, ":")
    print(camino)
