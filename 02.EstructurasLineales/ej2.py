pila = []

archivo = open("operaciones_pila.txt", "r")

for linea in archivo:
    partes = linea.strip().split(",")
    operacion = partes[0]

    if operacion == "PUSH":
        valor = int(partes[1])
        pila.append(valor)

    elif operacion == "POP":
        if len(pila) > 0:
            # el ultimo elemento es el tope de la pila
            del pila[len(pila) - 1]

archivo.close()

print("Pila final:", pila)
