def enqueue(cola, estado, valor):
    if (estado[1]<len(cola)):
        cola[(estado[0]+estado[1]) % len(cola)]= valor
        estado[1]= estado[1]+1
    else:
        print("Error: cola llena")

def dequeue(cola, estado):
    if (estado[1]>0):
        rta=cola[estado[0]]
        estado[0]=(estado[0]+1)%len(cola)
        estado[1]=estado[1]-1
        return rta
    else:
        print("Error: cola vacia")

def main():
    cola = [0, 0, 0, 0, 0]
    estado = [0, 0] # estado[0]= pos y estado[1]= long

    archivo = open("operaciones1.txt", "r")
    linea = archivo.readline()

    while linea != "":
        datos = linea.strip().split(",")
        if datos[0] == "ENQUEUE":
            valor = int(datos[1])
            enqueue(cola, estado, valor)
        elif datos[0] == "DEQUEUE":
            dequeue(cola, estado)
        linea = archivo.readline()
    archivo.close()

    print("Cola:")
    for i in range(estado[1]):
        posicion = (estado[0] + i) % len(cola)
        print(cola[posicion])

main()
