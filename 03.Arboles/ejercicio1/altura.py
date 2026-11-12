import sys


def leer_arreglo(path):
    with open(path) as f:
        return [int(linea.strip()) for linea in f if linea.strip() != ""]


def detectar_altura(n_nodos, r):
    total = 0
    nodos_en_nivel = 1
    h = 0

    while total < n_nodos:
        total += nodos_en_nivel
        nodos_en_nivel *= r
        h += 1

    if total != n_nodos:
        raise ValueError(
            f"{n_nodos} nodos no forman un arbol lleno de grado {r}"
        )

    return h


def main():
    if len(sys.argv) < 3:
        print(f"Uso: python3 {sys.argv[0]} <r> <archivo>", file=sys.stderr)
        sys.exit(1)

    r = int(sys.argv[1])
    arreglo = leer_arreglo(sys.argv[2])

    print(detectar_altura(len(arreglo), r))


if __name__ == "__main__":
    main()
