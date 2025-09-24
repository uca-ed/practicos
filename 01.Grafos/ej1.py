import json

f = open('archivos_ej1/01.json')
estructura = json.load(f)

nodos = estructura['P']
aristas = estructura['E']

def minimales():
    """Nodos sin predecesores"""
    minimales = []
    for nodo in nodos:
        tiene_predecesor = any(nodo in aristas[otro] for otro in aristas)
        if not tiene_predecesor:
            minimales.append(nodo)
    return minimales


def maximales():
    """Nodos sin sucesores"""
    maximales = []
    for nodo in nodos:
        if nodo not in aristas or len(aristas[nodo]) == 0:
            maximales.append(nodo)
    return maximales


def vecindad_derecha(nodo):
    """Nodos alcanzables directamente desde 'nodo'"""
    return aristas.get(nodo, [])


def vecindad_izquierda(nodo):
    """Nodos que llegan directamente a 'nodo'"""
    izquierda = []
    for origen, destinos in aristas.items():
        if nodo in destinos:
            izquierda.append(origen)
    return izquierda



print("Minimales:", minimales()[:20])  
print("Maximales:", maximales()[:20])
print("Vecindad derecha de '1':", vecindad_derecha("1")[:20])
print("Vecindad izquierda de '10':", vecindad_izquierda("10")[:20])

f.close()
