#Ejercicio 3: Representar listas por medio de celdas con enlace simple

# Nodo base
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __repr__(self):
        return f"[{self.valor}]"


# Lista enlazada simple
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar(self, valor):
        if self.cabeza is None:
            return False
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return True
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.siguiente
        return False

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def __repr__(self):
        nodos = []
        actual = self.cabeza
        while actual:
            nodos.append(str(actual.valor))
            actual = actual.siguiente
        return "INICIO → " + " → ".join(nodos) + " → None"


# Ejemplo de uso
def lista():
    lista = ListaEnlazada()
    lista.agregar_al_final(5)
    lista.agregar_al_final(15)
    lista.agregar_al_final(25)
    print(lista)
    # INICIO → 5 → 15 → 25 → None

    lista.eliminar(15)
    print(lista)
    # INICIO → 5 → 25 → None

    print("¿Está el 25 en la lista?", lista.buscar(25))
    print("¿Está el 15 en la lista?", lista.buscar(15))


if __name__ == "__main__":
    print("Ejercicio: Lista enlazada simple")
    lista()
