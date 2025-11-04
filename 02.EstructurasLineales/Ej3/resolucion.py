"""
3. Representar listas por medio de celdas con enlace simple.  
"""


def crear_nodo(valor):
    return {"dato": valor, "siguiente": None}

def insertar(lista, valor):
    nuevo = crear_nodo(valor)
    if lista["cabeza"] is None:
        lista["cabeza"] = nuevo
    else:
        actual = lista["cabeza"]
        while actual["siguiente"] is not None:
            actual = actual["siguiente"]
        actual["siguiente"] = nuevo

def eliminar(lista, valor):
    actual = lista["cabeza"]
    anterior = None

    while actual is not None and actual["dato"] != valor:
        anterior = actual
        actual = actual["siguiente"]

    if actual is None:
        return

    if anterior is None:
        lista["cabeza"] = actual["siguiente"]
    else:
        anterior["siguiente"] = actual["siguiente"]

def ejecutar_operaciones_lista():
    lista = {"cabeza": None}
    archivo = open("EstructuraDeDatos\\ED-Practica-ed-2025-2c\\02.EstructurasLineales\\Ej3\\operaciones.txt", "r")

    for linea in archivo:
        partes = linea.split()
        operacion = partes[0]

        if operacion == "INSERTAR":
            valor = int(partes[1])
            insertar(lista, valor)

        elif operacion == "ELIMINAR":
            valor = int(partes[1])
            eliminar(lista, valor)

    archivo.close()

    actual = lista["cabeza"]
    resultado = []
    while actual is not None:
        resultado.append(actual["dato"])
        actual = actual["siguiente"]

    print(resultado)

ejecutar_operaciones_lista()
