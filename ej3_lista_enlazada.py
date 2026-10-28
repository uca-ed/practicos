"""
Ejercicio 3: Listas representadas por medio de celdas con enlace simple.

Cada celda (Nodo) guarda un dato y una referencia a la siguiente celda.
La lista mantiene una referencia a la cabeza.
"""


class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        self.cabeza = Nodo(dato, self.cabeza)

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def insertar_en_posicion(self, dato, posicion):
        if posicion < 0:
            raise IndexError("Posicion invalida")
        if posicion == 0:
            self.insertar_al_inicio(dato)
            return
        actual = self.cabeza
        for _ in range(posicion - 1):
            if actual is None:
                raise IndexError("Posicion fuera de rango")
            actual = actual.siguiente
        if actual is None:
            raise IndexError("Posicion fuera de rango")
        actual.siguiente = Nodo(dato, actual.siguiente)

    def eliminar(self, dato):
        """Elimina la primera celda cuyo dato coincide. Devuelve True/False."""
        anterior = None
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def __len__(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def __str__(self):
        return " -> ".join(str(x) for x in self) + " -> NULL"


if __name__ == "__main__":
    lista = ListaEnlazada()
    for valor in [10, 20, 30]:
        lista.insertar_al_final(valor)
    lista.insertar_al_inicio(5)
    lista.insertar_en_posicion(15, 2)

    print("Lista:", lista)
    print("Longitud:", len(lista))
    print("Contiene 20?", lista.buscar(20))

    lista.eliminar(20)
    print("Lista tras eliminar 20:", lista)

    lista.eliminar(999)  # no existe, no rompe nada
    print("Lista tras intentar eliminar un valor inexistente:", lista)
