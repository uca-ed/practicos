import json
from collections import deque
 
 
def leer_grafo(nombre_archivo):
    f = open(nombre_archivo)
    estructura = json.load(f)
    f.close()
    return estructura['P'], estructura['E']
 
 
def vecinos(grafo, nodo):
    # no todos los nodos tienen vecindad derecha, por eso el get con lista vacia
    return grafo.get(nodo, [])
 
 
def obtener_camino(nodos, grafo, origen, destino):
    if origen not in nodos or destino not in nodos:
        return None
 
    if origen == destino:
        return [origen]
 
    visitados = {origen}
    anterior = {}
    cola = deque([origen])
 
    while cola:
        actual = cola.popleft()
 
        for vecino in vecinos(grafo, actual):
            if vecino in visitados:
                continue
 
            anterior[vecino] = actual
            visitados.add(vecino)
 
            if vecino == destino:
                camino = [destino]
                nodo = destino
                while nodo != origen:
                    nodo = anterior[nodo]
                    camino.append(nodo)
                camino.reverse()
                return camino
 
            cola.append(vecino)
 
    return None
 
 
def main():
    archivo = input("Archivo del grafo: ")
    origen = input("Nodo origen: ")
    destino = input("Nodo destino: ")
 
    nodos, grafo = leer_grafo(archivo)
    camino = obtener_camino(nodos, grafo, origen, destino)
 
    if camino is None:
        print(f"No hay camino entre {origen} y {destino}")
    else:
        print(" -> ".join(camino))
 
 
if __name__ == "__main__":
    main()