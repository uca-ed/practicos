def crear_nodo(valor):
    return {"valor": valor, "siguiente": None}

def insertar(lista, valor):
    nodo = crear_nodo(valor)
    if lista["cabeza"] is None:
        lista["cabeza"] = nodo
    else:
        actual = lista["cabeza"]
        while actual["siguiente"] is not None:
            actual = actual["siguiente"]
        actual["siguiente"] = nodo

def eliminar(lista):
    if lista["cabeza"] is None:
        return
    lista["cabeza"] = lista["cabeza"]["siguiente"]

def imprimir(lista):
    actual = lista["cabeza"]
    while actual is not None:
        print(actual["valor"], end=" -> ")
        actual = actual["siguiente"]
    print("None")


lista = {"cabeza": None}

insertar(lista, 1)
insertar(lista, 2)
insertar(lista, 3)
imprimir(lista)   
eliminar(lista)
imprimir(lista)   
