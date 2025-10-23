import sys

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, valor):
        anterior = None
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado

def procesar_operaciones_lista(ruta):
    lista = ListaSimple()
    consultas = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split()
            if not partes:
                continue
            operacion = partes[0].upper()
            if operacion == "INSERT" and len(partes) > 1:
                valor = " ".join(partes[1:])
                lista.insertar(valor)
            elif operacion == "DELETE" and len(partes) > 1:
                valor = " ".join(partes[1:])
                lista.eliminar(valor)
            elif operacion == "FIND" and len(partes) > 1:
                valor = " ".join(partes[1:])
                consultas.append((valor, lista.buscar(valor)))
    return lista.a_lista(), consultas

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python lista_simple.py archivo_operaciones")
        sys.exit(1)
    final, consultas = procesar_operaciones_lista(sys.argv[1])
    for valor, existe in consultas:
        print(f"FIND {valor}: {existe}")
    print(final)
