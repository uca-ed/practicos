def t_sort(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    grafo = {}
    grados_entrada = {} 
    for linea in lineas:
        linea = linea.strip()    
        partes = linea.split(',')
        origen = partes[0].strip()
        destino = partes[1].strip()
        if origen not in grados_entrada:
            grados_entrada[origen] = 0
        if destino not in grados_entrada:
            grados_entrada[destino] = 0
        if origen not in grafo:
            grafo[origen] = []
        grafo[origen].append(destino)
        grados_entrada[destino] += 1
    cola = []
    for nodo in grados_entrada:
        if grados_entrada[nodo] == 0:
            cola.append(nodo)
    secuenciaTSort = []
    while len(cola) > 0:
        actual = cola.pop(0)
        secuenciaTSort.append(actual)

        if actual in grafo:
            for vecino in grafo[actual]:
                grados_entrada[vecino] -= 1
                if grados_entrada[vecino] == 0:
                    cola.append(vecino)

    if len(secuenciaTSort) == len(grados_entrada): #Verificamos si hay ciclos#
        print("Secuencia del T-Sort:", secuenciaTSort)
    else:
        print("Error: La estructura es ciclica")
