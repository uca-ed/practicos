class NodoAVL:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
        self.altura = 1


class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _factor_balanceo(self, nodo):
        return self._altura(nodo.izq) - self._altura(nodo.der) if nodo else 0

    def _rotar_derecha(self, y):
        x = y.izq
        T2 = x.der

        x.der = y
        y.izq = T2

        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))

        return x

    def _rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq

        y.izq = x
        x.der = T2

        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))

        return y

    def _insertar(self, nodo, clave):
        if nodo is None:
            return NodoAVL(clave)
        elif clave < nodo.clave:
            nodo.izq = self._insertar(nodo.izq, clave)
        elif clave > nodo.clave:
            nodo.der = self._insertar(nodo.der, clave)
        else:
            return nodo

        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))

        balance = self._factor_balanceo(nodo)

        if balance > 1 and clave < nodo.izq.clave:
            return self._rotar_derecha(nodo)

        if balance < -1 and clave > nodo.der.clave:
            return self._rotar_izquierda(nodo)

        if balance > 1 and clave > nodo.izq.clave:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)

        if balance < -1 and clave < nodo.der.clave:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)

        return nodo

    def insertar(self, clave):
        self.raiz = self._insertar(self.raiz, clave)

    def _inorder(self, nodo, resultado):
        if nodo:
            self._inorder(nodo.izq, resultado)
            resultado.append(nodo.clave)
            self._inorder(nodo.der, resultado)

    def _preorder(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.clave)
            self._preorder(nodo.izq, resultado)
            self._preorder(nodo.der, resultado)

    def inorder(self):
        resultado = []
        self._inorder(self.raiz, resultado)
        return resultado

    def preorder(self):
        resultado = []
        self._preorder(self.raiz, resultado)
        return resultado

    def imprimir(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz

        if nodo is None:
            print("Árbol vacío")
            return

        if nodo.der:
            self.imprimir(nodo.der, nivel + 1)

        print("   " * nivel + f"- {nodo.clave}")

        if nodo.izq:
            self.imprimir(nodo.izq, nivel + 1)

