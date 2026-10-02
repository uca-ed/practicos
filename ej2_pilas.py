"""
Ejercicio 2: Pilas representadas sobre un arreglo.

La pila se implementa como un arreglo de tamano fijo con un puntero al
tope. Se lee un archivo de operaciones (PUSH/POP) y se muestra el estado
final de la pila.

Formato del archivo de operaciones:
    PUSH,<valor>
    POP,
"""

import os
import sys


class Pila:
    def __init__(self, capacidad=100):
        self.arreglo = [None] * capacidad
        self.capacidad = capacidad
        self.tope = -1  # -1 indica pila vacia

    def apilar(self, valor):
        if self.tope == self.capacidad - 1:
            raise OverflowError("Pila llena")
        self.tope += 1
        self.arreglo[self.tope] = valor

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("Pila vacia")
        valor = self.arreglo[self.tope]
        self.arreglo[self.tope] = None
        self.tope -= 1
        return valor

    def esta_vacia(self):
        return self.tope == -1

    def elementos(self):
        """Devuelve los elementos actuales, desde la base hasta el tope."""
        return [self.arreglo[i] for i in range(self.tope + 1)]


def procesar_archivo(ruta, capacidad=100):
    pila = Pila(capacidad)
    with open(ruta, encoding="utf-8") as f:
        for num_linea, linea in enumerate(f, start=1):
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split(",")
            operacion = partes[0].strip().upper()

            if operacion == "PUSH":
                valor = partes[1].strip()
                pila.apilar(valor)
            elif operacion == "POP":
                if pila.esta_vacia():
                    print(f"Linea {num_linea}: POP sobre pila vacia, se ignora")
                else:
                    pila.desapilar()
            else:
                print(f"Linea {num_linea}: operacion desconocida '{operacion}', se ignora")
    return pila


if __name__ == "__main__":
    ruta_defecto = os.path.join(os.path.dirname(__file__), "data", "operaciones_pila.txt")
    ruta = sys.argv[1] if len(sys.argv) > 1 else ruta_defecto

    pila_final = procesar_archivo(ruta)
    print("Estado final de la pila (base -> tope):")
    print(pila_final.elementos())
