import sys


def post_orden(arbol, grado, posicion):
    if posicion >= len(arbol):
        return

    for hijo in range(1, grado + 1):
        post_orden(arbol, grado, grado * posicion + hijo)
    print(arbol[posicion])


grado = int(sys.argv[1])
if grado < 1:
    sys.exit("El grado debe ser mayor que cero")

arbol = []
archivo = open(sys.argv[2], "r")
for linea in archivo:
    arbol.append(int(linea.strip()))
archivo.close()

post_orden(arbol, grado, 0)
