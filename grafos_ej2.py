# Ejercicio 2

import json
from grafos_ej1 import leer_grafo_json

def es_reflexiva(matriz):
    for i in range(len(matriz)):
        if matriz[i][i] != 1:
            return False
    return True

def es_simetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1 and matriz[j][i] != 1:
                return False
    return True

def es_antisimetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i != j and matriz[i][j] == 1 and matriz[j][i] == 1:
                return False
    return True

def es_transitiva(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j]:
                for k in range(n):
                    if matriz[j][k] and not matriz[i][k]:
                        return False
    return True

def tipo_de_relacion(matriz):
    reflexiva = es_reflexiva(matriz)
    simetrica = es_simetrica(matriz)
    antisimetrica = es_antisimetrica(matriz)
    transitiva = es_transitiva(matriz)

    print(f"Reflexiva: {reflexiva}")
    print(f"Simétrica: {simetrica}")
    print(f"Antisimétrica: {antisimetrica}")
    print(f"Transitiva: {transitiva}")

    if reflexiva and simetrica and transitiva:
        print("Es una relación de equivalencia.")
    elif reflexiva and antisimetrica and transitiva:
        print("Es un orden parcial.")
    else:
        print("No es ni equivalencia ni orden.")

if __name__ == "__main__":
    nodos, matriz, idx = leer_grafo_json('./archivos_ej2/01.json')

    print("\nAnálisis de propiedades:")
    tipo_de_relacion(matriz)
