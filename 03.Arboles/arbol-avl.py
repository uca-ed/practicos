import sys

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1

def altura(n):
    return n.altura if n else 0

def actualizar(n):
    n.altura = 1 + max(altura(n.izq), altura(n.der))

def balance(n):
    return altura(n.izq) - altura(n.der)

def rotar_derecha(y):
    x = y.izq
    subarbol = x.der
    x.der = y
    y.izq = subarbol
    actualizar(y)
    actualizar(x)
    return x

def rotar_izquierda(x):
    y = x.der
    subarbol = y.izq
    y.izq = x
    x.der = subarbol
    actualizar(x)
    actualizar(y)
    return y

def insertar(n, valor):
    if n is None:
        return Nodo(valor)
    if valor < n.valor:
        n.izq = insertar(n.izq, valor)
    elif valor > n.valor:
        n.der = insertar(n.der, valor)
    else:
        return n  # No insertamos valores duplicados.
    actualizar(n)
    b = balance(n)
    if b > 1:
        if valor > n.izq.valor:  # Izquierda-derecha
            n.izq = rotar_izquierda(n.izq)
        return rotar_derecha(n)  # Izquierda-izquierda
    if b < -1:
        if valor < n.der.valor:  # Derecha-izquierda
            n.der = rotar_derecha(n.der)
        return rotar_izquierda(n)  # Derecha-derecha
    return n

def mostrar(n, prefijo="", lado="Raiz"):
    if n is None:
        return
    print(f"{prefijo}{lado}: {n.valor} (altura={n.altura}, balance={balance(n)})")
    mostrar(n.izq, prefijo + "  ", "I")
    mostrar(n.der, prefijo + "  ", "D")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Uso: python arbol-avl.py ARCHIVO_DATOS")
    with open(sys.argv[1], encoding="utf-8") as f:
        valores = [int(v) for v in f.read().replace(",", " ").split()]
    raiz = None
    for valor in valores:
        raiz = insertar(raiz, valor)
    mostrar(raiz)
