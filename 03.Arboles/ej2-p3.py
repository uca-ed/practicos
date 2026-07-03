#Crear un árbol AVL realizando las inserciones dadas en el archivo de datos.

import math

def crear_nodo(dato):
    return {
        "dato":dato,
        "izq":None,
        "der":None,
        "altura":1
    }

def obtener_altura(nodo):
    if nodo is None:
        return 0
    return nodo["altura"]

def obtener_balance(nodo):
    if nodo is None:
        return 0
    return obtener_altura(nodo["izq"])-obtener_altura(nodo["der"])

def rotar_derecha(y):
    x=y["izq"]
    T2=x["der"]
    x["der"]=y
    y["izq"]=T2
    y["altura"]=1+max(obtener_altura(y["izq"]), obtener_altura(y["der"]))
    x["altura"]=1+max(obtener_altura(x["izq"]), obtener_altura(x["der"]))
    return x  

def rotar_izquierda(x):
    y = x["der"]
    T2 = y["izq"]
    y["izq"] = x
    x["der"] = T2
    x["altura"]=1+max(obtener_altura(x["izq"]),obtener_altura(x["der"]))
    y["altura"]=1+max(obtener_altura(y["izq"]),obtener_altura(y["der"]))
    return y 

def insertar(raiz, dato):
    if raiz is None:
        return crear_nodo(dato)
    if dato<raiz["dato"]:
        raiz["izq"]=insertar(raiz["izq"], dato)
    elif dato>raiz["dato"]:
        raiz["der"]=insertar(raiz["der"], dato)
    else:
        return raiz  

    raiz["altura"]=1+max(obtener_altura(raiz["izq"]), obtener_altura(raiz["der"]))
    balance=obtener_balance(raiz)

    if balance>1 and dato<raiz["izq"]["dato"]:
        return rotar_derecha(raiz)
    if balance<-1 and dato>raiz["der"]["dato"]:
        return rotar_izquierda(raiz)
    if balance>1 and dato>raiz["izq"]["dato"]:
        raiz["izq"]=rotar_izquierda(raiz["izq"])
        return rotar_derecha(raiz)
    if balance<-1 and dato<raiz["der"]["dato"]:
        raiz["der"]=rotar_derecha(raiz["der"])
        return rotar_izquierda(raiz)
    return raiz

def main():
    arbol=None
    with open(r"C:\Users\danie\OneDrive\Documentos\estructura de datos\practica3\ej2.txt") as f:
        datos=f.read().split(",")
        print("Datos a insertar en el árbol AVL:", datos)
        for valor in datos:
            arbol=insertar(arbol,valor)
        print(arbol)

main()
