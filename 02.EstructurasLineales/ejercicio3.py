# Ejercicio 3 - Representar listas por medio de celdas con enlace simple.
# Cada celda guarda un dato y una referencia a la celda siguiente.

class Celda:
    """Nodo de la lista: dato + enlace al siguiente."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:

    def __init__(self):
        self.cabeza = None   # referencia externa a la primera celda
        self.tamanio = 0

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_al_inicio(self, dato):
        nueva = Celda(dato)
        nueva.siguiente = self.cabeza
        self.cabeza = nueva
        self.tamanio += 1

    def insertar_al_final(self, dato):
        nueva = Celda(dato)
        if self.cabeza is None:
            self.cabeza = nueva
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nueva
        self.tamanio += 1

    def buscar(self, dato):
        """True si el dato esta en la lista."""
        actual = self.cabeza
        while actual is not None and actual.dato != dato:
            actual = actual.siguiente
        return actual is not None

    def eliminar(self, dato):
        """Saca la primera celda que contenga el dato. True si lo elimino."""
        anterior = None
        actual = self.cabeza
        while actual is not None and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            return False

        if actual is self.cabeza:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

        actual.siguiente = None
        self.tamanio -= 1
        return True

    def recorrer(self):
        """Devuelve los datos en una lista de Python (solo para mostrar)."""
        datos = []
        actual = self.cabeza
        while actual is not None:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

    def __len__(self):
        return self.tamanio

    def __str__(self):
        if self.esta_vacia():
            return "(lista vacia)"
        return " -> ".join(str(d) for d in self.recorrer()) + " -> None"


if __name__ == "__main__":
    lista = ListaEnlazada()

    print("Lista recien creada:", lista)

    for valor in [2, 52, 18, 36, 13]:
        lista.insertar_al_final(valor)
    print("Despues de insertar al final:", lista)

    lista.insertar_al_inicio(96)
    print("Despues de insertar 96 al inicio:", lista)

    print("Busco 18:", lista.buscar(18))
    print("Busco 77:", lista.buscar(77))

    lista.eliminar(18)
    print("Elimino 18 (del medio):", lista)

    lista.eliminar(96)
    print("Elimino 96 (la cabeza):", lista)

    lista.eliminar(13)
    print("Elimino 13 (la ultima):", lista)

    print("Elimino 77 (no esta):", lista.eliminar(77))
    print("Longitud final:", len(lista))
