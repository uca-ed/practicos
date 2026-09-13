# Ejercicio 1 - Representar colas sobre un arreglo.
# Lee un archivo de operaciones (ENQUEUE,valor / DEQUEUE,) y opera sobre una
# cola vacia. Al final muestra el estado de la cola.

import sys

CAPACIDAD = 10


class Cola:
    """Cola FIFO implementada sobre un arreglo de tamaño fijo, circular."""

    def __init__(self, capacidad):
        self.arr = [None] * capacidad
        self.pos = 0          # posicion del frente
        self.longitud = 0     # cantidad de elementos guardados

    def esta_vacia(self):
        return self.longitud == 0

    def esta_llena(self):
        return self.longitud == len(self.arr)

    def enqueue(self, valor):
        if self.esta_llena():
            raise IndexError("Error: la cola esta llena")
        self.arr[(self.pos + self.longitud) % len(self.arr)] = valor
        self.longitud += 1

    def dequeue(self):
        if self.esta_vacia():
            raise IndexError("Error: la cola esta vacia")
        rta = self.arr[self.pos]
        self.arr[self.pos] = None
        self.pos = (self.pos + 1) % len(self.arr)
        self.longitud -= 1
        return rta

    def contenido(self):
        """Devuelve los elementos del frente hacia el final."""
        elementos = []
        for i in range(self.longitud):
            elementos.append(self.arr[(self.pos + i) % len(self.arr)])
        return elementos

    def __str__(self):
        return "frente -> " + str(self.contenido()) + " <- final"


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


def procesar(operaciones, cola):
    for op, arg in operaciones:
        if op == "ENQUEUE":
            cola.enqueue(arg)
            print("ENQUEUE", arg, "->", cola)
        elif op == "DEQUEUE":
            valor = cola.dequeue()
            print("DEQUEUE  -> saco", valor, "|", cola)
        else:
            print("Operacion desconocida:", op)


if __name__ == "__main__":
    archivo = sys.argv[1] if len(sys.argv) > 1 else "operaciones_colas.txt"

    cola = Cola(CAPACIDAD)
    procesar(leer_operaciones(archivo), cola)

    print()
    print("Resultado final:", cola)
    print("Cantidad de elementos:", cola.longitud)
