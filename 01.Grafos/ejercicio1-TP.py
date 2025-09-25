import json

f = open('archivos_ej1/01.json')
estructura = json.load(f)

nodos = estructura['P']
aristas = estructura['E']


def buscar_minimales():
    lista_minimales = []
    for n in nodos:
        tiene = False
        for otro in aristas:
            if n in aristas[otro]:
                tiene = True
        if tiene == False:
            lista_minimales.append(n)
    return lista_minimales



def buscar_maximales():
    lista_maximales = []
    for n in nodos:
        if n in aristas:
            if len(aristas[n]) == 0:
                lista_maximales.append(n)
        else:
            lista_maximales.append(n)
    return lista_maximales



def vecinos_derecha(n):
    if n in aristas:
        return aristas[n]
    else:
        return []



def vecinos_izquierda(n):
    lista = []
    for origen in aristas:
        destinos = aristas[origen]
        for d in destinos:
            if d == n:
                lista.append(origen)
    return lista



print("Minimales:", buscar_minimales())
print("Maximales:", buscar_maximales())
print("Vecindad derecha de '1':", vecinos_derecha("1"))
print("Vecindad izquierda de '10':", vecinos_izquierda("10"))

f.close()
