import sys
from collections import deque, defaultdict

def cargar_grafo(ruta):
    adyacencias = defaultdict(list)
    entradas = defaultdict(int)
    vertices = set()
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split()
            if not partes:
                continue
            origen = partes[0]
            destinos = partes[1:]
            vertices.add(origen)
            adyacencias[origen].extend(destinos)
            for destino in destinos:
                vertices.add(destino)
                entradas[destino] += 1
    for vertice in vertices:
        adyacencias[vertice]
        entradas[vertice]
    return adyacencias, entradas

def t_sort(ruta):
    adyacencias, entradas = cargar_grafo(ruta)
    cola = deque([v for v, grado in entradas.items() if grado == 0])
    orden = []
    while cola:
        vertice = cola.popleft()
        orden.append(vertice)
        for vecino in adyacencias[vertice]:
            entradas[vecino] -= 1
            if entradas[vecino] == 0:
                cola.append(vecino)
    if len(orden) != len(entradas):
        return None
    return orden

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python t_sort.py archivo_grafo")
        sys.exit(1)
    resultado = t_sort(sys.argv[1])
    if resultado is None:
        print("La estructura es cíclica")
    else:
        print(" ".join(resultado))
