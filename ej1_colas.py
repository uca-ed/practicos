"""
Ejercicio 1: Colas representadas sobre un arreglo.

La cola se implementa como un arreglo circular de tamano fijo, con
punteros a frente y fondo. Se lee un archivo de operaciones (ENQUEUE/DEQUEUE)
y se muestra el estado final de la cola.

Formato del archivo de operaciones:
    ENQUEUE,<valor>
    DEQUEUE,
"""

import os
import sys


class Cola:
    def __init__(self, capacidad=100):
        self.arreglo = [None] * capacidad
        self.capacidad = capacidad
        self.frente = 0
        self.fondo = 0
        self.cantidad = 0

    def encolar(self, valor):
        if self.cantidad == self.capacidad:
            raise OverflowError("Cola llena")
        self.arreglo[self.fondo] = valor
        self.fondo = (self.fondo + 1) % self.capacidad
        self.cantidad += 1

    def desencolar(self):
        if self.cantidad == 0:
            raise IndexError("Cola vacia")
        valor = self.arreglo[self.frente]
        self.arreglo[self.frente] = None
        self.frente = (self.frente + 1) % self.capacidad
        self.cantidad -= 1
        return valor

    def esta_vacia(self):
        return self.cantidad == 0

    def elementos(self):
        """Devuelve los elementos actuales en orden, desde el frente."""
        resultado = []
        idx = self.frente
        for _ in range(self.cantidad):
            resultado.append(self.arreglo[idx])
            idx = (idx + 1) % self.capacidad
        return resultado


def procesar_archivo(ruta, capacidad=100):
    cola = Cola(capacidad)
    with open(ruta, encoding="utf-8") as f:
        for num_linea, linea in enumerate(f, start=1):
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split(",")
            operacion = partes[0].strip().upper()

            if operacion == "ENQUEUE":
                valor = partes[1].strip()
                cola.encolar(valor)
            elif operacion == "DEQUEUE":
                if cola.esta_vacia():
                    print(f"Linea {num_linea}: DEQUEUE sobre cola vacia, se ignora")
                else:
                    cola.desencolar()
            else:
                print(f"Linea {num_linea}: operacion desconocida '{operacion}', se ignora")
    return cola


if __name__ == "__main__":
    ruta_defecto = os.path.join(os.path.dirname(__file__), "data", "operaciones_cola.txt")
    ruta = sys.argv[1] if len(sys.argv) > 1 else ruta_defecto

    cola_final = procesar_archivo(ruta)
    print("Estado final de la cola (frente -> fondo):")
    print(cola_final.elementos())
