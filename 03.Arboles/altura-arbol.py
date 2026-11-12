import sys

def main():
    if len(sys.argv) != 3:
        print("Uso: python altura-arbol.py grado archivo.txt", file=sys.stderr)
        sys.exit(1)

    r = int(sys.argv[1])
    if r < 2:
        raise ValueError("El grado debe ser al menos 2.")

    with open(sys.argv[2], "r", encoding="utf-8") as archivo:
        nodos = [line.strip() for line in archivo if line.strip()]

    n = len(nodos)
    if n == 0:
        print(0)
        return

    # El último nodo del arreglo está en el nivel más profundo.
    # Subir de padre en padre hasta la raíz (índice 0) cuenta los niveles.
    h, i = 0, n - 1
    while i > 0:
        i = (i - 1) // r
        h += 1

    print(h + 1)

if __name__ == "__main__":
    main()
