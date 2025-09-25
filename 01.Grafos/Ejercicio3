import json

def lecturaJson():
    f = open('nombreArchivo.json')
    estructura = json.load(f)
    grafo = estructura['E']
    print("Nodos: ")
    for i in grafo:
        print(i)

    f.close()

def buscar_camino(origen, destino, visitados=None):
    if visitados is None:
        visitados = []
    visitados.append(origen)
    if origen == destino:
        return visitados
    for vecino in grafo.get(origen, []):
        if vecino not in visitados:
            resultado = buscar_camino(vecino, destino, visitados.copy())
            if resultado:
                return resultado
    return None


def main():
    lecturaJson()
    inicio = input("Nodo de inicio: ")
    fin = input("Nodo de destino: ")
    camino = buscar_camino(inicio, fin)
    if camino:
        print("Camino encontrado:", " → ".join(camino))
    else:
        print("No hay camino entre los nodos indicados.")
main()
