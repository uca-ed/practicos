import pandas as pd
import json
import numpy as np
import collections

def paso(matriz_np,n,x,y):
    cola=collections.deque([x])
    padres={x: None}
    while cola:
        actual=cola.popleft()
        if actual==y:
            camino=[]
            while actual is not None:
                camino.append(actual+1) #sumo 1 para que se muestre como en el json
                actual=padres[actual]
            return camino[::-1] #va de x a y
        
        for vecino in range(n):
            if matriz_np[actual, vecino]==1 and vecino not in padres:
                padres[vecino]=actual
                cola.append(vecino)
    return "No hay paso entre los nodos."


def main():
    archivo=input("Ingrese ruta de la matriz (dar vuelta las barras y sin comillas):")
    with open(archivo, 'r') as f:
        datos = json.load(f)
        
        # 1. Determinamos el tamaño según la lista de nodos 'P'
        n = len(datos["P"])
        print(f"Cargando matriz de {n}x{n}...")
        
        # 2. Creamos la matriz de adyacencia con NumPy
        matriz_np = np.zeros((n, n), dtype=int)
        
        # 3. Llenamos las aristas desde el diccionario 'E'
        for origen_str, destinos in datos["E"].items():
            fila = int(origen_str) - 1  # Ajuste de índice
            for destino_str in destinos:
                columna = int(destino_str) - 1
                matriz_np[fila, columna] = 1
        
        print("Matriz cargada con éxito.")
        x=int(input("Ingrese el valor de inicio(1 en adelante):"))-1
        y=int(input("Ingrese el valor de final(1 en adelante):"))-1
        if 0 <= x < n and 0 <= y < n:
            print("Secuencia de nodos:", paso(matriz_np,n,x,y))
        else:
            print("Valores de inicio o final fuera de rango.")
  
main()