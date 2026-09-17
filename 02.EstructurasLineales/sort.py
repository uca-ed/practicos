from collections import deque

#defino grafo, ejemplo sin ciclos
vertices = ["B", "D", "C", "A", "E"]
adyacencia = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["E"],
    "E": []
}

# Inicializo en cero la vecindad izquierda L(x) de cada nodo
grado = {}
for nodo in vertices:
    grado[nodo] = 0

# Busco L(x) de cada nodo (y el inicial)
for nodo in vertices:
    arr = adyacencia.get(nodo, [])
    for conexiones in arr:
        grado[conexiones] += 1

# Agrego a una cola todos los nodos iniciales
cola = deque()
for nodo in vertices:
    if grado[nodo] == 0:
        cola.append(nodo)

# Lista vacia para ordenar
orden = []

# Ordeno. Primero arranco con los nodos que tenian grado 0.
# Luego recorro los vecinos de cada uno de esos, si al grado
# del vecino le resto 1 y llega a cero, quiere decir que 
# es el siguiente, se agrega a la cola y de la cola a la
# lista orden.
while len(cola) > 0:
    nodo_actual = cola.popleft()
    orden.append(nodo_actual)

    vecinos = adyacencia.get(nodo_actual, [])
    for vecino in vecinos:
        grado[vecino] -= 1
        if grado[vecino] == 0:
            cola.append(vecino)

# Verifico
if len(orden) == len(vertices):
    print(orden)
else:
    print("Hay un ciclo.")