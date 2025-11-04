"""
7. Implementar Sort topológico sobre un grafo dado como dato en un archivo.  
"""

def leer_grafo_desde_archivo():
    ruta = "EstructuraDeDatos\\ED-Practica-ed-2025-2c\\02.EstructurasLineales\\Ej7\\grafo.txt"
    archivo = open(ruta, "r", encoding="utf-8")

    lista_nodos = set()
    adyacencia = {}
    grados_entrada = {}

    for linea in archivo:
        linea = linea.strip()
        if linea == "" or linea.startswith("#"):
            continue
        
        partes = linea.split()

        if len(partes) == 1:
            u = partes[0]
            lista_nodos.add(u)
            if u not in adyacencia:
                adyacencia[u] = []
            if u not in grados_entrada:
                grados_entrada[u] = 0

        elif len(partes) == 2:
            u = partes[0]
            v = partes[1]
            lista_nodos.add(u)
            lista_nodos.add(v)

            if u not in adyacencia:
                adyacencia[u] = []
            if v not in adyacencia:
                adyacencia[v] = []

            if u not in grados_entrada:
                grados_entrada[u] = 0
            if v not in grados_entrada:
                grados_entrada[v] = 0

            adyacencia[u].append(v)
            grados_entrada[v] += 1

    archivo.close()

    return lista_nodos, adyacencia, grados_entrada


def sort_topologico(lista_nodos, adyacencia, grados_entrada):
    cola = []
    
    for nodo in lista_nodos:
        if grados_entrada[nodo] == 0:
            cola.append(nodo)

    orden = []

    while cola:
        nodo = cola.pop(0)
        orden.append(nodo)

        for vecino in adyacencia[nodo]:
            grados_entrada[vecino] -= 1
            if grados_entrada[vecino] == 0:
                cola.append(vecino)

    if len(orden) < len(lista_nodos):
        print("El grafo es ciclico. No se puede realizar sort topologico.")
    else:
        print("Orden topologico:", orden)


def ejecutar():
    nodos, ady, grados = leer_grafo_desde_archivo()
    sort_topologico(nodos, ady, grados)


ejecutar()
