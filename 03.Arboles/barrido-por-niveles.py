import sys
from collections import deque


def leer_arbol(ruta):
    with open(ruta, encoding="utf-8") as f:
        return [linea.strip() for linea in f if linea.strip()]


def barrido_por_niveles(arbol, r):
    return list(arbol)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    r = int(sys.argv[1])
    arbol = leer_arbol(sys.argv[2])
    sys.stdout.write("\n".join(barrido_por_niveles(arbol, r)) + "\n")