import json
import csv

def leer_csv(archivo,nodo):
    matriz=[]
    with open(archivo,'r') as archivocsv:
        lector=csv.reader(archivocsv)
        for linea in lector:
            fila=[float(x) for x in linea]
            matriz.append(fila)
    largo=len(matriz)
    # Imprimo la vecindad derecha del nodo 1
    vecindad_der=[]
    for i in range(largo):
        if matriz[nodo-1][i]==1:
            vecindad_der.append(i+1)
    print("Vecindad derecha de ",nodo,": ",vecindad_der)
    # Imprimo la vecindad izquierda del nodo 1
    vecindad_izq=[]
    for i in range(largo):
        if matriz[i][nodo-1]==1:
            vecindad_izq.append(i+1)
    print("Vecindad izquierda de ",nodo,": ",vecindad_izq)
    # Imprimo los minimales del grafo
    minimales=[]
    for i in range(largo): #Recorro las columnas
        fuente=True
        for j in range(largo): #Recorro las filas
            if matriz[j][i]==1:
                fuente=False
        if fuente:
            minimales.append(i+1)
    print("Fuentes:")
    print(minimales)
    # Imprimo los maximales del grafo
    maximales=[]
    for i in range(largo): #Recorro las filas
        sumidero=True
        for j in range(largo): #Recorro las columnas
            if matriz[i][j]==1:
                sumidero=False
        if sumidero:
            maximales.append(i+1)
    print("Sumideros:")
    print(maximales)


def leer_json(archivo,nodo):
    f = open(archivo)
    estructura = json.load(f)
    # Imprimo la vecindad derecha de a
    print("Vecindad derecha del nodo",nodo,": ")
    print (estructura['E'][nodo])
    #Imprimo la vecindad izquierda del nodo
    vecinosIzq=[]
    for nodo_origen, nodos_destino in estructura['E'].items():
        if nodo in nodos_destino:
            vecinosIzq.append(nodo_origen)
    print("Vecindad izquierda del nodo",nodo,": ")
    print(vecinosIzq)

    #Imprimo los minimales del grafo
    nodos=set(estructura['E'].keys())
    nodos_con_entrada=set()
    for nodo_origen, nodos_destino in estructura['E'].items():
        for destino in nodos_destino:
            nodos_con_entrada.add(destino)
    nodos_minimos=nodos-nodos_con_entrada
    print("Minimales del grafo: ")
    print(nodos_minimos)
    
    #Imprimo los maximales del grafo
    maximales=[]
    for nodo_origen, nodos_destino in estructura['E'].items():
        if len(nodos_destino)==0:
            maximales.append(nodo_origen)
    print("Maximales del grafo: ")
    print(maximales)
    f.close()


def main():
    archivo="01.json"
    nodo=3
    if archivo.split('.')[1]=="csv":
        leer_csv(archivo,nodo)
    elif archivo.split('.')[1]=="json":
        leer_json(archivo,str(nodo))
main()