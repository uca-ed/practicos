# Ejercicio 1

import json
import csv

def leer_grafo_csv(path):
    matriz = []

    with open(path, newline='') as f:
        lector = csv.reader(f)
        for fila in lector:
            # Convertir cada valor a entero
            fila_entera = [int(valor) for valor in fila]
            matriz.append(fila_entera)

    # Los nodos son identificados por su índice (como strings)
    cantidad_nodos = len(matriz)
    nodos = [str(i) for i in range(cantidad_nodos)]

    # Crear índice de mapeo nodo -> posición
    idx = {}
    for i in range(cantidad_nodos):
        idx[nodos[i]] = i

    return nodos, matriz, idx

def leer_grafo_json(path):
    with open(path, 'r') as f:
        estructura = json.load(f)

    nodos = estructura["P"]
    arcos = estructura["E"]
    cantidad_nodos = len(nodos)

    # Crear diccionario de índice de cada nodo
    idx = {}
    i = 0
    while i < cantidad_nodos:
        nodo = nodos[i]
        idx[nodo] = i
        i += 1

    # Inicializar matriz de adyacencia con ceros
    matriz = []
    fila = 0
    while fila < cantidad_nodos:
        matriz.append([0] * cantidad_nodos)
        fila += 1

    # Completar matriz con los arcos
    for origen in arcos:
        lista_destinos = arcos[origen]
        for destino in lista_destinos:
            i = idx[origen]
            j = idx[destino]
            matriz[i][j] = 1

    return nodos, matriz, idx

# Vecindad derecha: nodos p tales que (x, p) pertenece a E
def vecindad_derecha(x, matriz):
    vecinos = []
    for p in range(len(matriz)):
        if matriz[x][p] == 1:
            vecinos.append(p)
    return vecinos

# Vecindad izquierda: nodos p tales que (p, x) pertenece a E
def vecindad_izquierda(x, matriz):
    vecinos = []
    for p in range(len(matriz)):
        if matriz[p][x] == 1:
            vecinos.append(p)
    return vecinos

# Minimales: nodos p cuya vecindad izquierda es nula
def minimales(matriz):
    fuentes = []
    for p in range(len(matriz)):
        if not vecindad_izquierda(p, matriz):
            fuentes.append(p)
    return fuentes

# Maximales: nodos p cuya vecindad derecha es nula
def maximales(matriz):
    sumideros = []
    for p in range(len(matriz)):
        if not vecindad_derecha(p, matriz):
            sumideros.append(p)
    return sumideros

def main():
    ruta = './archivos_ej1/01.json' # cambiar por .csv
    nodos, grafo, idx = leer_grafo_json(ruta) # leer_grafo_csv si es .csv

    print("\nMinimales:", [nodos[i] for i in minimales(grafo)])
    print("Maximales:", [nodos[i] for i in maximales(grafo)])

    nodo = "1000"
    print(f"Vecindad derecha de {nodo}:", [nodos[i] for i in vecindad_derecha(idx[nodo], grafo)])
    print(f"Vecindad izquierda de {nodo}:", [nodos[i] for i in vecindad_izquierda(idx[nodo], grafo)])

main()