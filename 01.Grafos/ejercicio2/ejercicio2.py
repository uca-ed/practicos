import json
import os


def leer_json(nombre_archivo):
    ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)

    f = open(ruta)
    estructura = json.load(f)
    f.close()

    nodos = estructura["P"]
    relaciones = estructura["E"]
    matriz = []

    for i in range(len(nodos)):
        fila = []

        for j in range(len(nodos)):
            fila.append(0)

        matriz.append(fila)

    for nodo in relaciones:
        for vecino in relaciones[nodo]:
            i = nodos.index(nodo)
            j = nodos.index(vecino)
            matriz[i][j] = 1

    return nodos, matriz


def es_reflexiva(matriz):
    for i in range(len(matriz)):
        if matriz[i][i] == 0:
            return False

    return True

def es_simetrica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False

    return True

def es_antisimetrica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):

            if i != j:
                if matriz[i][j] == 1 and matriz[j][i] == 1:
                    return False

    return True

def es_transitiva(matriz):
    n = len(matriz)

    for i in range(n):
        for j in range(n):
            for k in range(n):

                if matriz[i][j] == 1 and matriz[j][k] == 1:
                    if matriz[i][k] == 0:
                        return False

    return True

def es_orden(matriz):
    if es_reflexiva(matriz) and es_antisimetrica(matriz) and es_transitiva(matriz):
        return True

    return False

def es_equivalencia(matriz):
    if es_reflexiva(matriz) and es_simetrica(matriz) and es_transitiva(matriz):
        return True

    return False

#cambiar nombre de archivo segun cual se quiera probar
nodos, matriz = leer_json("01.json")

print("Reflexiva:", es_reflexiva(matriz))
print("Simetrica:", es_simetrica(matriz))
print("Antisimetrica:", es_antisimetrica(matriz))
print("Transitiva:", es_transitiva(matriz))
print("Es orden:", es_orden(matriz))
print("Es equivalencia:", es_equivalencia(matriz))

