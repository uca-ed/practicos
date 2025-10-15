from collections import defaultdict, deque
import json

def leerGrafoJson(archivo):
    with open(archivo, "r") as f:
        datos = json.load(f)
    return datos

def tSort(grafo):
    indeg = {nodo: 0 for nodo in grafo}
    for origen in grafo:
        for destino in grafo[origen]:
            indeg[destino] += 1

    cola = deque([nodo for nodo in grafo if indeg[nodo] == 0])
    resultado = []

    while cola:
        nodo = cola.popleft()
        resultado.append(nodo)
        print(f"Nodo procesado: {nodo}")

        for vecino in grafo[nodo]:
            indeg[vecino] -= 1
            if indeg[vecino] == 0:
                cola.append(vecino)

    # Si hay nodos sin procesar, hay ciclo
    if len(resultado) != len(grafo):
        print("Estructura ciclica: no se puede calcular T-Sort")
        return None
    return resultado


def procesarGrafoJson(archivo):
    grafo = leerGrafoJson(archivo)
    print("Grafo leido:", grafo)
    resultado = tSort(grafo)
    if resultado:
        print("Resultado final del T-Sort:", resultado)


def main():
    print("Grafo Aciclico")
    procesarGrafoJson("grafoA.json")
    print("\nGrafo Aciclico 2")
    procesarGrafoJson("grafoA2.json")
    print("\nGrafo Ciclico")
    procesarGrafoJson("grafoC.json")


main()