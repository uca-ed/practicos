import csv
import json


def leer_csv(nombre_archivo):
    matriz = []

    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)

        for fila in lector:
            matriz.append([int(x) for x in fila])

    nodos = [str(i + 1) for i in range(len(matriz))]

    return matriz, nodos


def leer_json(nombre_archivo):
    with open(nombre_archivo, encoding='utf-8') as archivo:
        estructura = json.load(archivo)

    nodos = estructura['P']
    aristas = estructura['E']

    n = len(nodos)
    matriz = [[0] * n for _ in range(n)]

    posicion = {}

    for i in range(n):
        posicion[nodos[i]] = i

    for origen in aristas:
        for destino in aristas[origen]:
            i = posicion[origen]
            j = posicion[destino]
            matriz[i][j] = 1

    return matriz, nodos


def vecindad_derecha(matriz, nodos, nodo):
    posicion = nodos.index(nodo)
    resultado = []

    for j in range(len(nodos)):
        if matriz[posicion][j] == 1:
            resultado.append(nodos[j])

    return resultado


def vecindad_izquierda(matriz, nodos, nodo):
    posicion = nodos.index(nodo)
    resultado = []

    for i in range(len(nodos)):
        if matriz[i][posicion] == 1:
            resultado.append(nodos[i])

    return resultado


def minimales(matriz, nodos):
    resultado = []

    for nodo in nodos:
        if vecindad_izquierda(matriz, nodos, nodo) == []:
            resultado.append(nodo)

    return resultado


def maximales(matriz, nodos):
    resultado = []

    for nodo in nodos:
        if vecindad_derecha(matriz, nodos, nodo) == []:
            resultado.append(nodo)

    return resultado


nombre_archivo = input("Ingrese el nombre del archivo: ")

if nombre_archivo.endswith(".csv"):
    matriz, nodos = leer_csv(nombre_archivo)

elif nombre_archivo.endswith(".json"):
    matriz, nodos = leer_json(nombre_archivo)

else:
    print("Formato de archivo incorrecto")
    exit()


print()
print("Nodos:", nodos)

print()
print("Minimales:")
print(minimales(matriz, nodos))

print()
print("Maximales:")
print(maximales(matriz, nodos))

nodo = input("\nIngrese un nodo: ")

if nodo in nodos:
    print()
    print("Vecindad derecha de", nodo, ":")
    print(vecindad_derecha(matriz, nodos, nodo))

    print()
    print("Vecindad izquierda de", nodo, ":")
    print(vecindad_izquierda(matriz, nodos, nodo))

else:
    print("El nodo no existe")
