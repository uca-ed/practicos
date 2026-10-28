import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: python barrido-simetrico.py archivo.txt", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as archivo:
        arbol = [line.strip() for line in archivo if line.strip()]

    def simetrico(i):
        if i >= len(arbol):
            return
        simetrico(2 * i + 1)
        print(arbol[i])
        simetrico(2 * i + 2)

    simetrico(0)

if __name__ == "__main__":
    main()
