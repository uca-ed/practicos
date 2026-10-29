import sys


def main():
    r = int(sys.argv[1])
    with open(sys.argv[2]) as f:
        n = len(f.read().split())
    altura = 0
    acumulado = 0
    nodos_nivel = 1
    while acumulado < n:
        acumulado += nodos_nivel
        nodos_nivel *= r
        altura += 1
    print(altura)


if __name__ == "__main__":
    main()
