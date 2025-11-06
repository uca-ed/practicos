from math import log, ceil
from typing import List, Any


# altura de un árbol m-ario representado en arreglo por niveles,
def altura_m_aria_sin_recorrer(arbol: List[Any], m: int) -> int:
    """
    La formula que vimos para calcular cantidad de niveles de un Árbol r-ario lleno
    es: Techo(log r (n)),siendo n=|P|.  De ahí se deduce la altura con la siguiente
    Fórmula (árbol m-ario lleno, con ceil para cubrir niveles parciales):
        h = ceil( log_m( n*(m-1) + 1 ) ) - 1
    """
    if m < 1:
        raise ValueError("El grado m debe ser >= 1")
    n = sum(1 for x in arbol if x is not None)  # contamos nodos válidos
    if n == 0:
        return -1  # árbol vacío: altura -1 por convención
    if m == 1:
        # Árbol degenerado (cada nodo tiene a lo sumo 1 hijo)
        # altura = n-1 si hay n nodos
        return n - 1
    return int(ceil(log(n * (m - 1) + 1, m)) - 1)

# Índices de los m hijos de i en arreglo por niveles (basado en 0).
def hijos_de(i: int, m: int) -> List[int]:
    base = m * i + 1
    return list(range(base, base + m))


# Barrido PRE-ORDEN (raíz, luego hijos de izq a der),
def preorden_indices(arbol: List[Any], m: int, i: int, visita: List[Any]):
    if i >= len(arbol):
        return
    if arbol[i] is None:
        return

    # primero visito el nodo actual
    visita.append(arbol[i])

    # segundo recorro recursivamente a sus hijos (si existen y no son None)
    for h in hijos_de(i, m):
        if h < len(arbol) and arbol[h] is not None:
            preorden_indices(arbol, m, h, visita)

# meti todo en una función que retorna la lista de etiquetas en pre-orden.
# Si la raíz es None o el arreglo está vacío, devuelve [].
def preorden(arbol: List[Any], m: int) -> List[Any]:
    if not arbol or arbol[0] is None:
        return []
    recorrido = []
    preorden_indices(arbol, m, 0, recorrido)
    return recorrido


# Ejemplo
if __name__ == "__main__":
    # Árbol 3-ario (m=3) guardado por niveles:
    arbol = ["A", "B", "C", "D", "E", "F", None, "G", "H"]
    m = 3

    h = altura_m_aria_sin_recorrer(arbol, m)
    print("Altura (raíz=0):", h)

    recorrido = preorden(arbol, m)
    print("Pre-orden:", recorrido)

    # Árbol binario (m=2) guardado por niveles:
    arbol = ["A", "B", "C", "D", "E", "F", None, "G", "H"]
    m = 2

    h = altura_m_aria_sin_recorrer(arbol, m)
    print("Altura (raíz=0):", h)

    recorrido = preorden(arbol, m)
    print("Pre-orden:", recorrido)

