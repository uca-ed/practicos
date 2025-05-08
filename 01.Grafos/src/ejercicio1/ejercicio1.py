import json
import csv

def cargarMatrizDeAdyacencia(archivoCSV):
    f = open(archivoCSV)
    matriz = []
    lector = (f.read()).split('\n')
    lector.pop()
    for fila in lector:
        matriz.append(fila.split(','))
    f.close()
    return matriz

def cargarEstructura(archivoJSON):
    f = open(archivoJSON)
    grafo = json.load(f)
    f.close()
    return grafo

def armarEstructuraPartiendoDeMatrizDeAdyacencia(matriz):
    grafo={
        'P':[],
        'E':{}
    }
    E={}
    for i in range(len(matriz)):
        E[str(i+1)] = []
        grafo['P'].append(str(i+1))
        for j in range(len(matriz[i])):
            if matriz[i][j] == '1':
                E[str(i+1)].append(str(j+1))
    grafo['E']=E
    return grafo

def vecindadDerechaDeUnNodo(grafo, nodo):
    return grafo['E'][nodo]

def vecindadIzquierdaDeUnNodo(grafo, nodo):
    vec=[]
    for nodoSaliente in grafo['E']:
        if nodo in grafo['E'][nodoSaliente]:
            vec.append(nodoSaliente)
    return vec

def minimalesDeUnGrafo(grafo):
    min = []
    for node in grafo['P']:
        if(len(vecindadDerechaDeUnNodo(grafo, node)) > 0 and len(vecindadIzquierdaDeUnNodo(grafo, node)) == 0):
            min.append(node)
    return min

def maximalesDeUnGrafo(grafo):
    max = []
    for node in grafo['P']:
        if(len(vecindadDerechaDeUnNodo(grafo, node)) == 0 and len(vecindadIzquierdaDeUnNodo(grafo, node)) > 0):
            max.append(node)
    return max


def main():
    #  a. Minimales del grafo  
    #  b. Maximales del grafo  
    #  c. Vecindad derecha de un nodo  
    #  d. Vecindad izquierda de un nodo 

    # cargarMatrizDeAdyacencia --> para cargar un archivo csv -> devuelve una matriz
    # armarEstructuraPartiendoDeMatrizDeAdyacencia --> transforma una matriz en una estructura dictionary con 'P' y 'E'
    # cargarEstructura --> para cargar un archivo json --> devuelve una estructura dictionary con 'P' y 'E'

    grafo = armarEstructuraPartiendoDeMatrizDeAdyacencia(cargarMatrizDeAdyacencia("02.csv")) # cargarEstructura('01.json') 
    print(grafo)

    print("Vecindad derecha de cada nodo")
    for node in grafo['P']:
        print(f"{node} : {vecindadDerechaDeUnNodo(grafo, node)}")

    print("Vecindad izquierda de cada nodo")
    for node in grafo['P']:
        print(f"{node} : {vecindadIzquierdaDeUnNodo(grafo, node)}")

    print("Minimales del grafo (fuentes)")
    minimals=minimalesDeUnGrafo(grafo)
    if(len(minimals)>0):
        for node in minimals:
            print(f"{node} : es un Minimal")
    else:
        print("--- No tiene minimales")

    print("Maximales del grafo (sumidero)")
    maximals=maximalesDeUnGrafo(grafo)
    if(len(maximals)>0):
        for node in maximals:
            print(f"{node} : es un Maximal")
    else:
        print("--- No tiene maximales")

    pass

main()