class NodoAVL:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
        self.altura = 1


class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        self.raiz = self._insertar(self.raiz, clave)

    def _insertar(self, nodo, clave):
        # Inserción tipo ABB
        if nodo is None:
            return NodoAVL(clave)
        if clave < nodo.clave:
            nodo.izq = self._insertar(nodo.izq, clave)
        elif clave > nodo.clave:
            nodo.der = self._insertar(nodo.der, clave)
        else:
            return nodo  # duplicado

        # Actualizar altura
        nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

        # Calcular balance
        balance = self.altura(nodo.izq) - self.altura(nodo.der)

        # Casos de rotación
        if balance > 1 and clave < nodo.izq.clave:  # LL
            return self.rotar_derecha(nodo)
        if balance < -1 and clave > nodo.der.clave:  # RR
            return self.rotar_izquierda(nodo)
        if balance > 1 and clave > nodo.izq.clave:  # LR
            nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)
        if balance < -1 and clave < nodo.der.clave:  # RL
            nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)

        return nodo

    def altura(self, nodo):
        return nodo.altura if nodo else 0

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
