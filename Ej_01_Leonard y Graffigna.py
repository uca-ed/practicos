import csv
import json


#archivo = 'C:/Users/user/Documents/Facultad/Estructura/archivos_ej1/archivos_ej1/01.json'
archivo = 'C:/Users/user/Documents/Facultad/Estructura/archivos_ej1/archivos_ej1/02.csv'

#Esto es para saber si es Json o csv dado que recibimos dos tipos de archivos distintos
def obtener(arch):
    if arch[-3:] == 'csv':
        matriz = csv_matrizAdy(arch)
    else:
        matriz = json_matrizAdy(arch)
    return matriz

def json_matrizAdy(arch):
    f = open(arch)
    G = json.load(f)
    matriz = {}
    for i in G['P']:
        fila = []
        # Recorremos cada vértice de P para comprobar si hay conexión
        for f in G['P']:
            # Si el vértice 'f' está en la lista de adyacencia de 'i', se agrega 1
            if f in G['E'].get(i, []):
                fila.append("1")
            else:
                fila.append("0")
        matriz[i] = fila
    return matriz

def csv_matrizAdy(arch):
    n = open(arch)
    file = csv.reader(n, delimiter=',')
    matriz = {}
    i = 0
    for f in file:
        i += 1
        matriz[str(i)] = f
    return matriz
    
matrix = obtener(archivo) #Esto es un diccionario que contiene el numero de nodo como key + una lista anidada de 1 y 0

# Vecindad derecha de un nodo
# Vecindad izquierda de un nodo

def minimal(graph):
    P = list(graph.keys()) #Lista con mis nodos
    n = len(P)
    minimales = []
    for j in range(n): #Va a suceder una cantidad de veces igual a los nodos + j es la posicion de la columna que estoy sumando
        x = 0
        for i in P: 
            x += int(graph[i][j])
        if x == 0:
            minimales.append(P[j])
            
    if minimales:
        print(f"Los minimales del grafo son: {minimales}")
    else:
        print ("No existen minimales")
    
def maximal(graph):
    P = list(graph.keys()) #Hago una lista con los nodos
    x = 0
    for i in graph:
        fila = graph[i] #Agarro la lista del nodo
        for n in fila:
            x += int(n) #pasa de str -> int y sume
        if x != 0: #Si suma ya corta y remueve porque una fila llena de ceros es un maximal
            P.remove(i)
    if len(P) != 0: #Decidir si hay o no maximales
        print ( f"se encontraron los siguientes nodos maximales:{P}")
    else:
        print ( "Esta matriz no posee nodos maximales")
        
        
def vecindad_der(graph, n):
    if n in graph.keys():
        nodos = [] #Aca agrego los nodos
        col = 0
        fila = graph[n]
        for i in fila:
            col += 1 #podría comenzar en 1, en teoría pero me da miedo romper algo
            if i == '1':
                nodos.append(str(col))
        print (f"La vecindad derecha del nodo {n} es: {nodos}")
    else:
        print (f"El nodo {n} no existe dentro del grafo.")

def vecindad_iz(graph, n):
    nodos = list(graph.keys())
    #Me rendi y hable con chat
    if n not in nodos:
        print (f'El nodo {n} no está en el grafo.')
        return

    indice = {nodo: i for i, nodo in enumerate(nodos)} #EXPLICACIÓN PARA MI: diccionario de mapeo entre el nombre del nodo y
    #su índice en la lista de nodos. Toma cada valor en la lista, lo vuelca en un diccionario,
    #key es lo que agarra de la lista, value es el numero de la posicion, entonces depués podes iterar por valor de la columna
    
    j = indice[n] #La columna que me interesa
    vec_izq = []
    
    for i in range(len(nodos)): #Recorremos filas
        if graph[nodos[i]][j] == '1': #Encontro la pos de filas en i + la j que le interesa
            vec_izq.append(nodos[i]) #el nodo en la lista
    print (f'La vecindad izquiera del nodo {n} es: {vec_izq}')
    
def grafo(graph):
    for i in graph:
        print(graph[i])
        

grafo(matrix)
maximal(matrix)
minimal(matrix)
vecindad_der(matrix, '5')
vecindad_iz(matrix, '2')