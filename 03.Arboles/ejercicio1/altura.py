
import sys

VACIOS = {"-", "None", "null"}  # marcas opcionales de posición vacía


def leer_arreglo(ruta):
    with open(ruta) as f:
        return [linea.strip() for linea in f if linea.strip()]


def altura(arreglo, r):
    # último índice ocupado (en un árbol generado lleno es directamente len-1)
    ultimo = len(arreglo) - 1
    while ultimo >= 0 and arreglo[ultimo] in VACIOS:
        ultimo -= 1
    if ultimo < 0:
        return 0  # árbol vacío

    # buscar el nivel k tal que (r^(k-1)-1)/(r-1) <= ultimo < (r^k-1)/(r-1)
    h = 1
    nodos_hasta_nivel = 1   # (r^h - 1)/(r - 1): cantidad de posiciones de los niveles 1..h
    nodos_en_nivel = 1      # r^(h-1)
    while ultimo >= nodos_hasta_nivel:
        nodos_en_nivel *= r
        nodos_hasta_nivel += nodos_en_nivel
        h += 1
    return h


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Uso: python altura.py <grado> <archivo>")
    r = int(sys.argv[1])
    print(altura(leer_arreglo(sys.argv[2]), r))
