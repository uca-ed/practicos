""" 2. Verificar si un grafo dado cumple las propiedades de Reflexividad, Simetría, Antisimetría y Transitividad. 
    Luego, debe decidir si el grafo es un orden o es corresponde a una relación de equivalencia."""

import csv
import os

#carga:
base = os.path.dirname(__file__)
ruta1 = os.path.join(base, "archivos_ej1", "01.csv")
ruta2 = os.path.join(base, "archivos_ej1", "02.csv")
ruta3 = os.path.join(base, "archivos_ej1", "03.csv")
ruta4 = os.path.join(base, "archivos_ej1", "04.csv")


matriz1 = []
matriz2 = []
matriz3 = []
matriz4 = []

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


def esReflexiva(M):
    rta = True
    i=0
    for f in M:
        if M[i][i]!=1:
            return False
        i += 1
    return True

def esSimetrica(M):
    for j in range(len(M)):
        for i in range(len(M)):
            if(M[j][i]!=M[i][j]):
                return False
    return True

def esAntisimetricaD(M):
    rta = True
    for j in range(len(M)):
        for i in range(len(M)):
            if(j!=i and M[j][i] == 1 and M[i][j]==1):
                return False
    return True


def esTransitiva(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                for k in range(n):
                    if M[j][k] == 1 and M[i][k] == 0:
                        return False
    return True

impMatriz(matriz1)

"""if(esReflexiva(matriz1)):
    print("Ref")"""

"""if(esSimetrica(matriz1)):
    print("Sim")"""

"""if(esAntisimetricaD([[0,1,1],
                    [0,0,1],
                    [0,0,0]])):
    print("Antisim") """


"""if(esTransitiva(matriz2)):
    print("Transitiva")"""

def determinaGrupo(M):
    rta=""
    if(esReflexiva(M) and esAntisimetricaD(M) and esTransitiva(M)):
        rta = "Es de orden"
    if(esReflexiva(M) and esSimetrica(M) and esTransitiva(M)):
        rta = "Es de equivalencia"
    
    return rta

print(determinaGrupo(matriz1))