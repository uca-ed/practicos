import sys

# lee un grafo de un archivo donde cada linea es un arco "origen destino"

def leer_grafo(nombre):
    sucesores = {}
    grado_entrada = {}
    arch = open(nombre)
    for linea in arch:
        linea = linea.strip()
        if linea == "":
            continue
        partes = linea.split()
        origen = partes[0]
        destino = partes[1]
        if origen not in sucesores:
            sucesores[origen] = []
            grado_entrada[origen] = 0
        if destino not in sucesores:
            sucesores[destino] = []
            grado_entrada[destino] = 0
        sucesores[origen].append(destino)
        grado_entrada[destino] = grado_entrada[destino] + 1
    arch.close()
    return sucesores, grado_entrada

def sort_topologico(sucesores, grado_entrada):
    # copia el grado de entrada para no romper el original
    entrada = {}
    for n in grado_entrada:
        entrada[n] = grado_entrada[n]
    # arranca con los nodos que no tienen arcos entrantes
    pendientes = []
    for n in entrada:
        if entrada[n] == 0:
            pendientes.append(n)
    orden = []
    while len(pendientes) > 0:
        x = pendientes.pop()
        orden.append(x)
        # "elimina" x bajando el grado de entrada de sus sucesores
        for s in sucesores[x]:
            entrada[s] = entrada[s] - 1
            if entrada[s] == 0:
                pendientes.append(s)
    # si quedaron nodos sin procesar es porque hay un ciclo
    if len(orden) != len(sucesores):
        return None
    return orden


if len(sys.argv) > 1:
    archivo = sys.argv[1]
else:
    archivo = "grafo.txt"

sucesores, grado_entrada = leer_grafo(archivo)
orden = sort_topologico(sucesores, grado_entrada)
if orden is None:
    print("Hay un ciclo, no se puede ordenar.")
else:
    print("Orden topologico:", " ".join(orden))
