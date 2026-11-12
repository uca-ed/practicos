import sys
from collections import deque

def main():
    if len(sys.argv) != 3:
        print("Uso: python barrido-por-nievles.py grado archivo.txt", file=sys.stderr)
        sys.exit(1)

    r = int(sys.argv[1])
    if r < 1:
        raise ValueError("El grado debe ser positivo.")

    with open(sys.argv[2], "r", encoding="utf-8") as archivo:
        arbol = [line.strip() for line in archivo if line.strip()]

    if not arbol:
        return

    cola = deque([0])
    while cola:
        i = cola.popleft()
        print(arbol[i])
        for j in range(r):
            hijo = r * i + 1 + j
            if hijo < len(arbol):
                cola.append(hijo)

if __name__ == "__main__":
    main()
