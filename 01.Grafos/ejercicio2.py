# CONSIGNA EJERCICIO 2 : 
# Verificar si un grafo dado cumple las propiedades de Reflexividad, Simetría, Antisimetría y Transitividad. 
# Luego, debe decidir si el grafo es un orden o es corresponde a una relación de equivalencia.

import json
import zipfile

def leer_matriz(rutaZip,nombreArch):
    with zipfile.ZipFile(rutaZip, "r") as z:
        with z.open(nombreArch) as f:
            datos = json.load(f)
    return datos["P"]
# VER BIEN ESTA FUNCION


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

def esOrdenParcial(matriz):
    if reflexiva(matriz) and antisimetrica(matriz) and transitiva(matriz):
        print("La matriz es reflexiva, antisimetrica y transitiva. Por ende es un orden parcial")
    else:
        print("La matriz no es un orden parcial")

def esOrdenTotal(matriz):
    if esOrdenParcial(matriz) and comparable(matriz):
        print("Además, es comparable. Por ende es un orden total")
    else:
        print("La matriz no es un orden total")

def esEquivalencia(matriz):
    if reflexiva(matriz) and simetrica(matriz) and transitiva(matriz):
        print("La matriz es reflexiva, simetrica y transitiva. Por ende es una relacion de equivalencia")
    else:
        print("La matriz no es una relacion de equivalencia")


