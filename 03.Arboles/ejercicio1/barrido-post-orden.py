
import sys

VACIOS = {"-", "None", "null"}


def leer_arreglo(ruta):
    with open(ruta) as f:
        return [linea.strip() for linea in f if linea.strip()]


def post_orden(arreglo, r):
    n = len(arreglo)
    salida = []

    def existe(i):
        return i < n and arreglo[i] not in VACIOS

    def visitar(i):
        if not existe(i):
            return
        for k in range(1, r + 1):          # 1) hijos de izquierda a derecha
            visitar(r * i + k)
        salida.append(arreglo[i])          # 2) raíz

    visitar(0)
    return salida


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Uso: python barrido-post-orden.py <grado> <archivo>")
    r = int(sys.argv[1])
    resultado = post_orden(leer_arreglo(sys.argv[2]), r)
    sys.stdout.write("\n".join(resultado) + ("\n" if resultado else ""))
