"""
Ejercicio 7: Sort topologico sobre un grafo dado como dato en un archivo.

Se resuelve con un enfoque distinto al del ejercicio 5 (que elimina nodos
fuente en base al grado de entrada): aca se usa una recorrida en
profundidad (DFS). Cada nodo se agrega al resultado cuando se terminan de
visitar todos sus descendientes (postorden), y el orden topologico es el
postorden invertido. Si durante la recorrida se encuentra un nodo que ya
esta en la pila de llamadas actual, hay un ciclo.

Formato del archivo de grafo (una arista por linea):
    origen,destino
"""

import os
import sys


def leer_grafo(ruta):
    nodos = set()
    aristas = []
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            origen, destino = [x.strip() for x in linea.split(",")]
            aristas.append((origen, destino))
            nodos.add(origen)
            nodos.add(destino)
    return nodos, aristas


def sort_topologico_dfs(nodos, aristas):
    r_vecindad = {n: [] for n in nodos}
    for origen, destino in aristas:
        r_vecindad[origen].append(destino)

    visitado = {n: False for n in nodos}
    en_pila_actual = {n: False for n in nodos}
    resultado = []
    hay_ciclo = False

    def dfs(nodo):
        nonlocal hay_ciclo
        visitado[nodo] = True
        en_pila_actual[nodo] = True
        for vecino in r_vecindad[nodo]:
            if hay_ciclo:
                return
            if en_pila_actual[vecino]:
                hay_ciclo = True
                return
            if not visitado[vecino]:
                dfs(vecino)
        en_pila_actual[nodo] = False
        resultado.append(nodo)  # postorden

    for nodo in nodos:
        if hay_ciclo:
            break
        if not visitado[nodo]:
            dfs(nodo)

    if hay_ciclo:
        return None

    resultado.reverse()
    return resultado


if __name__ == "__main__":
    ruta_defecto = os.path.join(os.path.dirname(__file__), "data", "grafo_topologico.txt")
    ruta = sys.argv[1] if len(sys.argv) > 1 else ruta_defecto

    nodos, aristas = leer_grafo(ruta)
    resultado = sort_topologico_dfs(nodos, aristas)

    if resultado is None:
        print("La estructura es ciclica: no existe un orden topologico.")
    else:
        print("Secuencia de orden topologico:", resultado)
