# Ejercicio 7 - Sort topologico sobre un grafo dado en un archivo.
#
# Es el mismo problema que el ejercicio 5, pero resuelto con el otro metodo
# clasico: DFS. Se recorre en profundidad y cada vertice se agrega a la
# secuencia cuando termina de procesarse; al final se invierte el resultado.
# El ciclo se detecta si durante el recorrido se vuelve a pisar un vertice
# que todavia esta "en proceso".
#
# Formato del archivo: una arista por linea, "origen,destino".

import sys

NO_VISITADO = 0
EN_PROCESO = 1
TERMINADO = 2


class Grafo:
    """Grafo dirigido con listas de adyacencia."""

    def __init__(self):
        self.adyacentes = {}
        self.vertices = []

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


def dfs(grafo, v, estado, secuencia):
    """Devuelve True si encuentra un ciclo."""
    estado[v] = EN_PROCESO

    for sucesor in grafo.adyacentes[v]:
        if estado[sucesor] == EN_PROCESO:
            return True                      # arista hacia atras -> ciclo
        if estado[sucesor] == NO_VISITADO:
            if dfs(grafo, sucesor, estado, secuencia):
                return True

    estado[v] = TERMINADO
    secuencia.append(v)                      # se agrega al terminar
    return False


def sort_topologico(grafo):
    """Devuelve (secuencia, hay_ciclo)."""
    estado = {}
    for v in grafo.vertices:
        estado[v] = NO_VISITADO

    secuencia = []
    for v in grafo.vertices:
        if estado[v] == NO_VISITADO:
            if dfs(grafo, v, estado, secuencia):
                return [], True

    secuencia.reverse()                      # el orden sale al reves
    return secuencia, False


if __name__ == "__main__":
    archivo = sys.argv[1] if len(sys.argv) > 1 else "grafo.txt"

    grafo = leer_grafo(archivo)
    print("Vertices:", grafo.vertices)

    secuencia, hay_ciclo = sort_topologico(grafo)
    print()
    if hay_ciclo:
        print("No se puede calcular el sort topologico: el grafo es ciclico.")
    else:
        print("Secuencia topologica:", " ".join(secuencia))
