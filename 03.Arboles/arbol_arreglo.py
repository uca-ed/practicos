import argparse


def leer_arbol(archivo: str) -> list[str]:
    with open(archivo) as f:
        return [linea.strip() for linea in f if linea.strip() != ""]


def hijos(k: int, r: int, n: int) -> range:
    primero = r * k + 1
    ultimo = min(r * k + r, n - 1)
    return range(primero, ultimo + 1)


def padre(k: int, r: int) -> int:
    return (k - 1) // r


def altura(n: int, r: int) -> int:
    if n == 0:
        return 0
    if r == 1:
        return n  
    h = 0
    nodos_hasta_nivel = 0 
    while nodos_hasta_nivel < n:
        nodos_hasta_nivel = nodos_hasta_nivel * r + 1
        h += 1
    return h


def leer_argumentos(con_grado: bool = True) -> tuple[int, str]:
    parser = argparse.ArgumentParser()
    if con_grado:
        parser.add_argument("r", type=int, help="Grado del árbol")
        parser.add_argument("archivo", help="Archivo con el árbol representado en un arreglo")
        args = parser.parse_args()
        return args.r, args.archivo
    parser.add_argument("datos", nargs="+", help="[grado] <archivo-origen>")
    args = parser.parse_args()
    if len(args.datos) == 1:
        return 2, args.datos[0]
    return int(args.datos[0]), args.datos[1]


def imprimir(nodos: list[str]):
    if nodos:
        print("\n".join(nodos))
