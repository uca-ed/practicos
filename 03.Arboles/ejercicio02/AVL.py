import sys

class Nodo:

    def __init__(self, val):
        self.val = val
        self.izq = None
        self.der = None
        self.altura = 1


def altura(n):
    return n.altura if n else 0


def balance(n):
    return altura(n.izq) - altura(n.der) if n else 0


def rotar_derecha(y):
    x = y.izq
    y.izq = x.der
    x.der = y
    y.altura = max(altura(y.izq), altura(y.der)) + 1
    x.altura = max(altura(x.izq), altura(x.der)) + 1
    return x


def rotar_izquierda(x):
    y = x.der
    x.der = y.izq
    y.izq = x
    x.altura = max(altura(x.izq), altura(x.der)) + 1
    y.altura = max(altura(y.izq), altura(y.der)) + 1
    return y


def insertar(nodo, val):
    # 1. Inserción normal de ABB
    if not nodo:
        return Nodo(val)
    if val < nodo.val:
        nodo.izq = insertar(nodo.izq, val)
    elif val > nodo.val:
        nodo.der = insertar(nodo.der, val)
    else:
        return nodo

    # 2. Actualizar altura y balancear
    nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))
    b = balance(nodo)

    # Casos de rotación
    if b > 1 and val < nodo.izq.val:
        return rotar_derecha(nodo)  # Izq-Izq
    if b < -1 and val > nodo.der.val:
        return rotar_izquierda(nodo)  # Der-Der
    if b > 1 and val > nodo.izq.val:
        nodo.izq = rotar_izquierda(nodo.izq)  # Izq-Der
        return rotar_derecha(nodo)
    if b < -1 and val < nodo.der.val:
        nodo.der = rotar_derecha(nodo.der)  # Der-Izq
        return rotar_izquierda(nodo)

    return nodo


def inorder(nodo):
    return inorder(nodo.izq) + [nodo.val] + inorder(nodo.der) if nodo else []

