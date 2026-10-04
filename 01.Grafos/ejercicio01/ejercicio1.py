import csv

def main():
    matriz = LeerArchivo();

    nodoDere = int(input("Vecidad Derecha del nodo: "))
    print();
    a = VecindadDerecha(matriz, nodoDere-1) 
    print ( indiceReal(a));
    print()

    nodoIzq = int(input("Vecidad Izquierda del nodo: "))
    b = VecindadIzquierda(matriz, nodoIzq-1)
    print( indiceReal(b) )
    print()

    print("\n----------------------Minimales de la matriz----------------------")
    print (indiceReal(Minimales(matriz)))

    print("\n----------------------Maximales de la matriz----------------------")
    print (indiceReal(Maximales(matriz)))




def LeerArchivo():
    matriz = [];

    with open('01.csv', mode='r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            fila_numeros = [int(valor) for valor in fila];
            #print(fila)  # Cada fila es una lista de texto
            matriz.append(fila_numeros);

    return matriz;

      

def VecindadDerecha(matriz, nodo):
    # x es el índice numérico del nodo analizado
    vecinos = []
    fila = matriz[nodo];
    
    for columna in range(len(fila)):
        if fila[columna] == 1:
            vecinos.append(columna);

    return vecinos

def VecindadIzquierda(matriz, nodo):
    vecinos = [] 

    for fila in range(len(matriz)):
        if matriz[fila][nodo] == 1 :
            vecinos.append(fila);

    return vecinos;

def indiceReal(nodos):
    for n in range(len(nodos)):
        nodos[n]+=1;

    return nodos;

def Minimales(matriz):

    minimales = []

    for nodo in range(len(matriz)):
        if VecindadIzquierda(matriz, nodo) == []:
            minimales.append(nodo)

    return minimales;

def Maximales(matriz):
    maximales = []

    for nodo in range(len(matriz)):
        if VecindadDerecha(matriz, nodo) == []:
            maximales.append(nodo)

    return maximales;

main();




