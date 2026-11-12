"""
Ejercicio 5: Calculo de T-Sort (orden topologico) sobre un grafo leido
desde un archivo. Si el grafo tiene ciclos, se informa que la estructura
es ciclica en lugar de calcular el orden.

Algoritmo (por eliminacion de nodos fuente, en base a Min(G) y grado de
entrada GI(x) = |L(x)|):

    1. Calcular el grado de entrada de cada nodo.
    2. Encolar los nodos con grado de entrada 0 (Min(G), las "fuentes").
    3. Mientras haya nodos disponibles:
       - Sacar un nodo, agregarlo al resultado.
       - Para cada vecino en R(x): decrementar su grado de entrada;
         si llega a 0, se vuelve disponible.
    4. Si al final no se recorrieron todos los nodos, el grafo es ciclico.

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


def tsort(nodos, aristas):
    grado_entrada = {n: 0 for n in nodos}
    r_vecindad = {n: [] for n in nodos}  # R(x): vecindad derecha

    for origen, destino in aristas:
        r_vecindad[origen].append(destino)
        grado_entrada[destino] += 1

    disponibles = [n for n in nodos if grado_entrada[n] == 0]  # Min(G)
    orden = []

    while disponibles:
        actual = disponibles.pop(0)
        orden.append(actual)
        for vecino in r_vecindad[actual]:
            grado_entrada[vecino] -= 1
            if grado_entrada[vecino] == 0:
                disponibles.append(vecino)

    if len(orden) != len(nodos):
        return None  # quedaron nodos con grado de entrada > 0 -> hay ciclo
    return orden


if __name__ == "__main__":
    ruta_defecto = os.path.join(os.path.dirname(__file__), "data", "grafo_tsort.txt")
    ruta = sys.argv[1] if len(sys.argv) > 1 else ruta_defecto

    nodos, aristas = leer_grafo(ruta)
    resultado = tsort(nodos, aristas)

    if resultado is None:
        print("La estructura es ciclica: no existe un orden T-Sort.")
    else:
        print("Secuencia T-Sort:", resultado)
