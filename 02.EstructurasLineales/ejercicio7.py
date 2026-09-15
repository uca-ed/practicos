import json
import os
import sys
from collections import deque

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def ruta(archivo):
    if os.path.isabs(archivo):
        return archivo
    return os.path.join(BASE_DIR, archivo)


def abrir_archivo(nombre_archivo):
    archivo = open(ruta(nombre_archivo), "r", encoding="utf-8")
    datos = json.load(archivo)
    archivo.close()

    if "E" not in datos or not isinstance(datos["E"], dict):
        raise ValueError('El archivo debe contener un diccionario "E" con las adyacencias.')

    if "P" in datos:
        nodos = list(datos["P"])
    else:
        nodos = list(datos["E"].keys())

        for vecinos in datos["E"].values():
            for vecino in vecinos:
                if vecino not in nodos:
                    nodos.append(vecino)

    grafo = {nodo: list(datos["E"].get(nodo, [])) for nodo in nodos}

    for vecinos in datos["E"].values():
        for vecino in vecinos:
            if vecino not in grafo:
                nodos.append(vecino)
                grafo[vecino] = []

    return nodos, grafo


def sort_topologico(nodos, grafo):
    # grado_entrada[x] = cantidad de aristas que llegan al nodo x
    grado_entrada = {nodo: 0 for nodo in nodos}

    for nodo in nodos:
        for vecino in grafo[nodo]:
            grado_entrada[vecino] += 1

    # Empezamos por todos los nodos minimales:
    # aquellos que no tienen ninguna arista entrante.
    cola = deque(
        nodo for nodo in nodos
        if grado_entrada[nodo] == 0
    )

    orden = []

    while cola:
        nodo = cola.popleft()
        orden.append(nodo)

        for vecino in grafo[nodo]:
            grado_entrada[vecino] -= 1

            if grado_entrada[vecino] == 0:
                cola.append(vecino)

    # Si quedaron nodos sin procesar, necesariamente hay un ciclo.
    if len(orden) != len(nodos):
        return None

    return orden


def main():
    # Se puede pasar otro archivo por línea de comandos:
    # python ejercicio7.py otro_grafo.json
    nombre_archivo = sys.argv[1] if len(sys.argv) > 1 else "grafo_prueba_ej7.json"

    try:
        nodos, grafo = abrir_archivo(nombre_archivo)
        orden = sort_topologico(nodos, grafo)

        if orden is None:
            print("No es posible realizar el Sort Topologico.")
            print("El grafo contiene al menos un ciclo.")
        else:
            print("Sort Topologico:")
            print(" -> ".join(str(nodo) for nodo in orden))

    except FileNotFoundError:
        print(f'Error: no se encontro el archivo "{nombre_archivo}".')
    except (json.JSONDecodeError, ValueError) as error:
        print(f"Error al leer el grafo: {error}")


if __name__ == "__main__":
    main()
