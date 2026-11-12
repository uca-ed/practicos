import sys


def leer_arbol(ruta):
    with open(ruta, encoding="utf-8") as f:
        return [linea.strip() for linea in f if linea.strip()]


def barrido_simetrico(arbol):
    n = len(arbol)
    res = []
    pila = []
    i = 0
    while pila or i < n:
        while i < n:
            pila.append(i)
            i = 2 * i + 1
        i = pila.pop()
        res.append(arbol[i])
        i = 2 * i + 2  
    return res


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    arbol = leer_arbol(sys.argv[1])
    sys.stdout.write("\n".join(barrido_simetrico(arbol)) + "\n")