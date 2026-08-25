import json

def cargar_nodos(nombre_arch):
    archivo = open(nombre_arch,"r")
    datos = json.load(archivo)
    archivo.close()

    nodos = datos["P"]
    return nodos

def cargar_arcos(nombre_arch):
    archivo = open(nombre_arch,"r")
    datos = json.load(archivo)
    archivo.close()

    arcos = datos["E"]
    return arcos

def es_reflexiva(nodos,arcos):
    for x in nodos:
        if x not in arcos:
            return False
        if x not in arcos[x]:
            return False
    return True

def es_simetrica(arcos):
    for u in arcos:
        for v in arcos[u]:
            if v not in arcos:
                return False
            if u not in arcos[v]:
                return False
    return True

def es_antisimetrica(arcos):
    for u in arcos:
        for v in arcos[u]:
            if u != v:
                if v in arcos and u in arcos[v]:
                    return False
    return True

def es_transitiva(arcos):
    for u in arcos:
        for v in arcos[u]:
            if v in arcos:
                for w in arcos[v]:
                    if w not in arcos[u]:
                        return False
    return True

def analizar_grafos(nombre_arch):
    nodos = cargar_nodos(nombre_arch)
    arcos = cargar_arcos(nombre_arch)

    print("Archivo: ", nombre_arch)
    print()
    
    if es_reflexiva(nodos,arcos):
        print("Grafo es reflexivo")
    else:
        print("Grafo no es reflexivo")

    if es_simetrica(arcos):
        print("Grafo es simetrico")
    else:
        print("Grafo no es simetrico")

    if es_antisimetrica(arcos):
        print("Grafo es antisimetrico")
    else:
        print("Grafo no es antisimetrico")

    if es_transitiva(arcos):
        print("Grafo es transtiva")
    else:
        print("Grafo no es transitiva")

    print()

    if es_reflexiva(nodos,arcos) and es_simetrica(arcos) and es_transitiva(arcos):
        print("Es una relacion de equivalencia")
    elif es_reflexiva(nodos,arcos) and es_antisimetrica(arcos) and es_transitiva(arcos):
        print("Es una relacion de orden")
    else:
        print("No es una relacion ni de equivalencia ni de orden")

    print()


def main():
    analizar_grafos("01.json")
    analizar_grafos("02.json")
    analizar_grafos("03.json")
main()

