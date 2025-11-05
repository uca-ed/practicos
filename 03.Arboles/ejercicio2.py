"""
2. Crear un árbol AVL realizando las inserciones dadas en el archivo de datos.
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None  
        self.derecha = None  
        self.altura = 1       

class AVL:
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def rotacion_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha

        x.derecha = y
        y.izquierda = T2

        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))
        x.altura = 1 + max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha))

        return x

    def rotacion_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda

        y.izquierda = x
        x.derecha = T2

        x.altura = 1 + max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def insertar(self, raiz, valor):
        if not raiz:
            return Nodo(valor)
        
        if valor < raiz.valor:
            raiz.izquierda = self.insertar(raiz.izquierda, valor)
        elif valor > raiz.valor:
            raiz.derecha = self.insertar(raiz.derecha, valor)
        else:
            return raiz

        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierda), self.obtener_altura(raiz.derecha))

        balance = self.obtener_balance(raiz)

        if balance > 1 and valor < raiz.izquierda.valor:
            return self.rotacion_derecha(raiz)

        if balance < -1 and valor > raiz.derecha.valor:
            return self.rotacion_izquierda(raiz)

        if balance > 1 and valor > raiz.izquierda.valor:
            raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
            return self.rotacion_derecha(raiz)

        if balance < -1 and valor < raiz.derecha.valor:
            raiz.derecha = self.rotacion_derecha(raiz.derecha)
            return self.rotacion_izquierda(raiz)

        return raiz

    def construir_avl_desde_arreglo(self, arreglo):
        raiz = None
        for elemento in arreglo:
            raiz = self.insertar(raiz, elemento)
        return raiz
    
    def imprimir_inorden(self, raiz):
        if not raiz:
            return
        
        self.imprimir_inorden(raiz.izquierda)
        
        val_izq = raiz.izquierda.valor if raiz.izquierda else "None"
        val_der = raiz.derecha.valor if raiz.derecha else "None"
        
        print(f"({raiz.valor}, izq: {val_izq}, der: {val_der}, altura: {raiz.altura})")
        
        self.imprimir_inorden(raiz.derecha)


# Para comparar, implementamos un BST simple sin balanceo
class Nodo_aux:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None  
        self.derecha = None   
        self.altura = 1       

class BSTSimple:
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def insertar_simple(self, raiz, valor):
        if raiz is None:
            return Nodo_aux(valor)

        if valor < raiz.valor:
            raiz.izquierda = self.insertar_simple(raiz.izquierda, valor)
        elif valor > raiz.valor:
            raiz.derecha = self.insertar_simple(raiz.derecha, valor)
        else:
            return raiz
            
        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierda), self.obtener_altura(raiz.derecha))
        
        return raiz

    def construir_bst_desde_arreglo(self, arreglo):
        """
        Función principal para crear el BST simple desde un arreglo.
        """
        raiz = None
        for elemento in arreglo:
            raiz = self.insertar_simple(raiz, elemento)
        return raiz
    
    def imprimir_inorden(self, raiz):
        if not raiz:
            return
        
        self.imprimir_inorden(raiz.izquierda)
        
        val_izq = raiz.izquierda.valor if raiz.izquierda else "None"
        val_der = raiz.derecha.valor if raiz.derecha else "None"
        
        print(f"({raiz.valor}, izq: {val_izq}, der: {val_der}, altura: {raiz.altura})")
        
        self.imprimir_inorden(raiz.derecha)

# Ejemplo de Uso

def prueba(arr):
    arreglo_numeros = arr
    mi_avl = AVL()
    print()
    print(f"\n Arreglo de entrada: {arreglo_numeros}")

    raiz_avl = mi_avl.construir_avl_desde_arreglo(arreglo_numeros)

    print("Arbol AVL construido. Recorrido Inorden:")
    mi_avl.imprimir_inorden(raiz_avl)
    mi_bst = BSTSimple()
    raiz_bst = mi_bst.construir_bst_desde_arreglo(arreglo_numeros)

    print("\n Recorrido Inorden del BST Simple (para comparar con arbol AVL):")
    mi_bst.imprimir_inorden(raiz_bst)



arreglo_numeros = [10, 20, 30, 40, 50, 25] 
prueba(arreglo_numeros)
arreglo_numeros = [50, 20, 80, 10, 30, 70, 90, 25] 
prueba(arreglo_numeros)
arreglo_numeros = [1, 5, 2, 6, 3, 7, 4] 
prueba(arreglo_numeros)