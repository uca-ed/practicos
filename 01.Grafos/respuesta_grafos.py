"""GRAFOS

EJERCICIO 1: Representar a un grafo utilizando una matriz de adyacencia. Sobre tal representación, se debe poder ejecutar los siguientes operadores:

a. Minimales del grafo
b. Maximales del grafo
c. Vecindad derecha de un nodo
d. Vecindad izquierda de un nodo
"""

import numpy as np
import pandas as pd
import json


def cargar_grafo_csv(path):
    matriz = pd.read_csv(path, header=None).values
    return matriz

def cargar_grafo_json(path):
    with open(path, 'r') as f:
        data = json.load(f)

    nodos = sorted(data["nodes"])
    n = len(nodos)
    matriz = np.zeros((n, n), dtype=int)

    for arista in data["edges"]:
        origen = nodos.index(arista["from"])
        destino = nodos.index(arista["to"])
        matriz[origen][destino] = 1

    return matriz, nodos

def nodos_minimales(matriz):

    return [i for i in range(len(matriz)) if np.sum(matriz[:, i]) == 0]

def nodos_maximales(matriz):

    return [i for i in range(len(matriz)) if np.sum(matriz[i]) == 0]

def vecindad_derecha(matriz, nodo):

    return [i for i in range(len(matriz)) if matriz[nodo][i] == 1]

def vecindad_izquierda(matriz, nodo):

    return [i for i in range(len(matriz)) if matriz[i][nodo] == 1]



matriz = cargar_grafo_csv("01.csv")
print("Minimales:", nodos_minimales(matriz))
print("Maximales:", nodos_maximales(matriz))
print("Vecindad derecha del nodo 0:", vecindad_derecha(matriz, 0))
print("Vecindad izquierda del nodo 2:", vecindad_izquierda(matriz, 2))

"""EJERCICIO 2: Verificar si un grafo dado cumple las propiedades de Reflexividad, Simetría, Antisimetría y Transitividad. Luego, debe decidir si el grafo es un orden o es corresponde a una relación de equivalencia."""

import json

def cargar_relaciones(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        data = json.load(file)
    nodos = data["P"]
    aristas = data["E"]
    relaciones = []
    for origen, destinos in aristas.items():
        for destino in destinos:
            relaciones.append((origen, destino))
    return nodos, relaciones

def es_reflexiva(nodos, relaciones):
    for nodo in nodos:
        if (nodo, nodo) not in relaciones:
            return False
    return True

def es_simetrica(relaciones):
    for a, b in relaciones:
        if (b, a) not in relaciones:
            return False
    return True

def es_antisimetrica(relaciones):
    for a, b in relaciones:
        if a != b and (b, a) in relaciones:
            return False
    return True

def es_transitiva(relaciones):
    for a, b in relaciones:
        for c, d in relaciones:
            if b == c and (a, d) not in relaciones:
                return False
    return True

def tipo_relacion(nodos, relaciones):
    reflexiva = es_reflexiva(nodos, relaciones)
    simetrica = es_simetrica(relaciones)
    antisimetrica = es_antisimetrica(relaciones)
    transitiva = es_transitiva(relaciones)

    print("Reflexiva:", reflexiva)
    print("Simétrica:", simetrica)
    print("Antisimétrica:", antisimetrica)
    print("Transitiva:", transitiva)

    if reflexiva and simetrica and transitiva:
        print("\n⇒ La relación es una **Relación de Equivalencia**.")
    elif reflexiva and antisimetrica and transitiva:
        print("\n⇒ La relación es un **Orden Parcial**.")
    else:
        print("\n⇒ La relación no es una relación de equivalencia ni un orden parcial.")


nodos, relaciones = cargar_relaciones("01.json")
tipo_relacion(nodos, relaciones)

"""EJERCICIO 3: Implementar el algoritmo de obtención de paso de un nodo a otro de un grafo. La aplicación debe soportar leer el grafo desde un archivo de disco y la salida debe ser una secuencia con los nodos a recorrer para recrear el paso.

"""

import json
from collections import deque

def cargar_grafo(desde_archivo):
    with open(desde_archivo, "r") as f:
        grafo = json.load(f)
    return grafo

def encontrar_camino(grafo, inicio, fin):
    visitados = []
    cola = deque([[inicio]])

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == fin:
            return camino

        if nodo not in visitados:
            visitados.append(nodo)
            for vecino in grafo.get(nodo, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None  # No se encontró camino

# Ejemplo de uso
grafo = cargar_grafo("esDivisorDe-200.json")
camino = encontrar_camino(grafo, "A", "E")

if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró camino entre los nodos.")
