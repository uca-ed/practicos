def push(pila, estado, valor):
    if (estado[0] < len(pila) - 1):
        estado[0] = estado[0] + 1
        pila[estado[0]] = valor
    else:
        print("Error: pila llena")


def pop(pila, estado):
    if (estado[0] > -1):
        estado[1] = pila[estado[0]]
        estado[0] = estado[0] - 1
    else:
        print("Error: pila vacia")


def main():
    pila = [0, 0, 0, 0, 0]
    estado = [-1, 0] # -1 es top y el 0 es el valor que devulve el pop

    archivo = open("operaciones2.txt", "r")
    linea = archivo.readline()

    while linea != "":
        datos = linea.strip().split(",")

        if datos[0] == "PUSH":
            valor = int(datos[1])
            push(pila, estado, valor)

        elif datos[0] == "POP":
            pop(pila, estado)

        linea = archivo.readline()

    archivo.close()

    print("Pila final:")

    for i in range(estado[0] + 1):
        print(pila[i])

main()