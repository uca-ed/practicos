#2. Crear un árbol AVL realizando las inserciones dadas en el archivo de datos.

import os

directorio_actual = os.path.dirname(__file__)
ruta_archivo = os.path.join(directorio_actual, "datos.txt")

with open(ruta_archivo) as f:
    valores = [int(linea.strip()) for linea in f]


class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1


class AVL:
    def insertar(self, raiz, valor):
        if not raiz:
            return NodoAVL(valor)
        elif valor < raiz.valor:
            raiz.izq = self.insertar(raiz.izq, valor)
        elif valor > raiz.valor:
            raiz.der = self.insertar(raiz.der, valor)
        else:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.izq), self.altura(raiz.der))
        balance = self.balance(raiz)

        if balance > 1 and valor < raiz.izq.valor:
            return self.rotar_derecha(raiz)
        if balance < -1 and valor > raiz.der.valor:
            return self.rotar_izquierda(raiz)
        if balance > 1 and valor > raiz.izq.valor:
            raiz.izq = self.rotar_izquierda(raiz.izq)
            return self.rotar_derecha(raiz)
        if balance < -1 and valor < raiz.der.valor:
            raiz.der = self.rotar_derecha(raiz.der)
            return self.rotar_izquierda(raiz)

        return raiz

    def altura(self, nodo):
        return nodo.altura if nodo else 0

    def balance(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izq) - self.altura(nodo.der)

    def rotar_derecha(self, y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        return x

    def rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        return y

    def inorden(self, raiz):
        if not raiz:
            return []
        return self.inorden(raiz.izq) + [raiz.valor] + self.inorden(raiz.der)

    def imprimir_arbol(self, nodo, nivel=0, prefijo="R: "):
        if nodo is not None:
            print(" " * (nivel * 4) + prefijo + str(nodo.valor))
            if nodo.izq or nodo.der:
                self.imprimir_arbol(nodo.izq, nivel + 1, "Izq ")
                self.imprimir_arbol(nodo.der, nivel + 1, "Der ")


class ABB:
    def insertar(self, raiz, valor):
        if not raiz:
            return NodoAVL(valor)
        if valor < raiz.valor:
            raiz.izq = self.insertar(raiz.izq, valor)
        elif valor > raiz.valor:
            raiz.der = self.insertar(raiz.der, valor)
        return raiz

    def inorden(self, raiz):
        if not raiz:
            return []
        return self.inorden(raiz.izq) + [raiz.valor] + self.inorden(raiz.der)

    def imprimir_arbol(self, nodo, nivel=0, prefijo="R"):
        if nodo is not None:
            print(" " * (nivel * 4) + prefijo + str(nodo.valor))
            if nodo.izq or nodo.der:
                self.imprimir_arbol(nodo.izq, nivel + 1, "Izq ")
                self.imprimir_arbol(nodo.der, nivel + 1, "Der")


if __name__ == "__main__":
    abb = ABB()
    raiz_abb = None
    for v in valores:
        raiz_abb = abb.insertar(raiz_abb, v)

    avl = AVL()
    raiz_avl = None
    for v in valores:
        raiz_avl = avl.insertar(raiz_avl, v)

   
    print("\nEstructura del ABB:")
    abb.imprimir_arbol(raiz_abb)

    print("\nEstructura del AVL:")
    avl.imprimir_arbol(raiz_avl)
