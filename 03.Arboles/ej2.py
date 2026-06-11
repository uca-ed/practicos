class NodoAVL:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None
        self.altura = 1

class ArbolAVL:
    
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izq) - self.obtener_altura(nodo.der)

    def rotar_derecha(self, y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self.obtener_altura(y.izq), self.obtener_altura(y.der))
        x.altura = 1 + max(self.obtener_altura(x.izq), self.obtener_altura(x.der))
        return x

    def rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self.obtener_altura(x.izq), self.obtener_altura(x.der))
        y.altura = 1 + max(self.obtener_altura(y.izq), self.obtener_altura(y.der))
        return y

    def insertar(self, raiz, dato):
        if not raiz:
            return NodoAVL(dato)
        
        if dato < raiz.dato:
            raiz.izq = self.insertar(raiz.izq, dato)
        elif dato > raiz.dato:
            raiz.der = self.insertar(raiz.der, dato)
        else:
            return raiz

        raiz.altura = 1 + max(self.obtener_altura(raiz.izq), self.obtener_altura(raiz.der))
        balance = self.obtener_balance(raiz)

        # Caso Izquierda-Izquierda
        if balance > 1 and dato < raiz.izq.dato:
            return self.rotar_derecha(raiz)

        # Caso Derecha-Derecha
        if balance < -1 and dato > raiz.der.dato:
            return self.rotar_izquierda(raiz)

        # Caso Izquierda-Derecha
        if balance > 1 and dato > raiz.izq.dato:
            raiz.izq = self.rotar_izquierda(raiz.izq)
            return self.rotar_derecha(raiz)

        # Caso Derecha-Izquierda
        if balance < -1 and dato < raiz.der.dato:
            raiz.der = self.rotar_derecha(raiz.der)
            return self.rotar_izquierda(raiz)

        return raiz

    def mostrar_arbol(self, nodo, prefijo="", es_izq=True):
        if nodo:
            print(prefijo + ("└── " if es_izq else "├── ") + str(nodo.dato) + f" (Alt: {nodo.altura})")
            self.mostrar_arbol(nodo.izq, prefijo + ("    " if es_izq else "│   "), True)
            self.mostrar_arbol(nodo.der, prefijo + ("    " if es_izq else "│   "), False)

if __name__ == "__main__":
    avl = ArbolAVL()
    raiz = None
    datos_a_insertar = [10, 20, 30, 40, 50, 25]
    
    print("Insertando los valores:", datos_a_insertar)
    for valor in datos_a_insertar:
        raiz = avl.insertar(raiz, valor)
        
    print("\nEstructura final del Árbol AVL balanceado:")
    avl.mostrar_arbol(raiz)
