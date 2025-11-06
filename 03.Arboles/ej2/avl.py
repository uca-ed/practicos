class NodoAVL:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
        self.altura = 1  # altura inicial del nodo (hoja)


class ArbolAVL:
    def __init__(self):
        self.raiz = None

    # --- Funciones auxiliares ---
    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _factor_balanceo(self, nodo):
        return self._altura(nodo.izq) - self._altura(nodo.der) if nodo else 0

    # --- Rotaciones ---
    def _rotar_derecha(self, y):
        x = y.izq
        T2 = x.der

        # rotación
        x.der = y
        y.izq = T2

        # actualizar alturas
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))

        return x  # nueva raíz

    def _rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq

        # rotación
        y.izq = x
        x.der = T2

        # actualizar alturas
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))

        return y  # nueva raíz

    # --- Inserción ---
    def _insertar(self, nodo, clave):
        # inserción normal de BST
        if nodo is None:
            return NodoAVL(clave)
        elif clave < nodo.clave:
            nodo.izq = self._insertar(nodo.izq, clave)
        elif clave > nodo.clave:
            nodo.der = self._insertar(nodo.der, clave)
        else:
            return nodo  # clave duplicada, no se inserta

        # actualizar altura del ancestro
        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))

        # balancear el nodo
        balance = self._factor_balanceo(nodo)

        # --- Casos de desbalance ---
        # Caso Izquierda-Izquierda
        if balance > 1 and clave < nodo.izq.clave:
            return self._rotar_derecha(nodo)

        # Caso Derecha-Derecha
        if balance < -1 and clave > nodo.der.clave:
            return self._rotar_izquierda(nodo)

        # Caso Izquierda-Derecha
        if balance > 1 and clave > nodo.izq.clave:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)

        # Caso Derecha-Izquierda
        if balance < -1 and clave < nodo.der.clave:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)

        return nodo

    def insertar(self, clave):
        """Inserta un nuevo valor en el árbol AVL."""
        self.raiz = self._insertar(self.raiz, clave)

    # --- Recorridos ---
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

    # --- Impresión visual del árbol ---
    def pretty_print(self, nodo=None, prefijo="", es_izq=True):
        """Muestra el árbol de forma visual (rotado 90°)."""
        if nodo is None:
            nodo = self.raiz

        if nodo is None:
            print("<árbol vacío>")
            return

        if nodo.der is not None:
            self.pretty_print(nodo.der, prefijo + ("│   " if es_izq else "    "), False)

        print(prefijo + ("└── " if es_izq else "┌── ") + f"{nodo.clave} (h={nodo.altura})")

        if nodo.izq is not None:
            self.pretty_print(nodo.izq, prefijo + ("    " if es_izq else "│   "), True)
