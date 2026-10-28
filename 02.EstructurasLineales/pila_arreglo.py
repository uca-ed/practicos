import os

class PilaArreglo:
    def __init__(self, capacidad=100):
        self.max = capacidad
        self.datos = [None] * self.max
        self.tope = -1

    def push(self, valor):
        if self.tope == self.max - 1:
            print("Error: Pila Llena (Overflow)")
            return
        self.tope += 1
        self.datos[self.tope] = valor

    def pop(self):
        if self.tope == -1:
            print("Error: Pila Vacía (Underflow)")
            return None
        valor = self.datos[self.tope]
        self.datos[self.tope] = None
        self.tope -= 1
        return valor

    def mostrar_estado(self):
        print(f"Estado final de la Pila (base a tope): {self.datos[:self.tope + 1]}")


def procesar_archivo_pila(ruta_archivo):
    pila = PilaArreglo()
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(',')
                comando = partes[0].strip().upper()

                if comando == "PUSH":
                    valor = int(partes[1].strip())
                    pila.push(valor)
                elif comando == "POP":
                    pila.pop()
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta_archivo}")

    pila.mostrar_estado()


if __name__ == "__main__":
    procesar_archivo_pila("operaciones_pila.txt")
