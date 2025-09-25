import json

def lecturaJson():
    f = open('nombreArchivo.json')
    estructura = json.load(f)
    grafo = estructura['E']
    print("Nodos: ")
    for i in grafo:
        print(i)

    f.close()


def es_reflexivo(grafo):
    for nodo in grafo:
        if nodo not in grafo[nodo]:
            return False
    return True

def es_simetrico(grafo):
    for nodo in grafo:
        for vecino in grafo[nodo]:
            if nodo not in grafo.get(vecino, []):
                return False
    return True

def es_antisimetrico(grafo):
    for nodo in grafo:
        for vecino in grafo[nodo]:
            if nodo != vecino and nodo in grafo.get(vecino, []):
                return False
    return True

def es_transitivo(grafo):
    for a in grafo:
        for b in grafo[a]:
            for c in grafo.get(b, []):
                if c not in grafo[a]:
                    return False
    return True


def main():
    lecturaJson()
    ("\nPropiedades del grafo:")
    reflexivo = es_reflexivo(grafo)
    simetrico = es_simetrico(grafo)
    antisimetrico = es_antisimetrico(grafo)
    transitivo = es_transitivo(grafo)

    print("Reflexivo:", reflexivo)
    print("Simétrico:", simetrico)
    print("Antisimétrico:", antisimetrico)
    print("Transitivo:", transitivo)

    if reflexivo and simetrico and transitivo:
        print("\nEl grafo representa una relación de equivalencia.")
    elif reflexivo and antisimetrico and transitivo:
        print("\nEl grafo representa una relación de orden.")
    else:
        print("\nEl grafo no representa ni una relación de equivalencia ni de orden.")

main()
