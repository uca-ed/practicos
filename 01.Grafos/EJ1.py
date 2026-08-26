import json

def BuscarMinimal(lista, nodos):
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
            minimales.append(nodos[col])
        col+=1
    return minimales


def BuscarMaximal(lista, nodos):
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
            maximales.append(nodos[fila])

        fila += 1

    return maximales


def BuscarVecindadDer(lista, nodos, nodo):
    idx = nodos.index(nodo)
    pos = []
    col=0
    while col < len(lista):
        if int(lista[idx][col]) == 1:
            pos.append(nodos[col])
        col += 1
    return pos


def BuscarVecindadIz(lista, nodos, nodo):
    idx = nodos.index(nodo)
    pos = []
    fila = 0
    while fila < len(lista):
        if int(lista[fila][idx]) == 1:
            pos.append(nodos[fila])
        fila += 1
    return pos


def LeerCSV(ruta):
    f=open(ruta, "r")   
    
    arr = []
    for linea in f:
        lista = linea.strip().split(",")
        arr.append(lista)   
    f.close()

    nodos = list(range(len(arr)))  

    return arr, nodos


def LeerJSON(ruta):
    f = open(ruta, "r")
    estructura = json.load(f)
    f.close()
    nodos = estructura["P"]
    n = len(nodos)
    arr = []
    fila = 0
    while fila < n:
        col = 0
        renglon = []
        while col < n:
            renglon.append("0")
            col += 1
        arr.append(renglon)
        fila += 1
    claves = list(estructura["E"])

    k = 0
    while k < len(claves):
        origen = claves[k]
        i = nodos.index(origen)

        destinos = estructura["E"][origen]

        d = 0
        while d < len(destinos):
            destino = destinos[d]
            j = nodos.index(destino)
            arr[i][j] = "1"
            d += 1

        k += 1

    return arr, nodos


def main():

    lista, nodos = LeerJSON("01.json") #Cambiar el nombre del archivo si se quiere ver otro

    print("Minimales:", BuscarMinimal(lista, nodos))
    print("Maximales:", BuscarMaximal(lista, nodos))

    nodo = nodos[2] #Cambiar a otro nodo cuando se quiera ver su vecindad

    print("Vecindad Derecha del nodo", nodo, ":", BuscarVecindadDer(lista, nodos, nodo))
    print("Vecindad Izquierda del nodo", nodo, ":", BuscarVecindadIz(lista, nodos, nodo))


main()
