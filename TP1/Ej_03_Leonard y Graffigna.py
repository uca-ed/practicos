import json
from collections import deque

def cargar_grafo(nombre_archivo):
    """Carga el grafo desde un archivo JSON."""
    with open(nombre_archivo, 'r') as f:
        grafo = json.load(f)
    return grafo

def encontrar_camino(grafo, inicio, fin):
    """
    Implementa búsqueda en anchura (BFS) para encontrar el camino más corto
    desde el nodo 'inicio' al nodo 'fin' en un grafo dirigido.
    """
    visitados = set()
    cola = deque([(inicio, [inicio])])

    while cola:
        nodo_actual, camino = cola.popleft()
        if nodo_actual == fin:
            return camino
        
        for vecino in grafo["E"].get(nodo_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [vecino]))
    
    return None  # No hay camino encontrado

def main():
    archivo = input("Ingrese el nombre del archivo JSON del grafo (ej: 'esDivisorDe-200.json'): ")
    grafo = cargar_grafo(archivo)
    
    inicio = input("Ingrese el nodo de origen: ")
    fin = input("Ingrese el nodo de destino: ")
    
    if inicio not in grafo["P"] or fin not in grafo["P"]:
        print("Uno de los nodos no existe en el grafo.")
        return

    camino = encontrar_camino(grafo, inicio, fin)
    
    if camino:
        print("Camino encontrado:")
        print(" → ".join(camino))
    else:
        print("No existe un camino desde", inicio, "hasta", fin)

if _name_ == "_main_":
    main()
