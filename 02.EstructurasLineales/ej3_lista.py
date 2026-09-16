"""
Ejercicio 3 - Representar LISTAS por medio de celdas con ENLACE SIMPLE.
"""


class Celda:
    """Celda con enlace simple."""

    def __init__(self, valor):
        self.valor = valor
        self.sig = None


class ListaEnlaceSimple:

    def __init__(self):
        self.primero = None


    def vacia(self):
        return self.primero is None

    def longitud(self):
        n = 0
        actual = self.primero
        while actual is not None:
            n = n + 1
            actual = actual.sig
        return n

    def buscar(self, valor):
        
        pos = 0
        actual = self.primero
        while actual is not None:
            if actual.valor == valor:
                return pos
            pos = pos + 1
            actual = actual.sig
        return -1

    def contenido(self):
        elems = []
        actual = self.primero
        while actual is not None:
            elems.append(actual.valor)
            actual = actual.sig
        return elems

    

    def insertar_al_principio(self, valor):
        aux = Celda(valor)
        aux.sig = self.primero      # engancho la nueva antes de la vieja primera
        self.primero = aux          # recien ahora muevo 'primero'

    def insertar_al_final(self, valor):
        aux = Celda(valor)
        if self.primero is None:
            self.primero = aux
            return
        actual = self.primero
        while actual.sig is not None:   # camino hasta la ultima celda
            actual = actual.sig
        actual.sig = aux

    def insertar_ordenado(self, valor):
        """Busca el lugar que le corresponde y lo inserta ahi."""
        aux = Celda(valor)

        # caso 1: va al principio (lista vacia, o el nuevo es el menor)
        if self.primero is None or valor <= self.primero.valor:
            aux.sig = self.primero
            self.primero = aux
            return

        # caso 2: busco la celda DETRAS de la cual va el nuevo
        actual = self.primero
        while actual.sig is not None and actual.sig.valor < valor:
            actual = actual.sig

        aux.sig = actual.sig    # el nuevo apunta al que seguia
        actual.sig = aux        # el anterior apunta al nuevo



    def eliminar(self, valor):
        """Elimina la primera celda con ese valor. Devuelve True si la encontro."""
        if self.primero is None:
            return False

        # caso 1: es la primera celda
        if self.primero.valor == valor:
            self.primero = self.primero.sig
            return True

        # caso 2: busco la celda ANTERIOR a la que quiero borrar
        actual = self.primero
        while actual.sig is not None and actual.sig.valor != valor:
            actual = actual.sig

        if actual.sig is None:
            return False        # no estaba

        actual.sig = actual.sig.sig   # salteo la celda: queda huerfana
        return True

    def __str__(self):
        if self.primero is None:
            return "<vacia>"
        partes = []
        actual = self.primero
        while actual is not None:
            partes.append(f"[{actual.valor}|*]")
            actual = actual.sig
        return "primero -> " + " -> ".join(partes) + " -> None"


def demo():
    print("Lista con celdas de ENLACE SIMPLE\n")
    lista = ListaEnlaceSimple()

    print("1) Insertar al final: 10, 20, 30")
    for v in [10, 20, 30]:
        lista.insertar_al_final(v)
        print(f"   insertar_al_final({v})     {lista}")

    print("\n2) Insertar al principio: 5")
    lista.insertar_al_principio(5)
    print(f"   insertar_al_principio(5)  {lista}")

    print("\n3) Insertar ordenado: 25 (tiene que quedar entre 20 y 30)")
    lista.insertar_ordenado(25)
    print(f"   insertar_ordenado(25)     {lista}")

    print("\n4) Insertar ordenado: 1 (queda al principio) y 99 (queda al final)")
    lista.insertar_ordenado(1)
    print(f"   insertar_ordenado(1)      {lista}")
    lista.insertar_ordenado(99)
    print(f"   insertar_ordenado(99)     {lista}")

    print("\n5) Buscar")
    for v in [25, 77]:
        pos = lista.buscar(v)
        print(f"   buscar({v})  ->  " +
              (f"esta en la posicion {pos}" if pos >= 0 else "no esta"))

    print("\n6) Eliminar")
    for v in [1, 25, 77]:
        ok = lista.eliminar(v)
        print(f"   eliminar({v})  ->  {'OK  ' if ok else 'no estaba'}  {lista}")

    print(f"\nRESULTADO FINAL")
    print(f"  Lista     : {lista}")
    print(f"  Contenido : {lista.contenido()}")
    print(f"  Longitud  : {lista.longitud()}")


if __name__ == "__main__":
    demo()
