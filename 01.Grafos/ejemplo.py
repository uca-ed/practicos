import json

f = open('01.json')
estructura = json.load(f)
f.close()
nodos = estructura['P']
arcos = estructura['E']

# c. Vecindad derecha de un nodo a
a = '7'  
vecindad_derecha_a = arcos[a]
print("Vecindad derecha de", a, ":", vecindad_derecha_a)

vecindad_izq = {}
for nodo in nodos:
    vecindad_izq[nodo] = []
for origen in arcos:
    for destino in arcos[origen]:
        vecindad_izq[destino].append(origen)

# d. Vecindad izquierda de a 
print("Vecindad izquierda de", a, ":", vecindad_izq[a])

# a. Minimales del grafo
minimales = []
for nodo in nodos:
    otros = []
    for origen in vecindad_izq[nodo]:
        if origen != nodo:
            otros.append(origen)
    if otros == []:
        minimales.append(nodo)
print("Minimales del grafo:", minimales)

# b. Maximales del grafo
maximales = []
for nodo in nodos:
    otros = []
    for destino in arcos[nodo]:
        if destino != nodo:
            otros.append(destino)
    if otros == []:
        maximales.append(nodo)
print("Maximales del grafo:", maximales)