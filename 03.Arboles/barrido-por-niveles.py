"""
Ejercicio 1d: barrido por niveles.
"""
from collections import deque

from arbol_arreglo import leer_arbol, hijos, leer_argumentos, imprimir


def por_niveles(A: list[str], r: int) -> list[str]:
    resultado = []
    cola = deque([0]) if A else deque()
    while cola:
        k = cola.popleft()
        resultado.append(A[k])
        cola.extend(hijos(k, r, len(A)))
    return resultado


if __name__ == "__main__":
    r, archivo = leer_argumentos()
    A = leer_arbol(archivo)
    imprimir(por_niveles(A, r))
