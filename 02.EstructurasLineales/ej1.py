cola = []

archivo = open("operaciones_cola.txt", "r")

for linea in archivo:
    partes = linea.strip().split(",")
    operacion = partes[0]

    if operacion == "ENQUEUE":
        valor = int(partes[1])
        cola.append(valor)

    elif operacion == "DEQUEUE":
        if len(cola) > 0:
            # desplazamos los elementos para sacar el del frente
            for i in range(len(cola) - 1):
                cola[i] = cola[i + 1]
            del cola[len(cola) - 1]

archivo.close()

print("Cola final:", cola)
