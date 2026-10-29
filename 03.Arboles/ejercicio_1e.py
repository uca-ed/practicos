import sys


def main():
    with open(sys.argv[1]) as f:
        arbol = [int(x) for x in f.read().split()]
    n = len(arbol)
    salida = []
    pila = []
    i = 0 if n else None
    while pila or i is not None:
        while i is not None and i < n:
            pila.append(i)
            i = 2 * i + 1
        if not pila:
            break
        i = pila.pop()
        salida.append(arbol[i])
        i = 2 * i + 2
    sys.stdout.write("".join(f"{v}\n" for v in salida))


if __name__ == "__main__":
    main()
