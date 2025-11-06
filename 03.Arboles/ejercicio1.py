import math

def alturaArbol(n, r):
    if r <= 1:
        return n - 1
    h = math.floor(math.log((n * (r - 1)) + 1, r)) - 1
    return h


def preorden(arbol, i, r):
    n = len(arbol)
    if i >= n:
        return
    print(arbol[i], end=" ")

    for k in range(r):
        hijo = r * i + (k + 1)
        if hijo < n:
            preorden(arbol, hijo, r)


def main():
    # Árbol ternario (r = 3)
    arbol = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    r = 3
    n = len(arbol)

    h = alturaArbol(n, r)
    print(f"Altura del árbol (sin recorrer): {h}")

    print("Barrido preorden:")
    preorden(arbol, 0, r)

main()
