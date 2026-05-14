import pandas as pd
import json
import numpy as np
#lo que ve con # en el main es en lo que le pedí ayuda a gemini porque sinceramente no se me ocurrió como arreglar el código para que me tome el json como con los csv que son matriz de adyacencia, por eso lo dejo con los #, mis disculpas
#para cuando vi otra vez lo que puso en git sobre los json ya lo había arreglado con gemini asi que mis disculpas pero asi va a quedar:(

def minimal(matriz): 
    minimales=[]
    for i in range(len(matriz)):
        if vecindad_izquierda(matriz,i)==[]:
            minimales.append(i)
    return minimales

def maximal(matriz):
    maximales=[]
    for i in range(len(matriz)):
        if vecindad_derecha(matriz,i)==[]:
            maximales.append(i)
    return maximales


def vecindad_derecha(matriz, valor): #sirve para el maximal
    vecinos=[]
    for i in range(len(matriz)):
        if matriz.iloc[valor,i]==1:
            vecinos.append(i)
    return vecinos
    

def vecindad_izquierda(matriz,valor): #sirve para el minimal
    vecinos=[]
    for i in range(len(matriz)):
        if matriz.iloc[i,valor]==1:
            vecinos.append(i)
    return vecinos

def main():
    archivo=input("Ingrese ruta de la matriz (dar vuelta las barras y sin comillas):")
    if archivo.endswith(".csv"):
        matriz=pd.read_csv(archivo, header=None)
        if not matriz.empty:
            print("Matriz:", matriz)
            print("Minimal:", minimal(matriz))
            print("Maximal:", maximal(matriz))
            valor=int(input("Ingrese el valor al que le gustaria buscar sus vecindades:"))
            if valor!="":
                print("Vecindad derecha:", vecindad_derecha(matriz,valor))
                print("Vecindad izquierda:", vecindad_izquierda(matriz,valor))
            else:
                print("No se ingresó un valor para buscar sus vecindades.")
        else:
            print("Matriz vacía.")
    elif archivo.endswith(".json"):
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
            print("Matriz:", matriz)
            print("Minimal:", minimal(matriz))
            print("Maximal:", maximal(matriz))
            valor=int(input("Ingrese el valor al que le gustaria buscar sus vecindades:"))
            if valor!="":
                print("Vecindad derecha:", vecindad_derecha(matriz,valor))
                print("Vecindad izquierda:", vecindad_izquierda(matriz,valor))
            else:
                print("No se ingresó un valor para buscar sus vecindades.")
        else:
            print("Matriz vacía.")
  
main()