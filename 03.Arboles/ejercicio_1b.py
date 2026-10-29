import sys


def main():
    r = int(sys.argv[1])
    with open(sys.argv[2]) as f:
        arbol = [int(x) for x in f.read().split()]
    n = len(arbol)
    salida = []
    pila = [0] if n else []
    while pila:
        i = pila.pop()
        salida.append(arbol[i])
        primero = r * i + 1
        ultimo = min(r * i + r, n - 1)
        for hijo in range(ultimo, primero - 1, -1):
            pila.append(hijo)
    sys.stdout.write("".join(f"{v}\n" for v in salida))


if __name__ == "__main__":
    main()
