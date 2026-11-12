import sys


def leer_arreglo(path):
    with open(path) as f:
        return [int(linea.strip()) for linea in f if linea.strip() != ""]


def simetrico(arreglo):
    n = len(arreglo)
    resultado = []

    def visitar(i):
        if i < n:
            visitar(2 * i + 1)
            resultado.append(arreglo[i])
            visitar(2 * i + 2)

    visitar(0)
    return resultado


def main():
    if len(sys.argv) < 2:
        print(f"Uso: python3 {sys.argv[0]} <archivo>", file=sys.stderr)
        sys.exit(1)

    arreglo = leer_arreglo(sys.argv[1])

    for valor in simetrico(arreglo):
        print(valor)


if __name__ == "__main__":
    main()
