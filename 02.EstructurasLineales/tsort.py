import json
from collections import deque

with open("grafo_prueba2.json", "r") as f:
    data = json.load(f)

vertices = data["P"]
adyacencia = data["E"]

#incializo en cero la vecindad izquierda L(x) de cada nodo
grado = {}
for nodo in vertices:
    grado[nodo] = 0

#busco L(x) de cada nodo (y el inicial)
for nodo in vertices:
    arr = adyacencia.get(nodo, [])
    for conexiones in arr:
        grado[conexiones] += 1

#agrego a una cola todos los nodos iniciales
cola = deque()
for nodo in vertices:
    if grado[nodo] == 0:
        cola.append(nodo)

#lista vacía para ordenar
orden = []

#ordeno. Primero arranco con los nodos que tenían grado 0.
#luego recorro los vecinos de cada uno de esos, si al grado
#del vecino le resto 1 y llega a cero, quiere decir que 
#es el siguiente, se agrega a la cola y de la cola a la
#lista orden.

while len(cola) > 0:
    nodo_actual = cola.popleft()
    orden.append(nodo_actual)

    vecinos = adyacencia.get(nodo_actual, [])
    for vecino in vecinos:
        grado[vecino] -= 1
        if grado[vecino] == 0:
            cola.append(vecino)

#verifico
if len(orden) == len(vertices):
    print(orden)
else:
    print("Hay un ciclo.")


    


