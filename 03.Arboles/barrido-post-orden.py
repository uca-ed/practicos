import sys


def leer_arbol(nombre_archivo):
    arbol = []
    archivo = open(nombre_archivo)
    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            arbol.append(int(linea))
    archivo.close()
    return arbol


def postorden(arbol, g):
    n = len(arbol)
    if n == 0:
        return

    pila = []
    salida = []
    pila.append(0)

    while len(pila) > 0:
        i = pila.pop()
        salida.append(i)

        j = 1
        while j <= g:
            hijo = g * i + j
            if hijo < n:
                pila.append(hijo)
            j = j + 1

    k = len(salida) - 1
    while k >= 0:
        print(arbol[salida[k]])
        k = k - 1


def main():
    grado = int(sys.argv[1])
    nombre_archivo = sys.argv[2]
    arbol = leer_arbol(nombre_archivo)
    postorden(arbol, grado)


if __name__ == "__main__":
    main()
