class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Lista:
    def __init__(self):
        self.primero = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.primero
        self.primero = nuevo

    def insertar_final(self, dato):
        nuevo = Nodo(dato)

        if self.primero is None:
            self.primero = nuevo
            return

        actual = self.primero
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def buscar(self, dato):
        actual = self.primero
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, dato):
        actual = self.primero
        anterior = None

        while actual is not None:
            if actual.dato == dato:
                if anterior is None:
                    self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True

            anterior = actual
            actual = actual.siguiente

        return False

    def mostrar(self):
        actual = self.primero
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")


lista = Lista()
lista.insertar_final(10)
lista.insertar_final(20)
lista.insertar_final(30)

print("Lista:")
lista.mostrar()

print("¿Está 20?:", lista.buscar(20))
lista.eliminar(20)
print("Lista luego de eliminar 20:")
lista.mostrar()
