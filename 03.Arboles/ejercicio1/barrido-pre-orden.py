"""
Ejercicio 1 b): Barrido pre-orden de un árbol r-ario representado en un arreglo.

Uso:
    python barrido-pre-orden.py <grado> <archivo-origen>
    python barrido-pre-orden.py --test

En un arreglo que representa un árbol r-ario por niveles (0-indexado):
Para un nodo en la posición 'pos', sus r hijos se ubican en:
    hijo_i = grado * pos + i    (para 1 <= i <= grado)
"""

import argparse
import os
import sys


def pre_orden(arbol: list, n: int, grado: int, pos: int):
    """Realiza el barrido pre-orden e imprime un nodo por renglón."""
    if pos >= n:
        return
    print(arbol[pos])
    base = grado * pos
    for i in range(1, grado + 1):
        hijo = base + i
        if hijo < n:
            pre_orden(arbol, n, grado, hijo)


def leer_arbol(ruta_archivo: str) -> list:
    """Lee las claves del archivo (un valor por línea o separados por espacios)."""
    if not os.path.isabs(ruta_archivo) and not os.path.exists(ruta_archivo):
        posible = os.path.join(os.path.dirname(os.path.abspath(__file__)), ruta_archivo)
        if os.path.exists(posible):
            ruta_archivo = posible

    for enc in ("utf-8", "utf-16", "latin-1"):
        try:
            with open(ruta_archivo, "r", encoding=enc) as f:
                return [int(x) for x in f.read().split()]
        except (UnicodeDecodeError, UnicodeError):
            continue
    with open(ruta_archivo, "r") as f:
        return [int(x) for x in f.read().split()]


def autotest():
    """Autochequeo con assert para verificar el orden del barrido."""
    # Árbol binario (grado 2): [1, 2, 3, 4, 5, 6, 7]
    #               1
    #          2         3
    #        4   5     6   7
    # Pre-orden esperado: 1, 2, 4, 5, 3, 6, 7
    arbol_binario = [1, 2, 3, 4, 5, 6, 7]
    resultado = []

    def recolectar(arbol, n, grado, pos):
        if pos >= n:
            return
        resultado.append(arbol[pos])
        base = grado * pos
        for i in range(1, grado + 1):
            hijo = base + i
            if hijo < n:
                recolectar(arbol, n, grado, hijo)

    recolectar(arbol_binario, len(arbol_binario), 2, 0)
    assert resultado == [1, 2, 4, 5, 3, 6, 7], f"Barrido binario incorrecto: {resultado}"

    # Árbol 4-ario (grado 4):
    # Raíz 0 con 4 hijos (1, 2, 3, 4), hijo 1 tiene hijos 5, 6, 7, 8
    arbol_4 = list(range(9))
    resultado.clear()
    recolectar(arbol_4, len(arbol_4), 4, 0)
    assert resultado == [0, 1, 5, 6, 7, 8, 2, 3, 4], f"Barrido 4-ario incorrecto: {resultado}"

    print("Autochequeo: barrido pre-orden verificado correctamente.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Barrido pre-orden de un árbol r-ario en arreglo.")
    parser.add_argument("grado", nargs="?", type=int, help="Grado r del árbol")
    parser.add_argument("archivo", nargs="?", help="Archivo con el árbol en arreglo")
    parser.add_argument("--test", action="store_true", help="Ejecutar autochequeo con asserts")
    args = parser.parse_args()

    if args.test:
        autotest()
        sys.exit(0)

    if args.grado is None or args.archivo is None:
        parser.error("Se requieren los argumentos <grado> y <archivo>")

    arbol = leer_arbol(args.archivo)
    pre_orden(arbol, len(arbol), args.grado, 0)
