"""3. Representar listas por medio de celdas con enlace simple.  """

# Clase que representa una celda o nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato      
        self.siguiente = None 

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo


    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" , ")
            actual = actual.siguiente
        print("None")


def main():
    lista = ListaEnlazada()
    lista.agregar(10)
    lista.agregar(20)
    lista.agregar(30)
    lista.mostrar()

main()
