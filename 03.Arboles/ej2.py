import sys


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1


def altura(nodo):
    if nodo is None:
        return 0
    return nodo.altura


def actualizar_altura(nodo):
    nodo.altura = 1 + max(altura(nodo.izquierdo), altura(nodo.derecho))


def rotar_derecha(nodo):
    nueva_raiz = nodo.izquierdo
    nodo.izquierdo = nueva_raiz.derecho
    nueva_raiz.derecho = nodo

    actualizar_altura(nodo)
    actualizar_altura(nueva_raiz)
    return nueva_raiz


def rotar_izquierda(nodo):
    nueva_raiz = nodo.derecho
    nodo.derecho = nueva_raiz.izquierdo
    nueva_raiz.izquierdo = nodo

    actualizar_altura(nodo)
    actualizar_altura(nueva_raiz)
    return nueva_raiz


def insertar(nodo, valor):
    if nodo is None:
        return Nodo(valor)

    if valor < nodo.valor:
        nodo.izquierdo = insertar(nodo.izquierdo, valor)
    elif valor > nodo.valor:
        nodo.derecho = insertar(nodo.derecho, valor)
    else:
        return nodo  # No insertamos valores repetidos.

    actualizar_altura(nodo)
    balance = altura(nodo.izquierdo) - altura(nodo.derecho)

    if balance > 1:
        # Caso izquierda-derecha: primero rotamos el hijo.
        if valor > nodo.izquierdo.valor:
            nodo.izquierdo = rotar_izquierda(nodo.izquierdo)
        return rotar_derecha(nodo)

    if balance < -1:
        # Caso derecha-izquierda: primero rotamos el hijo.
        if valor < nodo.derecho.valor:
            nodo.derecho = rotar_derecha(nodo.derecho)
        return rotar_izquierda(nodo)

    return nodo


def mostrar_pre_orden(nodo):
    if nodo is not None:
        print(nodo.valor)
        mostrar_pre_orden(nodo.izquierdo)
        mostrar_pre_orden(nodo.derecho)


if __name__ == "__main__":
    raiz = None
    archivo = open(sys.argv[1], "r")
    for linea in archivo:
        raiz = insertar(raiz, int(linea.strip()))
    archivo.close()

    print("AVL en pre-orden:")
    mostrar_pre_orden(raiz)
