import json
f = open('ed.json')
estructura = json.load(f)

def escribirCSV(arch,grafo):
    for i in range(1,len(grafo)+1):
        arch.write(",".join(map(str, grafo[str(i)])) + "\n")

def crearMatrizVacia():
    grafo = {}
    for i in range(1,len(estructura['E'])+1):
        grafo[str(i)] = []
        for j in range(len(estructura['E']["1"])):
            grafo[str(i)].append('0')
    return grafo

def esPrimo(num):
    if num == 1:
        return True
    for k in range(2, round(int(num)/2) + 1):
        if num % k == 0:
            return False
    return True

def minimales():
    # ====================     EJ 1: MINIMALES GRAFO     ====================
    e = open('01.csv',"w")

    # un minimal sera cada numero primo
    # entonces busco numeros primos y los pongo en el grafo
    grafo = crearMatrizVacia()
    primos = []
    # recorro primera fila de E (donde se guardan todos los numeros)
    for i in estructura['E']['1']:
        if esPrimo(int(i)):
            primos.append(i)
            grafo["1"][int(i)-1] = '1'
    #agrego los nodos q faltan en el resto del grafo
    for k in grafo:
        if k in primos:
            grafo[k][0] = '1'

    escribirCSV(e,grafo)
    e.close()

def maximales():
    # ====================     EJ 2: MAXIMOS GRAFO     ====================
    e = open('02.csv',"w")

    # un maximal sera cada multiplo "maximo"
    # los busco
    maximales = []
    for i in estructura["E"]:
        if estructura["E"][i][-1] not in maximales:
            maximales.append(estructura["E"][i][-1])

    # creo grafo con los datos obtenidos
    grafo = crearMatrizVacia()
    for j in range(1,len(estructura['E'])+1):
            for m in range(len(estructura['E'][str(j)])):
                if estructura['E'][str(j)][m] in maximales:
                    grafo[str(j)][m] = '1'
                    
    escribirCSV(e,grafo)
    e.close()

def vecindadDer(nodo):
    # ====================     EJ 3: VECINDAD DERECHA DE UN NODO     ====================
    e = open('03.csv',"w")

    #copio los datos de la vecindad derecha del nodo
    cadena = []
    for k in range(len(estructura['E'][nodo])):
        cadena.append(estructura['E'][nodo][k])

    #creo grafo que represente los nodos vecinos derechos
    grafo = crearMatrizVacia()
    for i in cadena:
        if i in estructura['E']:
            lst = []
            for k in range(len(estructura['E']["1"])):
                lst.append('1')
        grafo[i] = lst
        
    escribirCSV(e,grafo)
    e.close()

def vecindadIzq(nodo):
    # ====================     EJ 4: VECINDAD IZQUIERDA DE UN NODO     ====================
    e = open('04.csv',"w")

    #copio los datos de la vecindad izquierda del nodo
    cadena = []
    for i in range(1,int(nodo)+1):
        for k in range(len(estructura['E'][str(i)])):
            if int(nodo)%int(estructura['E'][str(i)][k]) == 0:
                if estructura['E'][str(i)][k] not in cadena:
                    cadena.append(estructura['E'][str(i)][k])

    #creo grafo que represente los nodos vecinos izquierdos
    grafo = crearMatrizVacia()
    for j in range(1,len(estructura['E'])+1):
        for m in range(len(estructura['E'][str(j)])):
            if estructura['E'][str(j)][m] in cadena:
                grafo[str(j)][m] = '1'

    escribirCSV(e,grafo)
    e.close()

minimales()
maximales()
vecindadDer("50")
vecindadIzq("50")

f.close()
