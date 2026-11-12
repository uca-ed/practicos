import sys


def leer_arbol(ruta):
    with open(ruta, encoding="utf-8") as f:
        return [linea.strip() for linea in f if linea.strip()]


def altura_arbol(arbol, r):
    restantes = len(arbol)
    nodos_en_nivel = 1
    altura = 0
    while restantes > 0:
        restantes = restantes - nodos_en_nivel
        nodos_en_nivel = nodos_en_nivel * r
        altura = altura + 1
    return altura


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    r = int(sys.argv[1])
    arbol = leer_arbol(sys.argv[2])
    print(altura_arbol(arbol, r))
