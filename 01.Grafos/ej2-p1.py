#profe disculpeme pero no entendí su código para leer el json asi que voy a proseguir a usar el de gemini que le entiendo a como funciona, disculpe
import pandas as pd
import json
import numpy as np

def relacion_orden(matriz,n):
    if reflexiva(matriz,n) and simetrica(matriz,n) and transitiva(matriz,n):
        return "Relación de equivalencia."
    elif reflexiva(matriz,n) and antisimetrica(matriz,n) and transitiva(matriz,n):
        return "Orden Parcial."
    elif reflexiva(matriz,n) and antisimetrica(matriz,n) and transitiva(matriz,n) and comparabilidad(matriz,n):
        return "Orden Total."
    else:
        return "No es ninguna."

def reflexiva(matriz,n):
    for i in range(n):
        if matriz[i][i]==0:
            return False
    return True

def simetrica(matriz,n):
    for i in range(n):
        for j in range(n):
            if matriz[i][j]!=matriz[j][i]:
                return False
    return True

def antisimetrica(matriz,n):
    for i in range(n):
        for j in range(n):
            if i!=j and matriz[i][j]==1 and matriz[j][i]==1:
                return False
    return True

def transitiva(matriz,n):
    # Optimizamos solo esta parte para que no tarde horas.
    # En lugar de 3 bucles, usamos multiplicación de matrices (regla de M^2 <= M)
    # matriz_bool es la matriz pero tratada como Verdadero/Falso
    matriz_bool = matriz.astype(bool)
    m2 = np.dot(matriz_bool, matriz_bool) # Esto hace el "i,j,k" internamente en milisegundos
    
    # Verificamos si donde hay un camino indirecto (m2), existe la flecha directa (matriz)
    # Si m2 > 0 (hay camino largo) y matriz == 0 (no hay flecha corta), no es transitiva
    if np.any((m2 > 0) & (matriz == 0)):
        return False
    return True
#    for i in range(n):
#        for j in range(n):
#            if matriz.iloc[i,j]==1:
#                for k in range(n):
#                    if matriz.iloc[j,k]==1 and matriz.iloc[i,k]!=1:
#                        return False
#    return True

def comparabilidad(matriz,n):
    for i in range(n):
        for j in range(n):
            if i!=j and matriz[i][j]!=1 and matriz[j][i]!=1:
                return False
    return True

def main():
    archivo=input("Ingrese ruta de la matriz (dar vuelta las barras y sin comillas):")
    with open(archivo, 'r') as f:
        datos=json.load(f)
        # 1. Creamos una matriz de ceros del tamaño adecuado (NxN)
    n = len(datos["P"])
    matriz_np = np.zeros((n, n), dtype=int)
        
        # 2. Llenamos con '1' donde existan aristas en el diccionario "E"
        # Restamos 1 a los valores porque tus nodos en el JSON empiezan en "1"
        # pero los índices de Python empiezan en 0.
    for origen_str, destinos in datos["E"].items():
        fila = int(origen_str) - 1
        for destino_str in destinos:
            columna = int(destino_str) - 1
            matriz_np[fila, columna] = 1
        
        # 3. Convertimos a DataFrame para que tus funciones sigan igual
    matriz=pd.DataFrame(matriz_np)
    if not matriz.empty:
        n=len(matriz)
        print("Matriz:", matriz)
        print("Es:", relacion_orden(matriz,n),"\nEs reflexiva?",reflexiva(matriz,n),"\nEs simétrica?",simetrica(matriz,n),"\nEs antisimétrica?",antisimetrica(matriz,n),"\nEs transitiva?",transitiva(matriz,n))
    else:
        print("Matriz vacía.")

main()