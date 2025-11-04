"""
2. Representar pilas sobre un arreglo.
El algoritmo debe leer el archivo de operaciones sobre pilas y operar, partiendo de una pila vacía.
Se debe mostrar el resultado final.
"""

def crear_pila(capacidad):
    return {
        "datos": [None] * capacidad,
        "tope": -1,
        "capacidad": capacidad
    }

def apilar(pila, valor):
    if pila["tope"] < pila["capacidad"] - 1:
        pila["tope"] += 1
        pila["datos"][pila["tope"]] = valor

def desapilar(pila):
    if pila["tope"] >= 0:
        pila["tope"] -= 1

def ejecutar_operaciones_pila():
    pila = crear_pila(20)
    archivo = open("EstructuraDeDatos\\ED-Practica-ed-2025-2c\\02.EstructurasLineales\\Ej2\\operaciones.txt", "r")
    
    for linea in archivo:
        partes = linea.split()
        operacion = partes[0]
        
        if operacion == "APILAR":
            valor = int(partes[1])
            apilar(pila, valor)
        elif operacion == "DESAPILAR":
            desapilar(pila)
    
    archivo.close()

    resultado = pila["datos"][:pila["tope"] + 1]
    print(resultado)

ejecutar_operaciones_pila()
