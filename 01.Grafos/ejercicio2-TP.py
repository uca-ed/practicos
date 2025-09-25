import json


f = open('nombreArchivo.json')
estructura = json.load(f)
grafo = estructura['E']
f.close()


def es_reflexivo(grafo):
    for nodo in grafo:
        if nodo in grafo[nodo]:
            pass
        else:
            return False
    return True


def es_simetrico(grafo):
    for nodo in grafo:
        for vecino in grafo[nodo]:
            if vecino in grafo:
                if nodo in grafo[vecino]:
                    pass
                else:
                    return False
            else:
                return False
    return True


def es_antisimetrico(grafo):
    for nodo in grafo:
        for vecino in grafo[nodo]:
            if nodo != vecino:
                if vecino in grafo:
                    if nodo in grafo[vecino]:
                        return False
    return True


def es_transitivo(grafo):
    for a in grafo:
        for b in grafo[a]:
            if b in grafo:
                for c in grafo[b]:
                    if c not in grafo[a]:
                        return False
    return True


print("Nodos: ")
for i in grafo:
    print(i)

print("\nPropiedades del grafo:")
reflexivo = es_reflexivo(grafo)
simetrico = es_simetrico(grafo)
antisimetrico = es_antisimetrico(grafo)
transitivo = es_transitivo(grafo)

print("Reflexivo:", reflexivo)
print("Simétrico:", simetrico)
print("Antisimétrico:", antisimetrico)
print("Transitivo:", transitivo)

if reflexivo == True and simetrico == True and transitivo == True:
    print("\nEl grafo representa una relación de equivalencia.")
elif reflexivo == True and antisimetrico == True and transitivo == True:
    print("\nEl grafo representa una relación de orden.")
else:
    print("\nEl grafo no representa ni una relación de equivalencia ni de orden.")
