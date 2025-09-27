class Cola:
    def __init__(self, largo):
        self.arr = [None] * largo
        self.front = 0
        self.rear = -1
        self.size = 0
        self.max = largo

    def queue(self, valor):
        if self.size+1 >= self.max:
            print("Cola llena!")
        else:
            self.rear = (self.rear + 1) % self.max
            self.arr[self.rear] = valor
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Cola vacía!")
        else:
            valor = self.arr[self.front]
            self.arr[self.front] = None
            self.front = (self.front + 1) % self.max
            self.size -= 1
            return valor
        
    def imprimir(self):
        for k in self.arr:
            print(k)


def leerInstrucciones():
    instrucciones = []
    archivo = open('colas.txt','r')
    for linea in archivo:
        linea = linea.strip().rstrip(",")
        if not linea:
            continue

        partes = linea.split()
        if partes[0] == "QUEUE":
            instrucciones.append(("QUEUE", int(partes[1])))
        elif partes[0] == "DEQUEUE":
            instrucciones.append(("DEQUEUE", None))
        else:
            print(f"Instrucción desconocida: {linea}")
    
    archivo.close()
    return instrucciones

def ejecutarInstrucciones(cola, instrucciones):
    for i in instrucciones:
        if i[0] == "QUEUE":
            cola.queue(i[1])
        elif i[0] == "DEQUEUE":
            cola.dequeue()


instrucciones = leerInstrucciones()
cola = Cola(5)
ejecutarInstrucciones(cola,instrucciones)
cola.imprimir()