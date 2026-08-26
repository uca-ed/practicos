import json


def leer_grafo(nombre_archivo):
    with open(nombre_archivo, encoding='utf-8') as archivo:
        estructura = json.load(archivo)

    return estructura


def vecindad_derecha(estructura, nodo):
    if nodo in estructura['E']:
        return estructura['E'][nodo]

    return []


def buscar_paso(estructura, origen, destino):
    origen = str(origen)
    destino = str(destino)

    if origen not in estructura['P'] or destino not in estructura['P']:
        return None

    # OPEN guarda pares (nodo_actual, nodo_anterior)
    # CLOSED guarda los pares ya tratados
    OPEN = [(origen, None)]
    CLOSED = []

    while OPEN != []:

        z, y = OPEN.pop(0)
        CLOSED.append((z, y))

        if destino in vecindad_derecha(estructura, z):
            CLOSED.append((destino, z))
            break

        nodos_open = [par[0] for par in OPEN]
        nodos_closed = [par[0] for par in CLOSED]

        for w in vecindad_derecha(estructura, z):

            if w not in nodos_open and w not in nodos_closed:
                OPEN.append((w, z))

    # Si el destino no aparece en CLOSED, no existe paso
    nodos_closed = [par[0] for par in CLOSED]

    if destino not in nodos_closed:
        return None

    # Reconstrucción de la secuencia de nodos
    camino = []
    actual = destino

    while actual is not None:
        camino.append(actual)

        anterior = None

        for nodo, padre in CLOSED:
            if nodo == actual:
                anterior = padre
                break

        actual = anterior

    camino.reverse()

    return camino


nombre_archivo = input("Ingrese el nombre del archivo JSON: ")

estructura = leer_grafo(nombre_archivo)

origen = input("Ingrese el nodo de origen: ")
destino = input("Ingrese el nodo de destino: ")

camino = buscar_paso(estructura, origen, destino)

print()

if camino is None:
    print("No existe un paso entre", origen, "y", destino)

else:
    print("Paso encontrado:")
    print(" -> ".join(camino))
