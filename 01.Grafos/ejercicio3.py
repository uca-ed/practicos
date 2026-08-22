import json
import sys


def buscar_camino(grafo, inicio, fin, visitados=None):
    if visitados is None:
        visitados = []

    visitados.append(inicio)

    if inicio == fin:
        return visitados

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            camino = buscar_camino(grafo, vecino, fin, visitados.copy())

            if camino is not None:
                return camino

    return None


def abrir_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        grafo = json.load(archivo)

    return grafo



def main():
    nombre_archivo = "esDivisorDe-200.json"
    grafo = abrir_archivo(nombre_archivo)
    inicio = input("Nodo de inicio: ")
    fin = input("Nodo de destino: ")
    camino = buscar_camino(grafo["E"], inicio, fin)
    if camino is None:
        print("No hay camino")
    else:
        print(" -> ".join(camino))

if __name__ == "__main__":
    main()
    