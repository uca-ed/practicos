""""
3. Representar listas por medio de celdas con enlace simple.
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None 

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None 

    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

if __name__ == "__main__":
    lista = ListaEnlazada()

    lista.insertar(10)
    lista.insertar(20)
    lista.insertar(30)
    
    print("Lista despues de insertar 10, 20, 30:", lista.mostrar())
    
    lista.insertar(40)
    lista.insertar(50)
    
    print("Lista final despues de insertar 40, 50:", lista.mostrar())
