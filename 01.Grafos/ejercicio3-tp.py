import json


f = open('nombreArchivo.json')
estructura = json.load(f)
grafo = estructura['E']
f.close()

print("Nodos: ")
for i in grafo:
    print(i)


def buscar_camino(origen, destino, visitados=None):
    if visitados == None:
        visitados = []
    visitados.append(origen)
    if origen == destino:
        return visitados
    if origen in grafo:
        for vecino in grafo[origen]:
            if vecino not in visitados:
                resultado = buscar_camino(vecino, destino, visitados.copy())
                if resultado != None:
                    return resultado
    return None


inicio = input("Nodo de inicio: ")
fin = input("Nodo de destino: ")
camino = buscar_camino(inicio, fin)

if camino != None:
    print("Camino encontrado:", " -> ".join(camino))
else:
    print("No hay camino entre los nodos indicados.")
