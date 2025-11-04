"""
1. Representar colas sobre un arreglo.
El algoritmo debe leer el archivo de operaciones sobre colas y operar, partiendo de una cola vacía.
Se debe mostrar el resultado final.  
"""

def crear_cola(capacidad):
    return {
        "datos": [None] * capacidad,
        "inicio": 0,
        "fin": 0,
        "cantidad": 0,
        "capacidad": capacidad
    }

def encolar(cola, valor):
    if cola["cantidad"] < cola["capacidad"]:
        cola["datos"][cola["fin"]] = valor
        cola["fin"] = (cola["fin"] + 1) % cola["capacidad"]
        cola["cantidad"] += 1

def desencolar(cola):
    if cola["cantidad"] > 0:
        cola["inicio"] = (cola["inicio"] + 1) % cola["capacidad"]
        cola["cantidad"] -= 1

def ejecutar_operaciones():
    cola = crear_cola(20)
    archivo = open("EstructuraDeDatos\\ED-Practica-ed-2025-2c\\02.EstructurasLineales\\Ej1\\operaciones.txt", "r")
    for linea in archivo:
        partes = linea.split()
        operacion = partes[0]
        if operacion == "ENCOLAR":
            valor = int(partes[1])
            encolar(cola, valor)
        elif operacion == "DESENCOLAR":
            desencolar(cola)
    archivo.close()
    valores = []
    indice = cola["inicio"]
    for _ in range(cola["cantidad"]):
        valores.append(cola["datos"][indice])
        indice = (indice + 1) % cola["capacidad"]
    print(valores)

ejecutar_operaciones()
