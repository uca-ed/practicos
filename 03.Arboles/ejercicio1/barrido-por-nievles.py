import sys
from collections import deque


def leer_arreglo(path):
    with open(path) as f:
        return [int(linea.strip()) for linea in f if linea.strip() != ""]


def hijos(i, r, n):
    primero = r * i + 1
    return [h for h in range(primero, primero + r) if h < n]


def por_niveles(arreglo, r):
    n = len(arreglo)
    resultado = []
    if n == 0:
        return resultado

    cola = deque([0])
    while cola:
        i = cola.popleft()
        resultado.append(arreglo[i])
        for hijo in hijos(i, r, n):
            cola.append(hijo)

    return resultado


def main():
    if len(sys.argv) < 3:
        print(f"Uso: python3 {sys.argv[0]} <r> <archivo>", file=sys.stderr)
        sys.exit(1)

    r = int(sys.argv[1])
    arreglo = leer_arreglo(sys.argv[2])

    for valor in por_niveles(arreglo, r):
        print(valor)


if __name__ == "__main__":
    main()
