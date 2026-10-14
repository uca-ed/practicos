# Ejercicio 2 - Representar pilas sobre un arreglo.
# Lee un archivo de operaciones (PUSH,valor / POP,) y opera sobre una pila
# vacia. Al final muestra el estado de la pila.

import sys

CAPACIDAD = 10


class Pila:
    """Pila LIFO implementada sobre un arreglo de tamaño fijo."""

    def __init__(self, capacidad):
        self.arr = [None] * capacidad
        self.top = -1     # -1 indica pila vacia

    def esta_vacia(self):
        return self.top == -1

    def esta_llena(self):
        return self.top == len(self.arr) - 1

    def push(self, valor):
        if self.esta_llena():
            raise IndexError("Error: la pila esta llena")
        self.top = self.top + 1
        self.arr[self.top] = valor

    def pop(self):
        if self.esta_vacia():
            raise IndexError("Error: la pila esta vacia")
        rta = self.arr[self.top]
        self.arr[self.top] = None
        self.top = self.top - 1
        return rta

    def contenido(self):
        """Devuelve los elementos de la base hacia el tope."""
        return self.arr[:self.top + 1]

    def __str__(self):
        return "base -> " + str(self.contenido()) + " <- tope"


def leer_operaciones(nombre_archivo):
    """Devuelve una lista de tuplas (operacion, argumento)."""
    operaciones = []
    archivo = open(nombre_archivo, "r")
    for linea in archivo:
        linea = linea.strip()
        if linea == "":
            continue
        partes = linea.split(",")
        op = partes[0].strip().upper()
        arg = partes[1].strip() if len(partes) > 1 else ""
        operaciones.append((op, arg))
    archivo.close()
    return operaciones


def procesar(operaciones, pila):
    for op, arg in operaciones:
        if op == "PUSH":
            pila.push(arg)
            print("PUSH", arg, "->", pila)
        elif op == "POP":
            valor = pila.pop()
            print("POP      -> saco", valor, "|", pila)
        else:
            print("Operacion desconocida:", op)


if __name__ == "__main__":
    archivo = sys.argv[1] if len(sys.argv) > 1 else "operaciones_pilas.txt"

    pila = Pila(CAPACIDAD)
    procesar(leer_operaciones(archivo), pila)

    print()
    print("Resultado final:", pila)
    print("Cantidad de elementos:", pila.top + 1)
