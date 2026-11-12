import json


def leer_grafo(nombre_archivo):
    with open(nombre_archivo, encoding='utf-8') as archivo:
        estructura = json.load(archivo)

    return estructura


def vecindad_derecha(estructura, nodo):
    if nodo in estructura['E']:
        return estructura['E'][nodo]

    return []


def es_reflexiva(estructura):
    for x in estructura['P']:
        if x not in vecindad_derecha(estructura, x):
            return False

    return True


def es_simetrica(estructura):
    for x in estructura['P']:
        for y in vecindad_derecha(estructura, x):

            if x not in vecindad_derecha(estructura, y):
                return False

    return True


def es_antisimetrica(estructura):
    for x in estructura['P']:
        for y in vecindad_derecha(estructura, x):

            if x != y and x in vecindad_derecha(estructura, y):
                return False

    return True


def es_transitiva(estructura):
    for x in estructura['P']:

        for y in vecindad_derecha(estructura, x):

            for z in vecindad_derecha(estructura, y):

                if z not in vecindad_derecha(estructura, x):
                    return False

    return True


nombre_archivo = input("Ingrese el nombre del archivo JSON: ")

estructura = leer_grafo(nombre_archivo)

reflexiva = es_reflexiva(estructura)
simetrica = es_simetrica(estructura)
antisimetrica = es_antisimetrica(estructura)
transitiva = es_transitiva(estructura)

print()
print("Reflexiva:", reflexiva)
print("Simétrica:", simetrica)
print("Antisimétrica:", antisimetrica)
print("Transitiva:", transitiva)

print()

if reflexiva and antisimetrica and transitiva:
    print("La relación es un ORDEN PARCIAL")
else:
    print("La relación NO es un orden parcial")

if reflexiva and simetrica and transitiva:
    print("La relación es de EQUIVALENCIA")
else:
    print("La relación NO es de equivalencia")
