
import sys

VACIOS = {"-", "None", "null"}


def leer_arreglo(ruta):
    with open(ruta) as f:
        return [linea.strip() for linea in f if linea.strip()]


def simetrico(arreglo):
    n = len(arreglo)
    salida = []

    def existe(i):
        return i < n and arreglo[i] not in VACIOS

    def visitar(i):
        if not existe(i):
            return
        visitar(2 * i + 1)        # 1) subárbol izquierdo
        salida.append(arreglo[i]) # 2) raíz
        visitar(2 * i + 2)        # 3) subárbol derecho

    visitar(0)
    return salida


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Uso: python barrido-simetrico.py <archivo>")
    resultado = simetrico(leer_arreglo(sys.argv[1]))
    sys.stdout.write("\n".join(resultado) + ("\n" if resultado else ""))
