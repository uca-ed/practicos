#Simulo listas enlazadas con clases

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def insertarFinal(self, valor):
        nuevo = Nodo(valor)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            aux = self.inicio
            while aux.siguiente:
                aux = aux.siguiente
            aux.siguiente = nuevo
        print(f"Se agrego el valor {valor} al final de la lista")

    def insertarPosicion(self,valor,pos):
        nuevo = Nodo(valor)

        # Caso 1: lista vacía o posición 0 → insertar al inicio
        if pos <= 0 or self.inicio is None:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
            return

        # Caso 2: recorrer hasta la posición anterior
        indice = 0
        aux = self.inicio
        while aux.siguiente and indice < pos - 1:
            aux = aux.siguiente
            indice += 1
        if not aux.siguiente:
            print(f"La posicion no existe, se agrego el valor {valor} al final de la lista")
        # Insertar en la posición
        nuevo.siguiente = aux.siguiente
        aux.siguiente = nuevo
        print(f"Se agrego el valor {valor} a la posicion {pos} de la lista")


    def eliminar(self, valor):
        anterior = None
        actual = self.inicio
        while actual and actual.dato != valor:
            anterior = actual
            actual = actual.siguiente
        if actual:
            if anterior is None:
                self.inicio = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
            print(f"Se elimino el valor {valor} de la lista")
        else:
            print(f"El valor {valor} no se pudo eliminar pues no estaba en la lista")

    def mostrar(self):
        aux = self.inicio
        while aux:
            print(aux.dato, end=" -> ")
            aux = aux.siguiente
        print("NULL")


def ProcesarLista(archivo):
    lista = ListaEnlazada()
    with open(archivo, 'r') as f:
        for linea in f:
            partes = linea.strip().split()
            if not partes:
                continue
            operacion = partes[0].upper()

            if operacion == "INSERTARFINAL" and len(partes) > 1:
                lista.insertarFinal(partes[1])
            elif operacion == "INSERTARPOSICION" and len(partes) > 2:
                lista.insertarPosicion(partes[1],int(partes[2]))
            elif operacion == "ELIMINAR" and len(partes) > 1:
                lista.eliminar(partes[1])
            elif operacion == "MOSTRAR":
                lista.mostrar()
            else:
                print(f"Operación inválida: {linea.strip()}")

    print("\nLista final:")
    lista.mostrar()

def main():
    arch="OpsLista.txt"
    ProcesarLista(arch)
main()