class NodoAVL:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
        self.altura = 1

def altura(nodo):
    if nodo is None:
        return 0
    return nodo.altura


def balance(nodo):
    if nodo is None:
        return 0
    return altura(nodo.izq) - altura(nodo.der)


def rotacion_derecha(y):
    x = y.izq
    T2 = x.der

    x.der = y
    y.izq = T2

    y.altura = 1 + max(altura(y.izq), altura(y.der))
    x.altura = 1 + max(altura(x.izq), altura(x.der))
    return x


def rotacion_izquierda(x):
    y = x.der
    T2 = y.izq
    y.izq = x
    x.der = T2
    x.altura = 1 + max(altura(x.izq), altura(x.der))
    y.altura = 1 + max(altura(y.izq), altura(y.der))
    return y


def insertar(nodo, clave):
    if nodo is None:
        return NodoAVL(clave)
    elif clave < nodo.clave:
        nodo.izq = insertar(nodo.izq, clave)
    elif clave > nodo.clave:
        nodo.der = insertar(nodo.der, clave)
    else:
        return nodo  

    nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))
    b = balance(nodo)

    if b > 1 and clave < nodo.izq.clave:
        return rotacion_derecha(nodo)

    if b < -1 and clave > nodo.der.clave:
        return rotacion_izquierda(nodo)

    if b > 1 and clave > nodo.izq.clave:
        nodo.izq = rotacion_izquierda(nodo.izq)
        return rotacion_derecha(nodo)

    if b < -1 and clave < nodo.der.clave:
        nodo.der = rotacion_derecha(nodo.der)
        return rotacion_izquierda(nodo)

    return nodo

def preorden(nodo):
    if nodo:
        print(nodo.clave, end=" ")
        preorden(nodo.izq)
        preorden(nodo.der)

def inorden(nodo):
    if nodo:
        inorden(nodo.izq)
        print(nodo.clave, end=" ")
        inorden(nodo.der)

def main():
    nombre_archivo = "datos.txt"
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    import re
    claves = [int(x) for x in re.findall(r"-?\d+", contenido)]

    if not claves:
        print("El archivo está vacío o no contiene números válidos.")
        return

    print(f"Claves a insertar: {claves}")

    raiz = None
    for c in claves:
        raiz = insertar(raiz, c)

    print("\nRecorrido Preorden:")
    preorden(raiz)
    print("\n\nRecorrido Inorden:")
    inorden(raiz)
    print("\n")


if __name__ == "__main__":
    main()
