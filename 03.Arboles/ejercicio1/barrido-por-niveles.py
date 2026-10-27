
import sys
from collections import deque

VACIOS = {"-", "None", "null"}


def leer_arreglo(ruta):
    with open(ruta) as f:
        return [linea.strip() for linea in f if linea.strip()]


def por_niveles(arreglo, r):
    n = len(arreglo)
    salida = []

    def existe(i):
        return i < n and arreglo[i] not in VACIOS

    cola = deque()
    if existe(0):
        cola.append(0)
    while cola:
        i = cola.popleft()
        salida.append(arreglo[i])
        for k in range(1, r + 1):
            hijo = r * i + k
            if existe(hijo):
                cola.append(hijo)
    return salida


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Uso: python barrido-por-niveles.py <grado> <archivo>")
    r = int(sys.argv[1])
    resultado = por_niveles(leer_arreglo(sys.argv[2]), r)
    sys.stdout.write("\n".join(resultado) + ("\n" if resultado else ""))
