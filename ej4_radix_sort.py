"""
Ejercicio 4: Radix Sort sobre palabras.

Sigue el algoritmo visto en la catedra:

    Sigma = (0, 1, ..., r-1)
    Q cola que contiene nombres
    Xi = (xip, xip-1, ..., xi1)     -> x_i1 es el caracter menos significativo (el ultimo)

    Para j = 1 hasta p
        Vaciar Q0, Q1, ..., Qr-1
        Mientras Q no vacia
            X <- Q
            Sea X = (xp, xp-1, ..., x1)
            Qxj <- X
        concatenar (Q0, Q1, ..., Qr-1)

Es decir: LSD radix sort. En cada pasada j se distribuye segun el caracter
que esta a "j" posiciones del final de la palabra (j=1 es el ultimo caracter),
usando r = 27 baldes: balde 0 para "relleno" (palabras mas cortas que la
posicion actual) y baldes 1..26 para 'a'..'z'.
"""

import os
import sys

ALFABETO = "abcdefghijklmnopqrstuvwxyz"
R = len(ALFABETO) + 1  # +1 para el balde de relleno (0)


def _balde(caracter):
    if caracter is None:
        return 0
    return ALFABETO.index(caracter) + 1


def radix_sort_palabras(palabras):
    if not palabras:
        return []

    palabras = [p.lower() for p in palabras]
    p = max(len(palabra) for palabra in palabras)  # longitud maxima

    cola = list(palabras)
    for j in range(1, p + 1):
        baldes = [[] for _ in range(R)]
        while cola:
            x = cola.pop(0)
            if j <= len(x):
                caracter = x[len(x) - j]  # caracter a "j" posiciones del final
            else:
                caracter = None  # palabra mas corta que la posicion actual
            baldes[_balde(caracter)].append(x)
        cola = [palabra for balde in baldes for palabra in balde]

    return cola


if __name__ == "__main__":
    ruta_defecto = os.path.join(os.path.dirname(__file__), "data", "palabras.txt")
    ruta = sys.argv[1] if len(sys.argv) > 1 else ruta_defecto

    with open(ruta, encoding="utf-8") as f:
        palabras = [linea.strip() for linea in f if linea.strip()]

    print("Palabras originales:")
    print(palabras)

    ordenadas = radix_sort_palabras(palabras)

    print("\nPalabras ordenadas (Radix Sort):")
    print(ordenadas)
