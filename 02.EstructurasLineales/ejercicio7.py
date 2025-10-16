#7) Sort Topologico
from collections import defaultdict, deque #diccionariopara representar grafos, donde cada nodo tiene una lista de vecinos (los nodos a los que apunta)

def cargar_grafo(nombre_archivo):
    grafo=defaultdict(list)
    with open(nombre_archivo, "r") as f:
        for linea in f:
            origen, destino=linea.strip().split()
            grafo[origen].append(destino)
    return grafo
def sort_topologico(grafo):
    grado_entrada=defaultdict(int) #creamos un dic donde cada clave nueva empieza con valor 0
    todos= set(grafo.keys())
    for v in grafo:
        for dest in grafo[v]:
            grado_entrada[dest]+=1  #se guaedan cuantas flechas entran a cada nodo
            todos.add(dest)
    cola = deque() #se eligen nodos con grados de entrada 0 (los que no dependen de nadie), para saber por donde arranca la cola
    for v in grafo:
        if grado_entrada[v] == 0:
            cola.append(v)
    orden=[]
    while cola: #aca procesamos los nodos en orden y actualizamos dependencias
        v=cola.popleft()
        orden.append(v)
        for dest in grafo[v]:
            grado_entrada[dest]-=1
            if grado_entrada[dest]== 0:
                cola.append(dest)
    return orden 
# Prueba:
grafo = cargar_grafo("grafo.txt")
orden = sort_topologico(grafo)
print("\n--- Orden Topológico ---")
print(" -> ".join(orden))
