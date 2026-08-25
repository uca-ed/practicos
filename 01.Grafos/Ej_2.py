import json

f = open('02.json')
estructura = json.load(f)
f.close()
nodos = estructura['P']
arcos = estructura['E']

arcos_set = {}
for origen in arcos:
    arcos_set[origen] = set(arcos[origen])

def hay_arco(a, b):
    return b in arcos_set[a]

def es_reflexivo(nodos):
    for n in nodos:
        if not hay_arco(n, n):
            return False
    return True

def es_simetrico(arcos_set):
    for a in arcos_set:
        for b in arcos_set[a]:
            if not hay_arco(b, a):
                return False
    return True

def es_antisimetrico(arcos_set):
    for a in arcos_set:
        for b in arcos_set[a]:
            if a != b and hay_arco(b, a):
                return False
    return True

def es_transitivo(arcos_set):
    for a in arcos_set:
        for b in arcos_set[a]:
            for c in arcos_set[b]:
                if not hay_arco(a, c):
                    return False
    return True

reflexivo = es_reflexivo(nodos)
simetrico = es_simetrico(arcos_set)
antisimetrico = es_antisimetrico(arcos_set)
transitivo = es_transitivo(arcos_set)

print("Reflexivo:", reflexivo)
print("Simétrico:", simetrico)
print("Antisimétrico:", antisimetrico)
print("Transitivo:", transitivo)

if reflexivo and antisimetrico and transitivo:
    print("El grafo es un ORDEN")
elif reflexivo and simetrico and transitivo:
    print("El grafo es una RELACIÓN DE EQUIVALENCIA")
else:
    print("El grafo no es ni orden ni relación de equivalencia")

