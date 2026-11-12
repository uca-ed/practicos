import csv
import json
import os


def leer_csv(nombre_archivo):
    matriz = []
    ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)

    f = open(ruta)
    lector = csv.reader(f)

    for fila in lector:
        if len(fila) > 0:
            matriz.append([int(valor) for valor in fila])

    f.close()

    nodos = list(range(len(matriz)))

    return nodos, matriz


def leer_json(nombre_archivo):
    ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)

    f = open(ruta)
    estructura = json.load(f)
    f.close()

    nodos = estructura["P"]
    relaciones = estructura["E"]
    matriz = []

    for nodo in nodos:
        fila = []

        for vecino in nodos:
            if vecino in relaciones[nodo]:
                fila.append(1)
            else:
                fila.append(0)

        matriz.append(fila)

    return nodos, matriz

#x es el nodo que quiero analizar
def vecindad_derecha(matriz,nodos,x):
    resultado = []

    posicion = nodos.index(x)

    for j in range(len(nodos)):
        if matriz[posicion][j] == 1:
            resultado.append(nodos[j])

    return resultado

#x es el nodo que quiero analizar
def vecindad_izquierda(matriz,nodos,x):
    resultado = []

    posicion = nodos.index(x)

    for i in range(len(nodos)):
        if matriz[i][posicion] == 1:
            resultado.append(nodos[i])

    return resultado

def minimales(matriz,nodos):
    resultado = []

    for nodo in nodos:
        if len(vecindad_izquierda(matriz, nodos, nodo)) == 0:
            resultado.append(nodo)

    return resultado

def maximales(matriz,nodos):
    resultado = []

    for nodo in nodos:
        if len(vecindad_derecha(matriz, nodos, nodo)) == 0:
            resultado.append(nodo)

    return resultado


# se puede probar cualquier archivo json o csv cambiando el nombre

#nodos, matriz = leer_csv("01.csv")
nodos, matriz = leer_json("01.json")

print("Minimales:", minimales(matriz, nodos))
print("Maximales:", maximales(matriz, nodos))

x = nodos[0]
print("Vecindad derecha:", vecindad_derecha(matriz, nodos, x))
print("Vecindad izquierda:", vecindad_izquierda(matriz, nodos, x))
