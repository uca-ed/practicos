# Ejercicio 1: barridos de un arbol de grado r representado en un arreglo
#
# Uso (un solo archivo para todo):
#   python ejercicio1.py                       -> genera los arboles y corre todos los barridos
#                                                 (reemplaza al viejo correr-barridos.sh)
#   python ejercicio1.py altura r archivo      -> altura del arbol
#   python ejercicio1.py pre-orden r archivo
#   python ejercicio1.py post-orden r archivo
#   python ejercicio1.py por-niveles r archivo
#   python ejercicio1.py simetrico archivo     -> solo arboles binarios

import contextlib
import importlib.util
import io
import os
import sys

CARPETA = os.path.dirname(os.path.abspath(__file__))


def leer_arreglo(ruta):
    with open(ruta) as f:
        return [int(x) for x in f if x.strip()]


# Ejercicio 1.a - Detectar la altura sin hacer recorridos
def detectar_altura(r, arr):
    n = len(arr)
    total = 0
    nodos = 1
    h = 0
    while total < n:
        total += nodos
        nodos *= r
        h += 1
    return h


# Ejercicio 1.b - Barrido pre-orden
def barrido_pre_orden(r, arr):
    n = len(arr)
    salida = []
    pila = [0]
    while pila:
        i = pila.pop()
        salida.append(arr[i])
        for c in range(r * i + r, r * i, -1):
            if c < n:
                pila.append(c)
    return salida


# Ejercicio 1.c - Barrido post-orden
def barrido_post_orden(r, arr):
    n = len(arr)
    salida = []
    pila = [(0, False)]
    while pila:
        i, visto = pila.pop()
        if visto:
            salida.append(arr[i])
        else:
            pila.append((i, True))
            for c in range(r * i + r, r * i, -1):
                if c < n:
                    pila.append((c, False))
    return salida


# Ejercicio 1.d - Barrido por niveles
def barrido_por_niveles(r, arr):
    n = len(arr)
    salida = []
    cola = [0]
    pos = 0
    while pos < len(cola):
        i = cola[pos]
        pos += 1
        salida.append(arr[i])
        for c in range(r * i + 1, r * i + r + 1):
            if c < n:
                cola.append(c)
    return salida


# Ejercicio 1.e - Barrido simetrico (arbol binario)
def barrido_simetrico(arr):
    n = len(arr)
    salida = []
    pila = [(0, False)]
    while pila:
        i, visto = pila.pop()
        if i >= n:
            continue
        if visto:
            salida.append(arr[i])
        else:
            pila.append((2 * i + 2, False))
            pila.append((i, True))
            pila.append((2 * i + 1, False))
    return salida


def imprimir(valores):
    for v in valores:
        print(v)


def generar_arbol(r, h):
    # generar-arbol.py (del profesor) tiene guion en el nombre, asi que se carga por ruta
    ruta = os.path.join(CARPETA, "generar-arbol.py")
    spec = importlib.util.spec_from_file_location("generar_arbol", ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        modulo.generar_arbol_por_niveles(r, h)
    return [int(x) for x in buffer.getvalue().split()]


def guardar(nombre, valores):
    with open(os.path.join(CARPETA, nombre), "w") as f:
        f.write("\n".join(str(v) for v in valores) + "\n")


def correr_todo():
    arbol = generar_arbol(4, 10)
    arbol_binario = generar_arbol(2, 20)
    guardar("arbol.txt", arbol)
    guardar("arbol-binario.txt", arbol_binario)
    guardar("pre-orden.txt", barrido_pre_orden(4, arbol))
    guardar("post-orden.txt", barrido_post_orden(4, arbol))
    guardar("por-niveles.txt", barrido_por_niveles(4, arbol))
    guardar("simetrico.txt", barrido_simetrico(arbol_binario))
    print("Listo: se generaron arbol.txt, arbol-binario.txt, pre-orden.txt, "
          "post-orden.txt, por-niveles.txt y simetrico.txt")


def main():
    args = sys.argv[1:]
    if not args:
        correr_todo()
        return

    barrido = args[0]
    if barrido == "simetrico" and len(args) == 2:
        imprimir(barrido_simetrico(leer_arreglo(args[1])))
    elif barrido in ("altura", "pre-orden", "post-orden", "por-niveles") and len(args) == 3:
        r = int(args[1])
        arr = leer_arreglo(args[2])
        if barrido == "altura":
            print(detectar_altura(r, arr))
        elif barrido == "pre-orden":
            imprimir(barrido_pre_orden(r, arr))
        elif barrido == "post-orden":
            imprimir(barrido_post_orden(r, arr))
        else:
            imprimir(barrido_por_niveles(r, arr))
    else:
        print(__doc__ if __doc__ else "Uso: ver comentarios al inicio del archivo")
        sys.exit(1)


if __name__ == "__main__":
    main()
