def altura(n, g):
    h = 0
    max_nodos = 1

    while n > max_nodos:
        h += 1
        max_nodos += g ** h

    return h


def main():
    n = 10
    g = 3  

    resultado = altura(n, g)

    print("Cantidad de nodos:", n)
    print("Grado del árbol:", g)
    print("Altura del árbol:", resultado)


if __name__ == "__main__":
    main()
