import json
import csv
def BuscarMinimal(lista):
    minimales = []
    col=0
    while(col<len(lista)):
        count=0
        fila=0
        while(fila<len(lista)):
            if(fila!=col and int(lista[fila][col])==1):
                count+=1
            fila+=1
        if(count==0):
            minimales.append(col)
        col+=1
    return minimales

def BuscarMaximal(lista):
    maximales = []
    fila = 0
    while fila < len(lista):
        count = 0
        col = 0
        while col < len(lista):
            if col != fila and int(lista[fila][col]) == 1:
                count += 1
            col += 1
        if count == 0:
            maximales.append(fila)
        fila += 1
    return maximales

def BuscarVecindadDer(lista, nodo):
    pos = []
    col=0
    while col < len(lista):
        if int(lista[nodo][col]) == 1:
            pos.append(col)
        col += 1
    return pos

def BuscarVecindadIz(lista, nodo):
    pos = []
    fila = 0
    while fila < len(lista):
        if int(lista[fila][nodo]) == 1:
            pos.append(fila)
        fila += 1
    return pos

def LeerCSV(ruta):
    f=open(ruta, "r")   
    
    arr = []
    for linea in f:
        lista = linea.strip().split(",")
        arr.append(lista)   
    f.close()
    return arr

def LeerJSON(ruta):
    f = open(ruta, "r")
    estructura = json.load(f)
    f.close()

    nodos = estructura["P"]
    n = len(nodos)

    arr = []
    for fila in range(n):
        renglon = []
        for col in range(n):
            renglon.append("0")
        arr.append(renglon)

    claves = list(estructura["E"])

    for k in range(len(claves)):
        origen = claves[k]
        i = nodos.index(origen)

        destinos = estructura["E"][origen]

        for d in range(len(destinos)):
            destino = destinos[d]
            j = nodos.index(destino)
            arr[i][j] = "1"

    return arr



def main():

    lista = LeerJSON("01.json") #Cambiar el nombre del archivo si se quiere ver otro

    print("Minimales:", BuscarMinimal(lista))
    print("Maximales:", BuscarMaximal(lista))

    nodo = 2 #Cambiar a otro nodo cuando se quuiera ver su vvecindad

    print("Vecindad Derecha del nodo", nodo, ":", BuscarVecindadDer(lista, nodo))
    print("Vecindad Izquierda del nodo", nodo, ":", BuscarVecindadIz(lista, nodo))



main()
