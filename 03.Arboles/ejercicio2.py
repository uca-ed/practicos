# Ejercicio 2

import sys


class Nodo:
    def __init__(self, val):
        self.val = val
        self.izq = None
        self.der = None
        self.alt = 1


def alt(n):
    return n.alt if n else 0


def balance(n):
    return alt(n.izq) - alt(n.der) if n else 0


def recalcular(n):
    n.alt = 1 + max(alt(n.izq), alt(n.der))


def rotar_der(y):
    x = y.izq
    y.izq = x.der
    x.der = y
    recalcular(y)
    recalcular(x)
    return x


def rotar_izq(x):
    y = x.der
    x.der = y.izq
    y.izq = x
    recalcular(x)
    recalcular(y)
    return y


def insertar(raiz, val):
    if raiz is None:
        return Nodo(val)
    if val < raiz.val:
        raiz.izq = insertar(raiz.izq, val)
    elif val > raiz.val:
        raiz.der = insertar(raiz.der, val)
    else:
        return raiz

    recalcular(raiz)
    b = balance(raiz)

    if b > 1 and val < raiz.izq.val:
        return rotar_der(raiz)
    if b < -1 and val > raiz.der.val:
        return rotar_izq(raiz)
    if b > 1 and val > raiz.izq.val:
        raiz.izq = rotar_izq(raiz.izq)
        return rotar_der(raiz)
    if b < -1 and val < raiz.der.val:
        raiz.der = rotar_der(raiz.der)
        return rotar_izq(raiz)

    return raiz


def dibujar(n, prefijo, rama):
    if n is None:
        return
    dibujar(n.der, prefijo + "    ", "/-- ")
    print(prefijo + rama + str(n.val))
    dibujar(n.izq, prefijo + "    ", "\\-- ")


def in_orden(n, salida):
    if n is None:
        return
    in_orden(n.izq, salida)
    salida.append(n.val)
    in_orden(n.der, salida)


with open(sys.argv[1]) as f:
    datos = [int(x) for x in f.read().split()]

raiz = None
for val in datos:
    raiz = insertar(raiz, val)

dibujar(raiz, "", "")
salida = []
in_orden(raiz, salida)
print()
print(" ".join(str(v) for v in salida))
