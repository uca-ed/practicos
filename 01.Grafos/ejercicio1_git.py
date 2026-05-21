import csv
import json


def leer_csv(archivo):
    matriz = []
    f = open(archivo, 'r')
    lector = csv.reader(f)
    for fila in lector:
        fila_numeros = []
        for numero in fila:
            fila_numeros.append(int(numero))
        matriz.append(fila_numeros)
    f.close()
    return matriz

def leer_json(archivo):
    f = open(archivo, 'r')
    grafo = json.load(f)
    f.close()
    return grafo

#operadores csv

def vecindad_derecha_csv(matriz, nodo):
    vecinos = []
    for i in range(len(matriz)):
        if matriz[nodo][i] == 1:
            vecinos.append(i)
    return vecinos

def vecindad_izquierda_csv(matriz, nodo):
    vecinos = []
    for i in range(len(matriz)):
        if matriz[i][nodo] == 1:
            vecinos.append(i)
    return vecinos

def minimales_csv(matriz):
    mins = []
    for i in range(len(matriz)):
        # Si la vecindad izquierda está vacía, es minimal
        if len(vecindad_izquierda_csv(matriz, i)) == 0:
            mins.append(i)
    return mins

def maximales_csv(matriz):
    maxs = []
    for i in range(len(matriz)):
        # Si la vecindad derecha está vacía, es maximal
        if len(vecindad_derecha_csv(matriz, i)) == 0:
            maxs.append(i)
    return maxs

#operadores JSON

def vecindad_derecha_json(grafo, nodo):
    # Si el nodo tira flechas, devolvemos a quiénes le tira
    if nodo in grafo['E']:
        return grafo['E'][nodo]
    else:
        return []

def vecindad_izquierda_json(grafo, nodo):
    vecinos = []
    for origen in grafo['E']:
        destinos = grafo['E'][origen]
        if nodo in destinos:
            vecinos.append(origen)
    return vecinos

def obtener_todos_los_nodos(grafo):
    # Armamos una lista con todos los nodos que existen en el JSON
    nodos = []
    for origen in grafo['E']:
        if origen not in nodos:
            nodos.append(origen)
        for destino in grafo['E'][origen]:
            if destino not in nodos:
                nodos.append(destino)
    return nodos

def minimales_json(grafo):
    mins = []
    nodos = obtener_todos_los_nodos(grafo)
    for nodo in nodos:
        if len(vecindad_izquierda_json(grafo, nodo)) == 0:
            mins.append(nodo)
    return mins

def maximales_json(grafo):
    maxs = []
    nodos = obtener_todos_los_nodos(grafo)
    for nodo in nodos:
        if len(vecindad_derecha_json(grafo, nodo)) == 0:
            maxs.append(nodo)
    return maxs


#ejecuciones


print("--- PRUEBA CSV ---")
matriz_csv = leer_csv('01.csv')
print("Matriz cargada:")
for fila in matriz_csv:
    print(fila)


print("Minimales:", minimales_csv(matriz_csv))
print("Maximales:", maximales_csv(matriz_csv))
print("Vecindad Derecha de 0:", vecindad_derecha_csv(matriz_csv, 0))
print("Vecindad Izquierda de 0:", vecindad_izquierda_csv(matriz_csv, 0))


print("\n JSON ")
grafo_json = leer_json('01.json')

primer_nodo = list(grafo_json['E'].keys())[5]

print("Minimales:", minimales_json(grafo_json))
print("Maximales:", maximales_json(grafo_json))
print(f"Vecindad Derecha de '{primer_nodo}':", vecindad_derecha_json(grafo_json, primer_nodo))
print(f"Vecindad Izquierda de '{primer_nodo}':", vecindad_izquierda_json(grafo_json, primer_nodo))
