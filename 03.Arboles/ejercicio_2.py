import sys


class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
        self.altura = 1


def altura(nodo):
    return nodo.altura if nodo else 0


def actualizar(nodo):
    nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))


def balance(nodo):
    return altura(nodo.izq) - altura(nodo.der) if nodo else 0


def rotar_derecha(y):
    x = y.izq
    y.izq = x.der
    x.der = y
    actualizar(y)
    actualizar(x)
    return x


def rotar_izquierda(x):
    y = x.der
    x.der = y.izq
    y.izq = x
    actualizar(x)
    actualizar(y)
    return y


def insertar(nodo, clave):
    if nodo is None:
        return Nodo(clave)
    if clave < nodo.clave:
        nodo.izq = insertar(nodo.izq, clave)
    elif clave > nodo.clave:
        nodo.der = insertar(nodo.der, clave)
    else:
        return nodo
    actualizar(nodo)
    b = balance(nodo)
    if b > 1:
        if balance(nodo.izq) < 0:
            nodo.izq = rotar_izquierda(nodo.izq)
        return rotar_derecha(nodo)
    if b < -1:
        if balance(nodo.der) > 0:
            nodo.der = rotar_derecha(nodo.der)
        return rotar_izquierda(nodo)
    return nodo


def pre_orden(nodo, salida):
    if nodo is None:
        return
    salida.append(f"{nodo.clave} (altura={nodo.altura}, balance={balance(nodo)})")
    pre_orden(nodo.izq, salida)
    pre_orden(nodo.der, salida)


def main():
    ruta = sys.argv[1] if len(sys.argv) > 1 else "datos.txt"
    with open(ruta) as f:
        claves = [int(x) for x in f.read().split()]
    raiz = None
    for clave in claves:
        raiz = insertar(raiz, clave)
    salida = []
    pre_orden(raiz, salida)
    sys.stdout.write("".join(f"{linea}\n" for linea in salida))


if __name__ == "__main__":
    main()
