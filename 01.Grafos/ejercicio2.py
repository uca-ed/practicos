# CONSIGNA EJERCICIO 2 : 
# Verificar si un grafo dado cumple las propiedades de Reflexividad, Simetría, Antisimetría y Transitividad. 
# Luego, debe decidir si el grafo es un orden o es corresponde a una relación de equivalencia.

import json

def crearMatrizAdyacencia(estructura):
    nodos = estructura["P"]
    arcos = estructura["E"]
    
    matriz = []
    for i in nodos:
        matAux = []
        if i in arcos:
            lst = estructura["E"][i]
            for j in range(1,len(nodos)+1):
                if str(j) in lst:
                    matAux.append(1)
                else:
                    matAux.append(0)
        else:
            for k in range(len(nodos)): matAux.append(0)
        matriz.append(matAux)

    return matriz

def reflexiva(matriz):
    n=len(matriz)
    for i in range(n):
        if matriz[i][i] != 1:
            return False
    return True

def simetrica(matriz):
    n=len(matriz)
    for i in range(n):
        for j in range (n):
            if matriz[i][j]!=matriz[j][i]:
                return False
    return True

def antisimetrica(matriz):
    n=len(matriz)
    for i in range(n):
        for j in range(n):
            if i!=j:
                if matriz[i][j]==1 and matriz[j][i]==1:
                    return False
    return True

def transitiva(matriz):
    n=len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz [i][j]==1:
                for k in range(n):
                    if matriz[j][k] ==1 and matriz[i][k]!=1:
                        return False
    return True

def comparable(matriz):
    n=len(matriz)
    for i in range(n):
        for j in range(n):
            if i!=j:
                if matriz[i][j]==0 and matriz[j][i]==0:
                    return False
    return True

def esOrden(matriz):
    if reflexiva(matriz) and antisimetrica(matriz) and transitiva(matriz):
        if comparable(matriz):
            print("La matriz es reflexiva, antisimetrica, transitiva y comparable. Por ende es un orden total")
        else:
            print("La matriz es reflexiva, antisimetrica y transitiva. Por ende es un orden parcial")
    else:
        print("La matriz no es un orden")

def esEquivalencia(matriz):
    if reflexiva(matriz) and simetrica(matriz) and transitiva(matriz):
        print("La matriz es reflexiva, simetrica y transitiva. Por ende es una relacion de equivalencia")
    else:
        print("La matriz no es una relacion de equivalencia")


f = open('02.json')
estructura = json.load(f)

mat = crearMatrizAdyacencia(estructura)
print("Reflexiva:",reflexiva(mat))
print("Simetrica:",simetrica(mat))
print("Antisimetrica:",antisimetrica(mat))
print("Transitiva:",transitiva(mat))
print("Comparable:",comparable(mat))
esOrden(mat)
esEquivalencia(mat)
