####################################################
#########            EJERCICIO 1           #########
####################################################

def leercsv(nombreArchivo):
    archivo = open(nombreArchivo,"r")
    matriz = []
    for linea in archivo:
        fila = []
        for val in linea.strip().split(","):
            fila.append(int(val))
        matriz.append(fila)
    archivo.close()
    return matriz

def leerjson(nombreArchivo):
    import json
    f = open(nombreArchivo)
    estructura = json.load(f)
    matriz = []
    nodos = estructura["P"]
    for fila in range(len(nodos)):
        matriz.append([0]*len(nodos))
        
    for fila in range(len(nodos)):
        nodo_origen = nodos[fila]
        
        destinos = estructura["E"].get(nodo_origen, [])
        
        for columna in range(len(nodos)):
            nodo_destino = nodos[columna] 
            
            if nodo_destino in destinos:
                matriz[fila][columna] = 1
    
    f.close()
    return matriz
    
def minimales(matriz):
    minimales = []
    for columna in range(len(matriz)):
        esMinimal = True
        for fila in range(len(matriz)):
            if matriz[fila][columna] == 1:
                esMinimal = False
                break
        if esMinimal:
            minimales.append(columna+1)
    print("Los minimales son los nodos: ", minimales)

def maximales(matriz):
    maximales = []
    nroFila = 1
    for columna in range(len(matriz)):
        esMaximal = True
        for fila in range(len(matriz)):
            if matriz[fila][columna] == 1:
                esMaximal = False
                break
        if esMaximal:
            maximales.append(nroFila)
        nroFila += 1
    print("Los maximales son los nodos: ", maximales)

def derecha(matriz, nodoElegido):
    vecindadDerecha = []
    nodo = nodoElegido-1
    for columna in range(len(matriz[nodo])):
        if matriz[nodo][columna] == 1:
            vecindadDerecha.append(columna + 1)
    print("La vecindad derecha del nodo elegido es: ", vecindadDerecha)

def izquierda(matriz, nodoElegido):
    vecindadIzquierda = []
    nodo = nodoElegido-1
    nodoIterado = 1
    for fila in range(len(matriz)):
        if matriz[fila][nodo] == 1:
            vecindadIzquierda.append(nodoIterado)
        nodoIterado += 1 
        
    print("La vecindad izquierda del nodo elegido es: ", vecindadIzquierda)

matriz = leerjson("02.json")
minimales(matriz)
maximales(matriz)
derecha(matriz, 3)
izquierda(matriz, 1)

####################################################
#########            EJERCICIO 2           #########
####################################################

def esReflexiva(matriz):
    for i in range(len(matriz)):
        if matriz[i][i] == 0:
            return False
    return True


def esSimetrica(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            if matriz[f][c]!=matriz[c][f]:
                return False
    return True

def esAntisimetrica(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            if matriz[f][c]== 1 and matriz[c][f]==1 and c!=f:
                return False
    return True

def esTransitiva(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                for k in range(n):
                    if matriz[j][k] == 1:
                        if matriz[i][k] == 0:
                            return False 
    return True

def clasificarRelacion(matriz):
    if esReflexiva(matriz) and esSimetrica(matriz) and esTransitiva(matriz):
        print("Relacion de Equivalencia")
    if esReflexiva(matriz) and esAntisimetrica(matriz) and esTransitiva(matriz):
        print("Relacion de Orden")
    return

matriz = leerjson("03.json")
esReflexiva(matriz)
esSimetrica(matriz)
esAntisimetrica(matriz)
esTransitiva(matriz)
clasificarRelacion(matriz)
