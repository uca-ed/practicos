class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


def insertar_al_final(primero, valor):
    nuevo = Nodo(valor)

    if primero is None:
        return nuevo

    actual = primero
    while actual.siguiente is not None:
        actual = actual.siguiente

    actual.siguiente = nuevo
    return primero


def mostrar_lista(primero):
    actual = primero
    while actual is not None:
        print(actual.valor, end=" -> ")
        actual = actual.siguiente
    print("None")


# La lista comienza vacia.
primero = None

primero = insertar_al_final(primero, 10)
primero = insertar_al_final(primero, 20)
primero = insertar_al_final(primero, 30)

mostrar_lista(primero)
