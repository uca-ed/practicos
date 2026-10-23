
cabeza = None  
# inserto en el final
nueva = {"dato": 1, "siguiente": None}
if cabeza is None:
    cabeza = nueva
else:
    actual = cabeza
    while actual["siguiente"] is not None:
        actual = actual["siguiente"]
    actual["siguiente"] = nueva

nueva = {"dato": 2, "siguiente": None}
if cabeza is None:
    cabeza = nueva
else:
    actual = cabeza
    while actual["siguiente"] is not None:
        actual = actual["siguiente"]
    actual["siguiente"] = nueva

nueva = {"dato": 3, "siguiente": None}
if cabeza is None:
    cabeza = nueva
else:
    actual = cabeza
    while actual["siguiente"] is not None:
        actual = actual["siguiente"]
    actual["siguiente"] = nueva


# inserto en el inicio
nueva = {"dato": 0, "siguiente": cabeza}
cabeza = nueva

# mostrar lista
elementos = []
actual = cabeza
while actual is not None:
    elementos.append(str(actual["dato"]))
    actual = actual["siguiente"]
print("Lista:", " -> ".join(elementos) + " -> None")

# elimino un valor
valor_a_borrar = 2
if cabeza is not None:
    if cabeza["dato"] == valor_a_borrar:
        cabeza = cabeza["siguiente"]
    else:
        anterior = cabeza
        actual = cabeza["siguiente"]
        while actual is not None and actual["dato"] != valor_a_borrar:
            anterior = actual
            actual = actual["siguiente"]
        if actual is not None:
            anterior["siguiente"] = actual["siguiente"]

elementos = []
actual = cabeza
while actual is not None:
    elementos.append(str(actual["dato"]))
    actual = actual["siguiente"]
print("Después de eliminar 2:", " -> ".join(elementos) + " -> None")
