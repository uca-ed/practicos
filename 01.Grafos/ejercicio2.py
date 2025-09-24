"""
2. Verificar si un grafo dado cumple las propiedades de Reflexividad, Simetría, Antisimetría y Transitividad. Luego, debe decidir si el grafo es un orden o es corresponde a una relación de equivalencia.

>  Utilizar los archivos provistos en el directorio archivos_ej2.zip 
"""

import json

# =============================
# Lectura de grafos
# =============================

def leer_json(ruta):
    with open(ruta) as f:
        data = json.load(f)
    nodos = list(map(int, data["P"]))
    n = len(nodos)
    matriz = [[0]*n for _ in range(n)]
    for u, vecinos in data["E"].items():
        u = int(u) - 1
        for v in vecinos:
            v = int(v) - 1
            matriz[u][v] = 1
    return matriz, nodos

# =============================
# Operadores sobre la matriz
# =============================

def es_reflexiva(matriz):
    n = len(matriz)
    for i in range(n):
        if matriz[i][i] != 1:
            return False
    return True

def es_simetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
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
            if matriz[i][j] == 1:
                for k in range(n):
                    if matriz[j][k] == 1 and matriz[i][k] == 0:
                        return False
    return True

# =============================
# Análisis del tipo de relación
# =============================

def tipo_relacion(matriz):
    reflexiva = es_reflexiva(matriz)
    simetrica = es_simetrica(matriz)
    antisimetrica = es_antisimetrica(matriz)
    transitiva = es_transitiva(matriz)

    print("Reflexiva:", reflexiva)
    print("Simetrica:", simetrica)
    print("Antisimetrica:", antisimetrica)
    print("Transitiva:", transitiva)

    if reflexiva and simetrica and transitiva:
        return "Relacion de equivalencia"
    elif reflexiva and antisimetrica and transitiva:
        return "Orden parcial"
    else:
        return "No es ni equivalencia ni orden parcial"

# =============================
# Ejemplo de uso
# =============================

if __name__ == "__main__":
    print("Ej 1")
    matriz, nodos = leer_json("01.json")
    resultado = tipo_relacion(matriz)
    print("Tipo de relacion:", resultado)
    
    print("\nEj 2")
    matriz, nodos = leer_json("02.json")
    resultado = tipo_relacion(matriz)
    print("Tipo de relacion:", resultado)
    
    print("\nEj 3")
    matriz, nodos = leer_json("03.json")
    resultado = tipo_relacion(matriz)
    print("Tipo de relacion:", resultado)