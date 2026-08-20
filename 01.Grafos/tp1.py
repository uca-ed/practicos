def leercsv():
    archivo = open("03.csv","r")
    matriz = []
    for linea in archivo:
        fila = []
        for val in linea.strip().split(","):
            fila.append(int(val))
        matriz.append(fila)
    archivo.close()
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

def leerjson():
    import json
    f = open('02.json')
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

matriz = leerjson()
minimales(matriz)
maximales(matriz)
derecha(matriz, 3)
izquierda(matriz, 1)