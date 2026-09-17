from collections import deque
import sys

from Grafo import Grafo


def leer_grafo(nombre_archivo):
	"""Lee un grafo dirigido desde un archivo.

	Cada línea debe contener ``origen destino`` para representar un arco.
	Una línea con un solo valor agrega un nodo aislado. Las líneas vacías y
	las que empiezan por ``#`` se ignoran.
	"""
	grafo = Grafo()

	with open(nombre_archivo, encoding="utf-8") as archivo:
		for numero_linea, linea in enumerate(archivo, start=1):
			datos = linea.split("#", 1)[0].split()
			if not datos:
				continue
			if len(datos) == 1:
				grafo.agregar_nodo(datos[0])
			elif len(datos) == 2:
				grafo.agregar_arco(datos[0], datos[1])
			else:
				raise ValueError(
					f"Línea {numero_linea}: se esperaban uno o dos nodos"
				)

	return grafo


def sort_topologico(grafo):
	"""Devuelve una ordenación topológica del grafo.

	Lanza ValueError si el grafo contiene un ciclo, porque en ese caso no
	existe una ordenación topológica.
	"""
	grados_entrada = {nodo: grafo.grado_entrada(nodo) for nodo in grafo.P}
	pendientes = deque(sorted(
		(nodo for nodo, grado in grados_entrada.items() if grado == 0),
		key=str,
	))
	orden = []

	while pendientes:
		nodo = pendientes.popleft()
		orden.append(nodo)

		for vecino in sorted(grafo.R(nodo), key=str):
			grados_entrada[vecino] -= 1
			if grados_entrada[vecino] == 0:
				pendientes.append(vecino)

	if len(orden) != len(grafo.P):
		raise ValueError("El grafo contiene un ciclo")

	return orden


def main():
	grafo = leer_grafo(sys.argv[1])
	
	try:
		print(" ".join(sort_topologico(grafo)))
	except ValueError as error:
		raise SystemExit(error) from error


if __name__ == "__main__":
	main()
