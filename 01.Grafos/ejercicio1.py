"""
1. Representar a un grafo utilizando una matriz de adyacencia. Sobre tal representación, se debe poder ejecutar los siguientes operadores:

      a. Minimales del grafo  
      b. Maximales del grafo  
      c. Vecindad derecha de un nodo  
      d. Vecindad izquierda de un nodo 

"""

import csv
import json

# =============================
# Lectura de grafos
# =============================

def leer_csv(ruta):
    with open(ruta, newline="") as f:
        reader = csv.reader(f)
        matriz = [list(map(int, fila)) for fila in reader]
    nodos = list(range(1, len(matriz) + 1))

    print("\nMatriz de adyacencia:")
    for fila in matriz:
        print(fila)

    return matriz, nodos

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

def minimales(matriz, nodos):
    resultado = []
    n = len(nodos)
    for j in range(n):  
        tiene_entrada = False
        for i in range(n): 
            if matriz[i][j] == 1: 
                tiene_entrada = True
                break
        if not tiene_entrada:
            resultado.append(nodos[j])
    return resultado

def maximales(matriz, nodos):
    resultado = []
    n = len(nodos)
    for i in range(n):  
        tiene_salida = False
        for j in range(n):  
            if matriz[i][j] == 1:  
                tiene_salida = True
                break
        if not tiene_salida:
            resultado.append(nodos[i])
    return resultado

def vecindad_derecha(matriz, nodos, nodo):
    resultado = []
    i = nodos.index(nodo)
    for j in range(len(nodos)):
        if matriz[i][j] == 1: 
            resultado.append(nodos[j])
    return resultado

def vecindad_izquierda(matriz, nodos, nodo):
    resultado = []
    j = nodos.index(nodo)
    for i in range(len(nodos)):
        if matriz[i][j] == 1:  
            resultado.append(nodos[i])
    return resultado

# =============================
# Ejemplo de uso
# =============================

if __name__ == "__main__":
    matriz, nodos = leer_csv("01.csv")
    
    print("\nNodos minimales:", minimales(matriz, nodos))
    print("Nodos maximales:", maximales(matriz, nodos))
    print("Vecindad derecha de 5:", vecindad_derecha(matriz, nodos, 5))
    print("Vecindad izquierda de 1:", vecindad_izquierda(matriz, nodos, 1))

    matriz, nodos = leer_csv("02.csv")
    
    print("\nNodos minimales:", minimales(matriz, nodos))
    print("Nodos maximales:", maximales(matriz, nodos))
    print("Vecindad derecha de 5:", vecindad_derecha(matriz, nodos, 5))
    print("Vecindad izquierda de 1:", vecindad_izquierda(matriz, nodos, 1))

    matriz, nodos = leer_csv("03.csv")
    
    print("\nNodos minimales:", minimales(matriz, nodos))
    print("Nodos maximales:", maximales(matriz, nodos))
    print("Vecindad derecha de 5:", vecindad_derecha(matriz, nodos, 5))
    print("Vecindad izquierda de 1:", vecindad_izquierda(matriz, nodos, 1))

    matriz, nodos = leer_csv("04.csv")
    
    print("\nNodos minimales:", minimales(matriz, nodos))
    print("Nodos maximales:", maximales(matriz, nodos))
    print("Vecindad derecha de 5:", vecindad_derecha(matriz, nodos, 5))
    print("Vecindad izquierda de 1:", vecindad_izquierda(matriz, nodos, 1))

    matriz, nodos = leer_json("01.json")
    
    print("\nNodos minimales:", minimales(matriz, nodos))
    print("Nodos maximales:", maximales(matriz, nodos))
    print("Vecindad derecha de 5:", vecindad_derecha(matriz, nodos, 5))
    print("Vecindad izquierda de 1:", vecindad_izquierda(matriz, nodos, 1))