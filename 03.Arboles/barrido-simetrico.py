import sys


def simetrico(arbol, posicion):
    if posicion >= len(arbol):
        return

    simetrico(arbol, 2 * posicion + 1)
    print(arbol[posicion])
    simetrico(arbol, 2 * posicion + 2)


arbol = []
archivo = open(sys.argv[1], "r")
for linea in archivo:
    arbol.append(int(linea.strip()))
archivo.close()

simetrico(arbol, 0)
