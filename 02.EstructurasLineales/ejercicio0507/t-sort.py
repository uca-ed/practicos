import json 

def leerGrafo(name):

    with open(name, "r") as archivo:
        datos = json.load(archivo)
    return datos['P'], datos['E']


def t_sort(nodos, arcos):

    gradoEntrada = {}

    for nodo in nodos:
        gradoEntrada[nodo]=0

    for origen in arcos:
        for destino in arcos[origen]:
            gradoEntrada[destino]+=1

    cola = []

    for nodo in nodos:
        if gradoEntrada[nodo] == 0:
            cola.append(nodo)

    resultado = []

    while len(cola) > 0:
        nodo = cola.pop(0)
        resultado.append(nodo)

        for destino in arcos.get(nodo, []):
            gradoEntrada[destino] -= 1

            if gradoEntrada[destino] == 0:
                cola.append(destino)

    if len(resultado) == len(nodos):
        print('Secuencia T-sort')
        print(resultado)

    else:
        print('La estructura es ciclica')
        print('no se puede calcular T-Sort')

def main():
    
    nodos, arcos = leerGrafo('grafo.json')
    t_sort(nodos, arcos)

main()
