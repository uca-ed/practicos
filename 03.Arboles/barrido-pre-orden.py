import sys

def main():
    if len(sys.argv) != 3:
        print("Uso: python barrido-pre-orden.py grado archivo.txt", file=sys.stderr)
        sys.exit(1)

    r = int(sys.argv[1])
    if r < 1:
        raise ValueError("El grado debe ser positivo.")

    with open(sys.argv[2], "r", encoding="utf-8") as archivo:
        arbol = [line.strip() for line in archivo if line.strip()]

    def preorden(i):
        if i >= len(arbol):
            return
        print(arbol[i])
        primer_hijo = r * i + 1
        for j in range(r):
            preorden(primer_hijo + j)

    preorden(0)

if __name__ == "__main__":
    main()
