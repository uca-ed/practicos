""" 1. Representar a un grafo utilizando una matriz de adyacencia. Sobre tal representación, 
    se debe poder ejecutar los siguientes operadores:

      a. Minimales del grafo  
      b. Maximales del grafo  
      c. Vecindad derecha de un nodo  
      d. Vecindad izquierda de un nodo  """

import csv
import os
import json

#carga:
base = os.path.dirname(__file__)
ruta1 = os.path.join(base, "archivos_ej1", "01.csv")
ruta2 = os.path.join(base, "archivos_ej1", "02.csv")
ruta3 = os.path.join(base, "archivos_ej1", "03.csv")
ruta4 = os.path.join(base, "archivos_ej1", "04.csv")
ruta_json=os.path.join(base, "archivos_ej1", "01.json")

matriz1 = []
matriz2 = []
matriz3 = []
matriz4 = []
with open(ruta_json, "r", encoding="utf-8") as f:
    datos = json.load(f)

nodos = datos["P"]        
ady = datos["E"]        
n = len(nodos)

matriz = [[0]*n for _ in range(n)]
mapa = {nodo: i for i, nodo in enumerate(nodos)}

for origen, destinos in ady.items():
    i = mapa[origen]
    for dest in destinos:
        j = mapa[dest]
        matriz[i][j] = 1

with open(ruta1, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for fila in reader:
        matriz1.append([int(x) for x in fila])

with open(ruta2, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for fila in reader:
        matriz2.append([int(x) for x in fila])

with open(ruta3, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for fila in reader:
        matriz3.append([int(x) for x in fila])

with open(ruta4, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for fila in reader:
        matriz4.append([int(x) for x in fila])


def impMatriz(M):
    print("Matriz de adyacencia:")
    for fila in M:
        print(fila) 


# A) MINIMAL DEL GRAFO  --> SIN ARISTAS ENTRANTES (fuentes)

#primero obtengo, para cada nodo, su grado de entrada: 
def gradosEntrada(matriz):
    n = len(matriz)
    in_deg = [0]*n

    for j in range(n): #voy de 0 a 5 
        s=0
        for i in range(n):
            s += matriz[i][j]
        in_deg[j] = s
    return in_deg

def minimal(inDeg):
    min=[]
    i=1
    for ele in inDeg:
        if ele == 0:
            min.append(i)
        i += 1

    if min == []:
        print("No hay nodos minimales")
    else:
        print("Minimales:")
        for x in min:
            print(x)


#minimal(gradosEntrada(matriz2))

#B) MAXIMAL DEL GRAFO --> NODO CUYO GRADO DE SALIDA = 0

def gradosSalida(matriz):
    out_deg = []
    for f in matriz:
        out_deg.append(sum(f))
    return out_deg


def maximal(outD):
    max = []
    i=1
    for ele in outD:
        if ele == 0:
            max.append(i)
        i+=1
    if(max==[]):
        print("Grafo sin maximales")
    else:
        print("maximales: ")
        for x in max:
            print(x)

#maximal(gradosSalida(matriz3))

#C) VECINDAD DERECHA DE UN NODO: NODOS A LOS QUE N APUNTA
def vecindadD(M,n):
    vd=[]
    fila = M[n-1]
    i=1
    for ap in fila:
        if ap == 1:
            vd.append(i)
        i +=1
    return vd


"""" impMatriz(matriz3)

VD= vecindadD(matriz3,2)
if VD != []:
    print("Vecindad derecha de 2:")
    for ele in VD:
        print(ele)  """

#D) VECINDAD IZQUIERDA D EUN NODO: TODOS LOS NODOS QUE APUNTAN A N

def vecindadI(M,n):
    col=[]
    vi=[]
    i=1
    for j in range(len(M)):
        col.append(M[j][n-1])
    
    for ele in col:
        if ele == 1:
            vi.append(i)
        i += 1
    return vi

"""impMatriz(matriz3)

VI = vecindadI(matriz3,4)
if VI != []:
    print("Vecindad izquierda de 4:")
    for ele in VI:
        print(ele) """