import json
import os


def leer_json(nombre_archivo):
    ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)

    f = open(ruta)
    estructura = json.load(f)
    f.close()

    nodos = estructura["P"]
    relaciones = estructura["E"]
    matriz = []

    for i in range(len(nodos)):
        fila = []

        for j in range(len(nodos)):
            fila.append(0)

        matriz.append(fila)

    for nodo in relaciones:
        for vecino in relaciones[nodo]:
            i = nodos.index(nodo)
            j = nodos.index(vecino)
            matriz[i][j] = 1

    return nodos, matriz


def vecindad_derecha(matriz,nodos,x):
    resultado = []

    posicion = nodos.index(x)

    for j in range(len(nodos)):
        if matriz[posicion][j] == 1:
            resultado.append(nodos[j])

    return resultado

def paso(matriz, nodos, origen, destino):
    OPEN = []
    CLOSED = []

    if origen == destino:
        return [origen]

    OPEN.append((origen, None))

    encontrado = False

    while len(OPEN) > 0 and not encontrado:

        nodo, anterior = OPEN.pop(0)

        CLOSED.append((nodo, anterior))

        vecinos = vecindad_derecha(matriz, nodos, nodo)

        for vecino in vecinos:

            if vecino == destino:
                CLOSED.append((destino, nodo))
                encontrado = True
                break

            visitado = False

            for x, padre in CLOSED:
                if x == vecino:
                    visitado = True

            for x, padre in OPEN:
                if x == vecino:
                    visitado = True

            if not visitado:
                OPEN.append((vecino, nodo))

    if not encontrado:
        return []

    camino = []

    actual = destino

    while actual is not None:

        camino.insert(0, actual)

        anterior = None

        for nodo, padre in CLOSED:
            if nodo == actual:
                anterior = padre
                break

        actual = anterior

    return camino

#cambiar para probar otro archivo
nodos, matriz = leer_json("esDivisorDe-200.json")

#cambiar para probar otros nodo
origen = nodos[0]
destino = nodos[1]

resultado = paso(matriz, nodos, origen, destino)

if len(resultado) > 0:
    print("Paso encontrado:", resultado)
else:
    print("No existe un paso entre los nodos")
