"""
5. Implementar en un lenguaje de programación el algoritmo de cálculo de T-Sort basado en un grafo.
De no ser posible calcularlo, indicar que la estructura es cíclica.  
> La aplicación debe soportar leer el grafo desde un archivo de disco y la salida debe ser la secuencia generada por t-sort.   
"""
def leer_grafo():
    ruta = "EstructuraDeDatos\\ED-Practica-ed-2025-2c\\02.EstructurasLineales\\Ej5\\grafo.txt"
    archivo = open(ruta, "r", encoding="utf-8")
    nodos = set()
    ady = {}
    indeg = {}
    for linea in archivo:
        s = linea.strip()
        if s == "" or s.startswith("#"):
            continue
        partes = s.split()
        if len(partes) == 1:
            u = partes[0]
            nodos.add(u)
            if u not in ady:
                ady[u] = []
            if u not in indeg:
                indeg[u] = 0
        elif len(partes) == 2:
            u, v = partes
            nodos.add(u)
            nodos.add(v)
            if u not in ady:
                ady[u] = []
            if v not in ady:
                ady[v] = []
            if u not in indeg:
                indeg[u] = 0
            if v not in indeg:
                indeg[v] = 0
            ady[u].append(v)
            indeg[v] += 1
    archivo.close()
    for u in nodos:
        if u not in ady:
            ady[u] = []
        if u not in indeg:
            indeg[u] = 0
    return nodos, ady, indeg

def t_sort(nodos, ady, indeg):
    cola = []
    for u in nodos:
        if indeg[u] == 0:
            cola.append(u)
    orden = []
    while cola:
        u = cola.pop(0)
        orden.append(u)
        for v in ady[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                cola.append(v)
    if len(orden) < len(nodos):
        print("Estructura ciclica: no es posible calcular t-sort")
    else:
        print(orden)

def ejecutar():
    nodos, ady, indeg = leer_grafo()
    t_sort(nodos, ady, indeg)

ejecutar()
