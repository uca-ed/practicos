import csv  
import json

def leerCSV(nombre):
    matriz=[]
    matriz = []
    with open(nombre, newline='') as csvfile:
        lector = csv.reader(csvfile)
        for fila in lector:
            # Convertir cada elemento a int
            matriz.append([int(x) for x in fila])
    return matriz

def leerJSON(nombre):
    with open(nombre) as f:
        estructura = json.load(f)
    return estructura

def minimales(matriz):
    n=len(matriz)
    print("Los nodos minimales son: ")
    for j in range(n):
        entrada=0
        for i in range(n):
            if (matriz[i][j]==1):
                entrada=1
                break
        if not entrada:
            print(j, end=" ")
    print()

def maximales(matriz):
    n=len(matriz)
    print("Los nodos maximales son: ")
    for i in range(n):
        salida=0
        for j in range(n):
            if (matriz[i][j]==1):
                salida=1
                break
        if not salida:
            print(i, end=" ")
    print()

def vecindadDerecha(matriz,nodo):
    n=len(matriz)
    print(f"Vecindad derecha de {nodo}: ", end="")
    for i in range(n):
        if (matriz[nodo][i]==1):
            print(i, end=" ")
    print()

def vecindadIzquierda(matriz,nodo):
    n=len(matriz)
    print(f"Vecindad deizquierda de {nodo}: ", end="")
    for i in range(n):
        if (matriz[i][nodo]==1):
            print(i, end=" ")
    print()

def main():
    matriz = leerCSV("01.csv")
    n = len(matriz)
    print("Cantidad de nodos:", n)
    
    minimales(matriz)
    maximales(matriz)
    vecindadDerecha(matriz, 0)   # ejemplo nodo 0
    vecindadIzquierda(matriz, 0) # ejemplo nodo 0


    estructura = leerJSON("01.json")
    print("\nJSON cargado:")
    for i in estructura['E']:
        print(i)
    
    # Vecindad derecha y cardinalidad del nodo 'a'
    print("Vecindad derecha de 'a':", estructura['E']["0"])
    print("Cantidad de vecinos de 'a':", len(estructura['E']["0"]))

if __name__ == "__main__":
    main()