
"""
grafos_utils.py

Este módulo proporciona funciones para representar y analizar grafos dirigidos simples.
Incluye construcción de matrices de adyacencia, verificación de propiedades de relaciones
(reflexividad, simetría, antisimetría, transitividad), obtención de vecindades y búsqueda
de caminos entre nodos.
"""

from typing import List, Tuple, Optional

def vecindad_derecha(nodo: str, relaciones: List[Tuple[str, str]]) -> List[str]:
    """
    Devuelve los nodos que se alcanzan directamente desde el nodo dado.
    """
    return [destino for origen, destino in relaciones if origen == nodo]

def vecindad_izquierda(nodo: str, relaciones: List[Tuple[str, str]]) -> List[str]:
    """
    Devuelve los nodos que tienen una arista dirigida hacia el nodo dado.
    """
    return [origen for origen, destino in relaciones if destino == nodo]

def obtener_nodos(relaciones: List[Tuple[str, str]]) -> List[str]:
    """
    Devuelve una lista de todos los nodos únicos en la relación.
    """
    nodos = set()
    for origen, destino in relaciones:
        nodos.add(origen)
        nodos.add(destino)
    return list(nodos)

def es_reflexivo(relaciones: List[Tuple[str, str]], nodos: List[str]) -> bool:
    """
    Verifica si el grafo es reflexivo: todos los nodos tienen una arista a sí mismos.
    """
    return all((n, n) in relaciones for n in nodos)

def es_simetrico(relaciones: List[Tuple[str, str]]) -> bool:
    """
    Verifica si el grafo es simétrico: si existe (a, b) entonces existe (b, a).
    """
    return all((b, a) in relaciones for a, b in relaciones)

def es_antisimetrico(relaciones: List[Tuple[str, str]]) -> bool:
    """
    Verifica si el grafo es antisimétrico: si (a, b) y (b, a) existen, entonces a = b.
    """
    return all(a == b or (b, a) not in relaciones for a, b in relaciones)

def es_transitivo(relaciones: List[Tuple[str, str]]) -> bool:
    """
    Verifica si el grafo es transitivo: si (a, b) y (b, c) existen, entonces (a, c) también.
    """
    return all((a, d) in relaciones for a, b1 in relaciones for b2, d in relaciones if b1 == b2)

def tipo_relacion(relaciones: List[Tuple[str, str]]) -> str:
    """
    Determina si la relación es de equivalencia, de orden, o ninguna.
    """
    nod = obtener_nodos(relaciones)
    r = es_reflexivo(relaciones, nod)
    s = es_simetrico(relaciones)
    a = es_antisimetrico(relaciones)
    t = es_transitivo(relaciones)

    if r and s and t:
        return "Relación de equivalencia"
    elif r and a and t:
        return "Relación de orden"
    else:
        return "Ninguna"

def matriz_adyacencia(relaciones: List[Tuple[str, str]], nodos: List[str]) -> List[List[int]]:
    """
    Genera la matriz de adyacencia del grafo.
    """
    indice = {n: i for i, n in enumerate(nodos)}
    n = len(nodos)
    matriz = [[0] * n for _ in range(n)]
    for origen, destino in relaciones:
        i, j = indice[origen], indice[destino]
        matriz[i][j] = 1
    return matriz

def encontrar_camino(origen: str, destino: str, relaciones: List[Tuple[str, str]]) -> Optional[List[str]]:
    """
    Devuelve una lista con el camino desde 'origen' hasta 'destino' si existe, utilizando BFS.
    """
    cola = [(origen, [origen])]
    visitados = set()
    while cola:
        actual, camino = cola.pop(0)
        if actual == destino:
            return camino
        for vecino in vecindad_derecha(actual, relaciones):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [vecino]))
    return None

def minimos_maximos(relaciones: List[Tuple[str, str]]) -> Tuple[List[str], List[str]]:
    """
    Devuelve los nodos con menor y mayor grado de salida (vecindad derecha).
    """
    nod = obtener_nodos(relaciones)
    grados = {n: len(vecindad_derecha(n, relaciones)) for n in nod}
    min_grado = min(grados.values())
    max_grado = max(grados.values())
    minimos = [n for n, g in grados.items() if g == min_grado]
    maximos = [n for n, g in grados.items() if g == max_grado]
    return minimos, maximos
