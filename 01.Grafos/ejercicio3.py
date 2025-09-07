
import json
from collections import deque

#Esta funcion la hizo chatgpt
def cargar_grafo(ruta_archivo):
    """
    Retorna:
        dict: diccionario con las vecindades derechas del grafo
              (estructura["E"]).
    """
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        estructura = json.load(f)
    return estructura["E"]


def obtener_camino(vecindades, origen, destino):
    """
    Parámetros:
        vecindades (dict): diccionario {nodo: [vecinos]} con la lista de adyacencia del grafo.
        origen (str): nodo de partida.
        destino (str): nodo de llegada.

    Retorna:
        list o None: lista con el camino [origen, ..., destino] si existe, o None si no hay camino.
    """
    # Cola para recorrer el grafo en anchura
    cola = deque([origen])

    # Conjunto de visitados para no repetir nodos
    visitados = set([origen])

    # Diccionario de padres: cada nodo apunta a su predecesor
    padres = {origen: None}

    # Bucle principal BFS
    while cola:
        actual = cola.popleft()  # saco el primer elemento
        if actual == destino:    # si llegamos al destino, terminamos
            break
        for vecino in vecindades.get(actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = actual
                cola.append(vecino)

    # Reconstrucción del camino si se llegó al destino
    if destino not in padres:
        return None  # no hay camino

    camino = []
    nodo = destino
    while nodo is not None:
        camino.append(nodo)
        nodo = padres[nodo]
    camino.reverse()
    return camino


def main():
    
    ruta = r"C:\Users\Fede\Documents\GitHub\practicos\01.Grafos\archivos_ej3\esDivisorDe-200.json"

    # Nodos de origen y destino como strings, porque así vienen en los JSON
    origen = "1"
    destino = "54"

    # Cargo el grafo y ejecuto la búsqueda
    grafo = cargar_grafo(ruta)
    camino = obtener_camino(grafo, origen, destino)

    # Salida
    if camino:
        print("Camino encontrado:", " -> ".join(camino))
    else:
        print(f"No existe camino entre {origen} y {destino}")


if __name__ == "__main__":
    main()
