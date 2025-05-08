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

def estructuraAMatriz(grafo):
    matriz=[]
    for i in range(len(grafo['E'])):
        matriz.append([0]*len(grafo['E']))
    for x in grafo['E']:
        for y in grafo['E'][x]:
            matriz[int(x)-1][int(y)-1]='1'
    return matriz


def matrizTranspuesta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def reflexividad(grafo):
    for node in grafo['P']:
        if node not in grafo['E'][node]:
            return False
    return True

def simetria(matriz):
    matriz_transpuesta = matrizTranspuesta(matriz)
    if(matriz == matriz_transpuesta):
        return True
    return False

def antisimetria(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == '1' and matriz[j][i] == '1' and i != j:
                return False
    return True

def transitividad(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == '1':
                for k in range(len(matriz)):
                    #print(f"i {i} j {j} k {k}")
                    if matriz[j][k] == 1 and matriz[i][k] == '0':
                        return False
    return True

def ordenORelacionDeEquivalencia(grafo):
    matriz= estructuraAMatriz(grafo)

    print("Reflexividad")
    reflex = reflexividad(grafo)
    print(f"-->{reflex}")
    print("Simetría")
    sim = simetria(matriz)
    print(f"-->{sim}")
    print("AntiSimetría")
    antisim = antisimetria(matriz)
    print(f"-->{antisim}")
    print("Transitiva")
    trans = transitividad(matriz)
    print(f"-->{trans}")

    if reflex and sim and trans:
        return ("El grafo es una relación de equivalencia.")
    elif reflex and antisim and trans:
        return ("El grafo es una relación de orden.")
    else:
        return ("El grafo no es ni una relación de equivalencia ni de orden.")


def main():
    #  Verificar si un grafo dado cumple las propiedades de Reflexividad, Simetría, Antisimetría y Transitividad. 
    # Luego, debe decidir si el grafo es un orden o es corresponde a una relación de equivalencia.

    # cargarMatrizDeAdyacencia --> para cargar un archivo csv -> devuelve una matriz
    # armarEstructuraPartiendoDeMatrizDeAdyacencia --> transforma una matriz en una estructura dictionary con 'P' y 'E'
    # cargarEstructura --> para cargar un archivo json --> devuelve una estructura dictionary con 'P' y 'E'

    grafo = cargarEstructura('03.json') 
    #grafo = armarEstructuraPartiendoDeMatrizDeAdyacencia(cargarMatrizDeAdyacencia("02.csv"))
    print(ordenORelacionDeEquivalencia(grafo))
    
    pass

main()