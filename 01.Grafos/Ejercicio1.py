import json

#ejercicio 1
#minimal de un grafo: son aquellos nodos para los que no existe ninguna arista dirigida desde otro vértice hacia él. En una matriz de adyacencia nos podemos dar cuenta de esto corroborando que la columna correspondiente a un nodo contenga únicamente ceros.

def leerArchivo_json(nomarch):
    f = open(nomarch)
    estructura = json.load(f)
    f.close()
    return estructura

def leerArchivo_csv(nomarch):
    arch = open(nomarch , "r")
    matriz=[]
    contador=0
    linea=arch.readline()
    while linea!="":
        lineaArr=linea.split(",")
        for i in range(len(lineaArr)):
            lineaArr[i] = int(lineaArr[i])
        matriz.append(lineaArr)
        linea=arch.readline()
        contador+=1
    arch.close()
    return matriz

def minimal_json(struct):
    minimales=[]
    for i in struct['E']:
        min=True
        for j in struct['E']:
            if (i in struct['E'][j]):
                min=False
        if min==True:
            minimales.append(i)
    return minimales

def minimal_csv(matriz):
    minimales=[]
    for i in range(len(matriz)):
        min=True
        for j in range(len(matriz)):
            if matriz[j][i]!=0:  #mantengo fija la columna
                min=False
        if min==True:
            minimales.append(i)
    return minimales  #devuelve un arreglo con los nodos minimales

def maximal_json(struct):
    maximales=[]
    for i in struct['P']:
        if ((not (i in struct['E'])) or struct['E'][i]==[]):
            maximales.append(i)
    return maximales

def maximal_csv(matriz):
    maximales=[]
    for i in range(len(matriz)):
        max=True
        for j in range(len(matriz)):
            if matriz[i][j]!=0:  #mantengo fija la columna
                max=False
        if max==True:
            maximales.append(i)
    return maximales      #devuelve un arreglo con los nodos maximales

def vecindadDer_json(struct,nodo):
    arrVecDer=struct['E'][nodo]
    return arrVecDer

def vecindadDer_csv(matriz,nodo):
    matVecDer=[]
    for i in range(len(matriz)):
        if(matriz[nodo][i]==1):
            matVecDer.append(i)
    return matVecDer   #devuelve un arreglo con la vecindad Derecha

def vecindadIzq_json(struct,nodo):
    arrVecIzq=[]
    for i in struct['E']:
        if nodo in struct['E'][i]:
            arrVecIzq.append(i)
    return arrVecIzq

def vecindadIzq_csv(matriz,nodo):
    matVecIzq=[]
    for i in range(len(matriz)):
        if(matriz[i][nodo]==1):
            matVecIzq.append(i)
    return matVecIzq   #devuelve un arreglo con la vecindad Derecha

def main():
    mat= leerArchivo_csv("01.csv")
    print(mat)
    minimales=minimal_csv(mat)
    print("los minimales (teniendo en cuenta que los nodos van de 0 a n) son:",minimales)
    print("los maximales (teniendo en cuenta que los nodos van de 0 a n) son:",maximal_csv(mat))
    nodo=1
    print("la vecindad derecha (teniendo en cuenta que los nodos van de 0 a n) del nodo",nodo,"es:",vecindadDer_csv(mat,nodo))
    nodo2=3
    print("la vecindad izquierda (teniendo en cuenta que los nodos van de 0 a n) del nodo",nodo2,"es:",vecindadIzq_csv(mat,nodo2))

    estructura = leerArchivo_json("01.json")
    print("los minimales son:",minimal_json(estructura))
    print("los maximales son:",maximal_json(estructura))
    print("la vecindad derecha del nodo '406' es:",vecindadDer_json(estructura,'406'))
    print("la vecindad izquierda del nodo '22' es:",vecindadIzq_json(estructura,'22'))
main()
