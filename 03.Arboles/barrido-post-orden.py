import sys


def leer_arbol(ruta):
    with open(ruta, encoding="utf-8") as f:
        return [linea.strip() for linea in f if linea.strip()]


def barrido_post_orden(arbol, r):
    n = len(arbol)
    res = []
    pila = [(0, 0)]
    while pila:
        x, e = pila.pop()
        if e == 0:
            pila.append((x, 1))
            for i in range(r, 0, -1):
                hijo = r * x + i
                if hijo < n:
                    pila.append((hijo, 0))
        else:
            res.append(arbol[x])
    return res


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    r = int(sys.argv[1])
    arbol = leer_arbol(sys.argv[2])
    sys.stdout.write("\n".join(barrido_post_orden(arbol, r)) + "\n")
