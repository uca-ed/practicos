import sys


def leer_arbol(ruta):
    with open(ruta, encoding="utf-8") as f:
        return [linea.strip() for linea in f if linea.strip()]


def barrido_pre_orden(arbol, r):
    n = len(arbol)
    res = []
    pila = [0]
    while pila:
        x = pila.pop()
        res.append(arbol[x])
        for i in range(r, 0, -1):
            hijo = r * x + i
            if hijo < n:
                pila.append(hijo)
    return res


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    r = int(sys.argv[1])
    arbol = leer_arbol(sys.argv[2])
    sys.stdout.write("\n".join(barrido_pre_orden(arbol, r)) + "\n")
