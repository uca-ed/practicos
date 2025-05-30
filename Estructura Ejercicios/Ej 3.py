class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None

class Lista:
    def __init__(self):
        self.inicio = None

    def agregar(self, x):
        nuevo = Nodo(x)
        nuevo.sig = self.inicio
        self.inicio = nuevo

    def mostrar(self):
        aux = self.inicio
        while aux is not None:
            print(aux.valor, end=" -> ")
            aux = aux.sig
        print("None")

    def eliminar(self, x):
        ant = None
        act = self.inicio
        while act is not None and act.valor != x:
            ant = act
            act = act.sig
        if act is None:
            print(x, "no encontrado")
            return
        if ant is None:
            self.inicio = act.sig
        else:
            ant.sig = act.sig
        print(x, "eliminado")

# Ejemplo de uso
l = Lista()
l.agregar(10)
l.agregar(20)
l.agregar(30)
print("Lista original:")
l.mostrar()
l.eliminar(20)
print("Después de eliminar 20:")
l.mostrar()
