import json

def leer_grafo_E(archivo):
    """Lee el grafo usando directamente la estructura 'E' del JSON"""
    with open(archivo, "r") as f:
        estructura = json.load(f)
    return estructura["E"]

def leer_grafo_P(archivo):
    """Construye el grafo Hasse desde 'P' (sin saltos intermedios)"""
    with open(archivo, "r") as f:
        estructura = json.load(f)

    nodos = sorted(int(x) for x in estructura["P"])
    grafo = {str(n): [] for n in nodos}

    for a in nodos:
        for b in nodos:
            if a != b and b % a == 0:
                # Verificar si existe un divisor intermedio
                intermedio = any(a < c < b and b % c == 0 and c % a == 0 for c in nodos)
                if not intermedio:
                    grafo[str(a)].append(str(b))
    return grafo

def encontrar_camino(grafo, inicio, destino):
    """Búsqueda BFS del camino más corto usando listas normales"""
    visitados = set()
    cola = [(inicio, [inicio])]  # lista en lugar de deque

    while cola:
        nodo, camino = cola.pop(0)  # simula popleft
        if nodo == destino:
            return camino
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo.get(nodo, []):
                if vecino not in visitados:
                    cola.append((vecino, camino + [vecino]))
    return None

def main():
    archivo = "esDivisorDe-2000.json"
    inicio = "2"
    destino = "100"

    # Caso 1: Grafo E (saltos permitidos)
    grafo_E = leer_grafo_E(archivo)
    camino_E = encontrar_camino(grafo_E, inicio, destino)
    print("Camino con E (saltos permitidos):")
    if camino_E:
        print(" -> ".join(camino_E))
    else:
        print(f"No existe camino de {inicio} a {destino} en E")

    # Caso 2: Grafo P (Hasse, sin saltos)
    grafo_P = leer_grafo_P(archivo)
    camino_P = encontrar_camino(grafo_P, inicio, destino)
    print("\nCamino con P (Hasse, sin saltos):")
    if camino_P:
        print(" -> ".join(camino_P))
    else:
        print(f"No existe camino de {inicio} a {destino} en P")

# Llamada directa a main
main()