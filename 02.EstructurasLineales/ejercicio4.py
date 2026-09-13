# Ejercicio 4 - Radix Sort. Ordena las palabras de un archivo.
#
# Se usa la version LSD: se recorre de la ultima posicion a la primera y en
# cada pasada se reparten las palabras en r colas (una por simbolo del
# alfabeto) y despues se concatenan las colas en orden.
#
# Las palabras mas cortas se completan con un simbolo de relleno que va
# primero en el alfabeto, asi "casa" queda antes que "casaca".

import sys

RELLENO = ""   # simbolo de relleno, menor que cualquier letra


class Cola:
    """Cola simple, usada como balde del radix."""

    def __init__(self):
        self.items = []
        self.pos = 0

    def esta_vacia(self):
        return self.pos >= len(self.items)

    def enqueue(self, valor):
        self.items.append(valor)

    def dequeue(self):
        if self.esta_vacia():
            raise IndexError("Error: la cola esta vacia")
        rta = self.items[self.pos]
        self.pos += 1
        return rta


def armar_alfabeto(palabras):
    """Alfabeto ordenado con todos los simbolos que aparecen, mas el relleno."""
    simbolos = set()
    for palabra in palabras:
        for letra in palabra:
            simbolos.add(letra)
    return [RELLENO] + sorted(simbolos)


def radix_sort(palabras):
    if len(palabras) == 0:
        return []

    p = max(len(palabra) for palabra in palabras)   # cantidad de pasadas
    alfabeto = armar_alfabeto(palabras)
    posicion = {}
    for i in range(len(alfabeto)):
        posicion[alfabeto[i]] = i

    cola = list(palabras)

    for j in range(p - 1, -1, -1):          # de la ultima letra a la primera
        baldes = []
        for i in range(len(alfabeto)):      # vaciar Q0, Q1, ..., Qr-1
            baldes.append(Cola())

        for palabra in cola:                # mientras Q no este vacia
            letra = palabra[j] if j < len(palabra) else RELLENO
            baldes[posicion[letra]].enqueue(palabra)

        cola = []                           # concatenar (Q0, Q1, ..., Qr-1)
        for balde in baldes:
            while not balde.esta_vacia():
                cola.append(balde.dequeue())

    return cola


def leer_palabras(nombre_archivo):
    palabras = []
    archivo = open(nombre_archivo, "r")
    for linea in archivo:
        for palabra in linea.split():
            palabras.append(palabra.strip())
    archivo.close()
    return palabras


if __name__ == "__main__":
    archivo = sys.argv[1] if len(sys.argv) > 1 else "palabras.txt"

    palabras = leer_palabras(archivo)
    print("Palabras sin ordenar:")
    print(palabras)

    ordenadas = radix_sort(palabras)
    print()
    print("Palabras ordenadas con Radix Sort:")
    for palabra in ordenadas:
        print(" ", palabra)
