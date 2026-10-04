

import json


def main():

    nodo_origen = input("Ingresá el nodo de origen: ")
    nodo_destino = input("Ingresá el nodo de destino: ")

    with open('multiplos20000Ref.json') as f:
        grafo = json.load(f)

    resultado = obtener_paso(grafo, nodo_origen, nodo_destino)

    print(f"El paso para ir de {nodo_origen} a {nodo_destino} es: {resultado}")


def obtener_paso(grafo, nodo_origen, nodo_destino):

    OPEN = [(nodo_origen, None)]
    CLOSED = {}

    while len(OPEN) > 0:

        z, y = OPEN.pop(0)

        CLOSED[z] = y

        if z == nodo_destino:
            return recrear_camino(CLOSED, nodo_origen, nodo_destino)

        vecinos_z = VecindadDerecha(grafo, z)

        for w in vecinos_z:

            nodos_en_open = [par[0] for par in OPEN]

            if w not in CLOSED and w not in nodos_en_open:
                OPEN.append((w, z))

    return "No existe un paso entre esos nodos."


def VecindadDerecha(grafo, z):
    return grafo['E'].get(str(z), [])

def recrear_camino(CLOSED, nodo_origen, nodo_destino):

    camino = []
    nodo_actual = nodo_destino

    while nodo_actual is not None:

        camino.append(nodo_actual)

        if nodo_actual == nodo_origen:
            break

        nodo_actual = CLOSED.get(nodo_actual)

    camino.reverse()

    return camino


main()