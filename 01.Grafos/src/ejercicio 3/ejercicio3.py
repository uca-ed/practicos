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


def bfs_camino(grafo, origen, destino):
    origen = str(origen)
    destino = str(destino)

    visitados = set()
    cola = [[origen]]

    while cola:
        camino = cola[0]
        cola = cola[1:]
        nodo = camino[-1]

        if nodo == destino:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo.get(nodo, []):
                nuevo_camino = camino + [vecino]
                cola.append(nuevo_camino)

    return f"No hay camino de {origen} a {destino}"


def main():
    grafo = cargarEstructura('multiplos200Ref.json') 
    origen = 10
    destino = 50
    resultado = bfs_camino(grafo['E'], origen, destino)#***************
    print("Camino:", resultado)
    pass
main()