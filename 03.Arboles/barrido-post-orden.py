"""
Ejercicio 1c: barrido post-orden (cada subárbol de izquierda a derecha, luego la raíz).
"""
from arbol_arreglo import leer_arbol, hijos, leer_argumentos, imprimir


def post_orden(A: list[str], r: int, k: int, resultado: list[str]):
    for hijo in hijos(k, r, len(A)):
        post_orden(A, r, hijo, resultado)
    resultado.append(A[k])


if __name__ == "__main__":
    r, archivo = leer_argumentos()
    A = leer_arbol(archivo)
    resultado = []
    if A:
        post_orden(A, r, 0, resultado)
    imprimir(resultado)
