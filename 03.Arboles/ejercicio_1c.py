import sys


def main():
    r = int(sys.argv[1])
    with open(sys.argv[2]) as f:
        arbol = [int(x) for x in f.read().split()]
    n = len(arbol)
    salida = []
    pila = [(0, False)] if n else []
    while pila:
        i, expandido = pila.pop()
        if expandido:
            salida.append(arbol[i])
            continue
        pila.append((i, True))
        primero = r * i + 1
        ultimo = min(r * i + r, n - 1)
        for hijo in range(ultimo, primero - 1, -1):
            pila.append((hijo, False))
    sys.stdout.write("".join(f"{v}\n" for v in salida))


if __name__ == "__main__":
    main()
