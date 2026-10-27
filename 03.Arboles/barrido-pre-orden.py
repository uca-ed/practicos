"""
Ejercicio 1b: barrido pre-orden (raíz, luego cada subárbol de izquierda a derecha).
"""
from arbol_arreglo import leer_arbol, hijos, leer_argumentos, imprimir


def pre_orden(A: list[str], r: int, k: int, resultado: list[str]):
    resultado.append(A[k])
    for hijo in hijos(k, r, len(A)):
        pre_orden(A, r, hijo, resultado)


if __name__ == "__main__":
    r, archivo = leer_argumentos()
    A = leer_arbol(archivo)
    resultado = []
    if A:
        pre_orden(A, r, 0, resultado)
    imprimir(resultado)
