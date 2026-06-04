class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        print(f"Insertado: {dato}")

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        print(f"Insertado al inicio: {dato}")

    def eliminar(self, dato):
        if self.cabeza is None:
            print("Lista vacía")
            return

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            print(f"Eliminado: {dato}")
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                print(f"Eliminado: {dato}")
                return
            actual = actual.siguiente

        print(f"Elemento {dato} no encontrado")

    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual is not None:
            if actual.dato == dato:
                print(f"Elemento {dato} encontrado en posición {posicion}")
                return True
            actual = actual.siguiente
            posicion += 1
        print(f"Elemento {dato} no encontrado")
        return False

    def mostrar(self):
        if self.cabeza is None:
            print("Lista vacía")
            return
        actual = self.cabeza
        elementos = []
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print("Lista: " + " -> ".join(elementos) + " -> None")


def main():
    lista = ListaEnlazada()

    lista.insertar_al_final(1)
    lista.insertar_al_final(2)
    lista.insertar_al_final(3)
    lista.insertar_al_final(4)
    lista.insertar_al_inicio(0)

    print()
    lista.mostrar()

    print()
    lista.buscar(3)
    lista.buscar(99)

    print()
    lista.eliminar(3)
    lista.mostrar()

    lista.eliminar(0)
    lista.mostrar()

if __name__ == "__main__":
    main()
