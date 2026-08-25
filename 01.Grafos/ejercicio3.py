"""
EJERCICIO 3 - Obtencion del paso (camino) de un nodo a otro de un grafo.

La aplicacion:
  1. Lee un grafo dirigido desde un archivo .json de disco.
  2. Dado un nodo ORIGEN y un nodo DESTINO, busca un camino entre ellos.
  3. La salida es la SECUENCIA de nodos a recorrer para recrear el paso:
        origen -> n1 -> n2 -> ... -> destino

Algoritmo: BUSQUEDA EN ANCHURA (BFS) con listas ABIERTA y CERRADA.

    - ABIERTA (open):   cola de nodos por explorar (descubiertos pero todavia
                        no expandidos). Es una cola FIFO.
    - CERRADA (closed): conjunto de nodos ya visitados, para no repetirlos.
    - PADRE:            por cada nodo, desde que nodo llegue a el. Sirve para
                        reconstruir el camino yendo del destino al origen y
                        dando vuelta la lista.

Como BFS expande por niveles, el primer camino que llega al destino es el
MAS CORTO (menor cantidad de pasos).

Por que BFS y no Floyd-Warshall:
    Floyd-Warshall calcula los caminos entre TODOS los pares de nodos y cuesta
    O(n^3). Para el archivo de 20000 nodos eso son ~8.000.000.000.000 de
    operaciones: inviable. BFS resuelve un par origen->destino recorriendo
    cada arista una sola vez, O(nodos + aristas), y aca es instantaneo.

Uso desde la terminal de VS Code:

    python3 camino.py esDivisorDe-200.json 1 128
    python3 camino.py multiplos200Ref.json 128 8
    python3 camino.py esDivisorDe-200.json        (pide origen y destino)
    python3 camino.py                             (pide todo por teclado)
"""

import json
import os
import re
import sys
from collections import deque


# ======================================================================
# 1. Lectura del grafo (lista de adyacencia)
# ======================================================================

def leer_json(ruta):
    """Lee {"P": [...nodos...], "E": {nodo: [vecinos...]}} y devuelve
    (nodos, ady), donde ady[nodo] = lista de sucesores directos.

    Es tolerante a una coma de mas antes de } o ] (el archivo
    esDivisorDe-20000.json la trae y romperia json.load)."""
    with open(ruta, encoding="utf-8") as f:
        texto = f.read()
    try:
        datos = json.loads(texto)
    except json.JSONDecodeError:
        datos = json.loads(reparar_json(texto))

    nodos = datos["P"]
    ady = {n: [] for n in nodos}
    for origen, vecinos in datos["E"].items():
        ady[origen] = list(vecinos)     # el bucle a->a, si viene, no molesta
    return nodos, ady


def reparar_json(texto):
    """Arregla dos defectos que trae esDivisorDe-20000.json:
       1) comas colgantes antes de } o ]   ->  se sacan
       2) le falta la llave } de cierre     ->  se agregan las que falten
    (cuenta { y [ que quedaron abiertos y los cierra al final)."""
    texto = re.sub(r",(\s*[\]}])", r"\1", texto)
    faltan_llaves = texto.count("{") - texto.count("}")
    faltan_corch = texto.count("[") - texto.count("]")
    return texto + "]" * max(0, faltan_corch) + "}" * max(0, faltan_llaves)


# ======================================================================
# 2. Busqueda del camino: BFS con listas abierta y cerrada
# ======================================================================

def buscar_camino(ady, origen, destino):
    """Devuelve [origen, ..., destino] o None si no hay camino."""
    if origen == destino:
        return [origen]

    abierta = deque([origen])     # cola de nodos por expandir
    cerrada = {origen}            # nodos ya visitados
    padre = {origen: None}        # de donde llegue a cada nodo

    while abierta:
        actual = abierta.popleft()
        for vecino in ady.get(actual, ()):
            if vecino in cerrada:
                continue
            padre[vecino] = actual
            if vecino == destino:
                return reconstruir(padre, destino)
            cerrada.add(vecino)
            abierta.append(vecino)
    return None


def reconstruir(padre, destino):
    """Sigue los punteros 'padre' del destino al origen y da vuelta la lista."""
    camino = []
    nodo = destino
    while nodo is not None:
        camino.append(nodo)
        nodo = padre[nodo]
    camino.reverse()
    return camino


# ======================================================================
# 3. Programa principal
# ======================================================================

def main():
    args = sys.argv[1:]
    ruta = args[0] if len(args) > 0 else input("Archivo del grafo (.json): ").strip()

    nodos, ady = leer_json(ruta)
    aristas = sum(len(v) for v in ady.values())
    print(f"\nGrafo cargado: {len(nodos)} nodos, {aristas} aristas.")
    print("(Enter en el origen para salir)\n")

    origen_cli = args[1] if len(args) > 1 else None
    destino_cli = args[2] if len(args) > 2 else None

    primera_vez = True
    while True:
        if primera_vez and origen_cli is not None:
            origen = origen_cli
        else:
            origen = input("Origen : ").strip()
        if origen == "":
            break

        if primera_vez and destino_cli is not None:
            destino = destino_cli
        else:
            destino = input("Destino: ").strip()
        primera_vez = False

        if origen not in ady:
            print(f"  El nodo '{origen}' no existe.\n"); continue
        if destino not in ady:
            print(f"  El nodo '{destino}' no existe.\n"); continue

        camino = buscar_camino(ady, origen, destino)
        if camino is None:
            print(f"  No existe un camino de {origen} a {destino}.\n")
        else:
            print(f"  Camino ({len(camino) - 1} paso(s)):")
            print("  " + " -> ".join(camino) + "\n")

        if origen_cli is not None and destino_cli is not None:
            break


if __name__ == "__main__":
    main()
