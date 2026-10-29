import sys
from collections import deque


def leer_arbol(nombre_archivo):
    arbol = []
    archivo = open(nombre_archivo)
    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            arbol.append(int(linea))
    archivo.close()
    return arbol


def por_niveles(arbol, g):
    if not arbol or arbol[0] is None:
        return

    cola = deque([0])

    while cola:
        i = cola.popleft()
        print(arbol[i])

        for j in range(1, g + 1):
            hijo = g * i + j

            if hijo < len(arbol) and arbol[hijo] is not None:
                cola.append(hijo)


def main():
    grado = int(sys.argv[1])
    nombre_archivo = sys.argv[2]
    arbol = leer_arbol(nombre_archivo)
    por_niveles(arbol, grado)


if __name__ == "__main__":
    main()
