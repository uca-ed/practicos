"""
2. Crear un árbol AVL realizando las inserciones dadas en el archivo de datos.
"""

class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.altura = 1
        self.izq = None
        self.der = None


def altura(nodo):
    if nodo is None:
        return 0
    return nodo.altura


def actualizar_altura(nodo):
    nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))


def balance(nodo):
    return altura(nodo.izq) - altura(nodo.der) if nodo else 0


def rotar_derecha(y):
    x = y.izq
    temp = x.der
    x.der = y
    y.izq = temp
    actualizar_altura(y)
    actualizar_altura(x)
    return x


def rotar_izquierda(x):
    y = x.der
    temp = y.izq
    y.izq = x
    x.der = temp
    actualizar_altura(x)
    actualizar_altura(y)
    return y


def insertar(nodo, valor):
    if nodo is None:
        return NodoAVL(valor)

    if valor < nodo.valor:
        nodo.izq = insertar(nodo.izq, valor)
    else:
        nodo.der = insertar(nodo.der, valor)

    actualizar_altura(nodo)

    equilibrio = balance(nodo)

    if equilibrio > 1 and valor < nodo.izq.valor:
        return rotar_derecha(nodo)

    if equilibrio < -1 and valor > nodo.der.valor:
        return rotar_izquierda(nodo)

    if equilibrio > 1 and valor > nodo.izq.valor:
        nodo.izq = rotar_izquierda(nodo.izq)
        return rotar_derecha(nodo)

    if equilibrio < -1 and valor < nodo.der.valor:
        nodo.der = rotar_derecha(nodo.der)
        return rotar_izquierda(nodo)

    return nodo


def mostrar_en_orden(nodo):
    if nodo:
        mostrar_en_orden(nodo.izq)
        print(nodo.valor, end=" ")
        mostrar_en_orden(nodo.der)


def ejecutar():
    raiz = None

    archivo = open("EstructuraDeDatos\\ED-Practica-ed-2025-2c\\03.Arboles\\02.datos.txt", "r")

    for linea in archivo:
        numero = int(linea.strip())
        raiz = insertar(raiz, numero)

    archivo.close()

    print("AVL final en orden:")
    mostrar_en_orden(raiz)
    print()


ejecutar()
