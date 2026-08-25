import json
 
 
def leer_grafo(nombre_archivo):
    f = open(nombre_archivo)
    estructura = json.load(f)
    f.close()
    return estructura['P'], estructura['E']
 
 
def armar_vecinos(nodos, relaciones):
    # diccionario nodo -> set de vecinos, para poder consultar rapido
    vecinos = {}
    for nodo in nodos:
        vecinos[nodo] = set(relaciones.get(nodo, []))
    return vecinos
 
 
def armar_mascaras(nodos, vecinos):
    # cada nodo se representa como un entero donde el bit i esta prendido
    # si hay relacion con el nodo que ocupa la posicion i
    indice = {}
    for i, nodo in enumerate(nodos):
        indice[nodo] = i
 
    mascaras = {}
    for nodo in nodos:
        m = 0
        for vecino in vecinos[nodo]:
            if vecino in indice:
                m |= (1 << indice[vecino])
        mascaras[nodo] = m
 
    return mascaras
 
 
def es_reflexiva(nodos, vecinos):
    for nodo in nodos:
        if nodo not in vecinos[nodo]:
            return False
    return True
 
 
def es_simetrica(nodos, vecinos):
    for a in nodos:
        for b in vecinos[a]:
            if a not in vecinos.get(b, ()):
                return False
    return True
 
 
def es_antisimetrica(nodos, vecinos):
    for a in nodos:
        for b in vecinos[a]:
            if a != b and a in vecinos.get(b, ()):
                return False
    return True
 
 
def es_transitiva(nodos, vecinos, mascaras):
    todos = (1 << len(nodos)) - 1
 
    for a in nodos:
        mascara_a = mascaras[a]
        for b in vecinos[a]:
            mascara_b = mascaras[b]
            # si b tiene algun vecino que a no tiene, no es transitiva
            # ~mascara_a invierte los bits de a (donde a no tiene vecino, queda un 1)
            # mascara_b & ~mascara_a deja prendidos solo los bits de vecinos de b que a no tiene
            if (mascara_b & ~mascara_a) & todos != 0:
                return False
    return True
 
 
def clasificar(reflexiva, simetrica, antisimetrica, transitiva):
    if reflexiva and antisimetrica and transitiva:
        return "orden"
    if reflexiva and simetrica and transitiva:
        return "equivalencia"
    return "ninguna de las dos"
 
 
def main():
    archivo = input("Archivo del grafo: ")
    nodos, relaciones = leer_grafo(archivo)
 
    vecinos = armar_vecinos(nodos, relaciones)
    mascaras = armar_mascaras(nodos, vecinos)
 
    reflexiva = es_reflexiva(nodos, vecinos)
    simetrica = es_simetrica(nodos, vecinos)
    antisimetrica = es_antisimetrica(nodos, vecinos)
    transitiva = es_transitiva(nodos, vecinos, mascaras)
 
    print("Reflexividad:", reflexiva)
    print("Simetria:", simetrica)
    print("Antisimetria:", antisimetrica)
    print("Transitividad:", transitiva)
    print("El grafo corresponde a una relacion de:", clasificar(reflexiva, simetrica, antisimetrica, transitiva))
 
 
if __name__ == "__main__":
    main()