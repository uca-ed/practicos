
import re
import sys
from collections import deque


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1


def altura(nodo):
    return nodo.altura if nodo else 0


def actualizar(nodo):
    nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))


def factor_balance(nodo):
    return altura(nodo.izq) - altura(nodo.der)


def rotar_derecha(y):
    #       y            x
    #      / \          / \
    #     x   C   ->   A   y
    #    / \              / \
    #   A   B            B   C
    x = y.izq
    y.izq = x.der
    x.der = y
    actualizar(y)
    actualizar(x)
    return x


def rotar_izquierda(x):
    #     x                y
    #    / \              / \
    #   A   y     ->     x   C
    #      / \          / \
    #     B   C        A   B
    y = x.der
    x.der = y.izq
    y.izq = x
    actualizar(x)
    actualizar(y)
    return y


class AVL:
    def __init__(self):
        self.raiz = None
        self.ultima_rotacion = None

    def insertar(self, valor):
        self.ultima_rotacion = None
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        # 1) inserción común de ABB
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self._insertar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._insertar(nodo.der, valor)
        else:
            self.ultima_rotacion = "repetido, se ignora"
            return nodo

        # 2) actualizar altura y revisar balance al volver de la recursión
        actualizar(nodo)
        fb = factor_balance(nodo)

        if fb > 1:  # cargado a la izquierda
            if valor < nodo.izq.valor:
                self.ultima_rotacion = f"LL en {nodo.valor}: rotación simple a derecha"
                return rotar_derecha(nodo)
            self.ultima_rotacion = f"LR en {nodo.valor}: rotación doble izquierda-derecha"
            nodo.izq = rotar_izquierda(nodo.izq)
            return rotar_derecha(nodo)

        if fb < -1:  # cargado a la derecha
            if valor > nodo.der.valor:
                self.ultima_rotacion = f"RR en {nodo.valor}: rotación simple a izquierda"
                return rotar_izquierda(nodo)
            self.ultima_rotacion = f"RL en {nodo.valor}: rotación doble derecha-izquierda"
            nodo.der = rotar_derecha(nodo.der)
            return rotar_izquierda(nodo)

        return nodo

    # ---- barridos para mostrar el resultado ----
    def pre_orden(self):
        res = []

        def visitar(n):
            if n:
                res.append(n.valor)
                visitar(n.izq)
                visitar(n.der)

        visitar(self.raiz)
        return res

    def simetrico(self):
        res = []

        def visitar(n):
            if n:
                visitar(n.izq)
                res.append(n.valor)
                visitar(n.der)

        visitar(self.raiz)
        return res

    def por_niveles(self):
        res = []
        cola = deque([self.raiz] if self.raiz else [])
        while cola:
            n = cola.popleft()
            res.append(n.valor)
            if n.izq:
                cola.append(n.izq)
            if n.der:
                cola.append(n.der)
        return res

    def dibujar(self):
        """Árbol acostado: la raíz a la izquierda, el subárbol derecho arriba."""
        lineas = []

        def visitar(n, prefijo, es_der):
            if n is None:
                return
            visitar(n.der, prefijo + ("    " if es_der else "│   "), True)
            conector = "┌── " if es_der else "└── "
            lineas.append(f"{prefijo}{conector}{n.valor} (FB={factor_balance(n)})")
            visitar(n.izq, prefijo + ("│   " if es_der else "    "), False)

        if self.raiz:
            visitar(self.raiz.der, "", True)
            lineas.append(f"{self.raiz.valor} (FB={factor_balance(self.raiz)})")
            visitar(self.raiz.izq, "", False)
        return "\n".join(lineas)


def leer_valores(ruta):
    with open(ruta) as f:
        tokens = [t for t in re.split(r"[\s,;]+", f.read()) if t]
    valores = []
    for t in tokens:
        try:
            valores.append(int(t))
        except ValueError:
            try:
                valores.append(float(t))
            except ValueError:
                valores.append(t)  # si no son números, se comparan como texto
    return valores


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Uso: python avl.py <archivo-de-datos>")

    arbol = AVL()
    print("Inserciones:")
    for v in leer_valores(sys.argv[1]):
        arbol.insertar(v)
        detalle = arbol.ultima_rotacion or "sin rotación"
        print(f"  insertar {v}: {detalle}")

    print("\nÁrbol final (acostado, derecha arriba):")
    print(arbol.dibujar())
    print(f"\nAltura: {altura(arbol.raiz)}")
    print("Pre-orden:  ", " ".join(map(str, arbol.pre_orden())))
    print("Simétrico:  ", " ".join(map(str, arbol.simetrico())))
    print("Por niveles:", " ".join(map(str, arbol.por_niveles())))
