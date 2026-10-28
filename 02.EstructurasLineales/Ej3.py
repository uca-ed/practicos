def crearCelda(valor):
    return {
        "info": valor,
        "sig": None}
def iniciarLista():
    return {
        "cabeza": None}

def agregarValor(lista, valor):
    nueva_celda = crearCelda(valor)
    if lista["cabeza"] is None:
        lista["cabeza"] = nueva_celda
    else:
        actual = lista["cabeza"]
        while actual["sig"] is not None:
            actual = actual["sig"]
        actual["sig"] = nueva_celda

def eliminarValor(lista, valor):
    if lista["cabeza"] is None:
        return "[ERROR] La lista está vacía"
    if lista["cabeza"]["info"] == valor:
        lista["cabeza"] = lista["cabeza"]["sig"]
        return
    actual = lista["cabeza"]
    while actual["sig"] is not None:
        if actual["sig"]["info"] == valor:
            actual["sig"] = actual["sig"]["sig"]
            return
        actual = actual["sig"]
    return "[ERROR] Valor no encontrado"

def contieneValor(lista,valor):
    actual=lista["cabeza"]
    while actual is not None:
        if actual["info"] == valor:
            return True
        actual = actual["sig"]
    return False

def imprimirLista(lista):
    actual=lista["cabeza"]
    posicion=1
    while actual is not None:
        print("\nValor: "+actual["info"]+" Posicion: "+str(posicion))
        posicion+=1
        actual=actual["sig"]


# --- prueba del codigo ---


mi_lista = iniciarLista()
imprimirLista(mi_lista)

print("=== Agrego A B C D en ese orden ===")
agregarValor(mi_lista, "A")
agregarValor(mi_lista, "B")
agregarValor(mi_lista, "C")
agregarValor(mi_lista, "D")
imprimirLista(mi_lista)

print("\n=== Búsquedas ===")
print("¿Contiene 'B'?:", contieneValor(mi_lista, "B"))
print("¿Contiene 'Z'?:", contieneValor(mi_lista, "Z"))

print("\n=== Eliminar ('B') ===")
eliminarValor(mi_lista, "B")
imprimirLista(mi_lista)

print("\n=== Eliminar la cabeza ('A') ===")
eliminarValor(mi_lista, "A")
imprimirLista(mi_lista)

print("\n=== Eliminar el final ('D') ===")
eliminarValor(mi_lista, "D")
imprimirLista(mi_lista)
