import json
from collections import deque

def cargar_grafo(ruta_json: str) -> dict[str, list[str]]:
    """Lee el grafo desde un archivo JSON y devuelve un diccionario de adyacencias."""
    with open(ruta_json, "r", encoding="utf-8") as f:
        estructura = json.load(f)
    return estructura["E"]

def busqueda_de_paso(E: dict[str, list[str]], s: str, t: str) -> list[str] | None:
    """Implementa la Búsqueda de Paso del apunte."""
    open_q = deque([(s, None)])
    closed: list[tuple[str, str | None]] = []
    padre: dict[str, str | None] = {s: None}

    while open_q:
        z, y = open_q.popleft()
        closed.append((z, y))

        if t in E.get(z, []):
            padre[t] = z
            return reconstruir_camino(padre, t)

        en_open = {n for (n, _) in open_q}
        en_closed = {n for (n, _) in closed}
        for w in E.get(z, []):
            if w not in en_open and w not in en_closed and w not in padre:
                padre[w] = z
                open_q.append((w, z))

    return None

def reconstruir_camino(padre: dict[str, str | None], t: str) -> list[str]:
    """Reconstruye el camino desde el nodo s hasta t."""
    camino = [t]
    while padre[camino[-1]] is not None:
        camino.append(padre[camino[-1]])
    camino.reverse()
    return camino

def imprimir_vecindades(E):
    """Imprime las vecindades de cada nodo para depuración."""
    for nodo in E:
        print(f"Vecindad de {nodo}: {E[nodo]}")

if __name__ == "__main__":
    # Cargar el grafo desde el archivo JSON
    E = cargar_grafo("archivos_ej3/esDivisorDe-200.json")  # Cambia la ruta si es necesario
    imprimir_vecindades(E)  # Imprime las vecindades para depuración

    s, t = "1", "192"  # origen y destino
    camino = busqueda_de_paso(E, s, t)
    
    if camino:
        print("Secuencia de nodos para recrear el paso:")
        print(" -> ".join(camino))
    else:
        print(f"No existe camino desde {s} hasta {t}.")
