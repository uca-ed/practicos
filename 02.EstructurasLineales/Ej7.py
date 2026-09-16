from collections import *
import json
f=open("Arch_Grafo.json")
estructura = json.load(f)
Aristas = estructura["aristas"]
Nodos = estructura["nodos"]
grafo = {nodo: [] for nodo in Nodos}
grado_entrada = {nodo: 0 for nodo in Nodos}
for a in Aristas:
    origen = a["nombre"]
    destino = a["correlativa"]
    grafo[origen].append(destino)
    grado_entrada[destino] += 1
G = deque([nodo for nodo in Nodos if grado_entrada[nodo] == 0])
orden_topologico = []
while G:
    actual = G.popleft()
    orden_topologico.append(actual)
    for vecino in grafo[actual]:
        grado_entrada[vecino] -= 1
        if grado_entrada[vecino] == 0:
            G.append(vecino)
if len(orden_topologico) == len(Nodos):
    for materia in orden_topologico:
        print(materia)

f.close()