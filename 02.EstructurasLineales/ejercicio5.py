# Ejercicio 5 - T-Sort sobre un grafo dirigido leido de un archivo.
# Si el grafo tiene un ciclo no se puede calcular y se avisa.
#
# Formato del archivo: una arista por linea, "origen,destino".
# Una linea con un solo nombre carga un vertice suelto (sin aristas).
#
# Metodo usado: grados de entrada (Kahn). Se arranca por los vertices que no
# tienen predecesores y se los va sacando de a uno con una cola.

import sys


class Grafo:
    """Grafo dirigido con listas de adyacencia."""

    def __init__(self):
        self.adyacentes = {}    # vertice -> lista de sucesores
        self.vertices = []      # en orden de aparicion, para que la salida
                                # sea siempre la misma

    def agregar_vertice(self, v):
        if v not in self.adyacentes:
            self.adyacentes[v] = []
            self.vertices.append(v)

    def agregar_arista(self, origen, destino):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.adyacentes[origen].append(destino)


def leer_grafo(nombre_archivo):
    grafo = Grafo()
    archivo = open(nombre_archivo, "r")
    for linea in archivo:
        linea = linea.strip()
        if linea == "" or linea.startswith("#"):
            continue
        partes = linea.split(",")
        origen = partes[0].strip()
        if len(partes) > 1 and partes[1].strip() != "":
            grafo.agregar_arista(origen, partes[1].strip())
        else:
            grafo.agregar_vertice(origen)
    archivo.close()
    return grafo


def calcular_grados_de_entrada(grafo):
    grados = {}
    for v in grafo.vertices:
        grados[v] = 0
    for v in grafo.vertices:
        for sucesor in grafo.adyacentes[v]:
            grados[sucesor] += 1
    return grados


def t_sort(grafo):
    """Devuelve (secuencia, hay_ciclo)."""
    grados = calcular_grados_de_entrada(grafo)

    # cola con todos los vertices que no tienen predecesores
    cola = []
    for v in grafo.vertices:
        if grados[v] == 0:
            cola.append(v)

    secuencia = []
    frente = 0
    while frente < len(cola):
        v = cola[frente]        # dequeue
        frente += 1
        secuencia.append(v)

        for sucesor in grafo.adyacentes[v]:
            grados[sucesor] -= 1
            if grados[sucesor] == 0:
                cola.append(sucesor)

    # si quedaron vertices afuera es porque forman un ciclo
    hay_ciclo = len(secuencia) < len(grafo.vertices)
    return secuencia, hay_ciclo


if __name__ == "__main__":
    archivo = sys.argv[1] if len(sys.argv) > 1 else "grafo.txt"

    grafo = leer_grafo(archivo)
    print("Vertices:", grafo.vertices)
    print("Aristas:")
    for v in grafo.vertices:
        for sucesor in grafo.adyacentes[v]:
            print("  ", v, "->", sucesor)

    secuencia, hay_ciclo = t_sort(grafo)
    print()
    if hay_ciclo:
        print("No se puede calcular el T-Sort: la estructura es ciclica.")
        faltan = [v for v in grafo.vertices if v not in secuencia]
        print("Vertices involucrados en el ciclo:", faltan)
    else:
        print("Secuencia T-Sort:", " ".join(secuencia))
