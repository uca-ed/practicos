MAX = 100

cola = [0] * MAX

frente = 0
fin = 0

archivo = open("operaciones.txt", "r")

for linea in archivo:
    partes = linea.strip().split(",")

    operacion = partes[0]

    if operacion == "ENQUEUE":
        valor = int(partes[1])
        cola[fin] = valor
        fin += 1

    elif operacion == "DEQUEUE":
        if frente < fin:
            frente += 1

archivo.close()

print("Cola final:")

for i in range(frente, fin):
    print(cola[i], end=" ")

print()




pila = [0] * MAX
tope = 0

archivo = open("operaciones2.txt", "r")

for linea in archivo:
    partes = linea.strip().split(",")

    operacion = partes[0]

    if operacion == "PUSH":
        valor = int(partes[1])
        pila[tope] = valor
        tope += 1

    elif operacion == "POP":
        if tope > 0:
            tope -= 1

archivo.close()

print("Pila final:")

for i in range(tope):
    print(pila[i], end=" ")

print()