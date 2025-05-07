# Ejercicio 3

import json
from grafos_ej1 import leer_grafo_json

def paso(grafo, inicio, destino, camino=None, visitados=None):
    if camino is None:
        camino = []
    if visitados is None:
        visitados = []

    camino.append(inicio)
    visitados.append(inicio)

    if inicio == destino:
        return camino

    vecinos = []
    for indice in range(len(grafo[inicio])):
        if grafo[inicio][indice] == 1:
            vecinos.append(indice)

    for vecino in vecinos:
        if vecino not in visitados:
            resultado = paso(grafo, vecino, destino, camino.copy(), visitados.copy())
            if resultado is not None:
                return resultado

    return None  # No hay camino

def main():
    ruta = "./archivos_ej3/esDivisorDe-200.json"
    nodos, grafo, idx = leer_grafo_json(ruta)

    print("Matriz de adyacencia:")
    for fila in grafo:
        print(fila)

    origen = 2
    destino = 4

    camino = paso(grafo, origen, destino)

    if camino:
        print(f"Camino de '{origen}' a '{destino}': {' -> '.join(map(str, camino))}")
    else:
        print(f"No hay camino de '{origen}' a '{destino}'")

main()