"""1. Representar colas sobre un arreglo. 
El algoritmo debe leer el archivo de operaciones sobre colas y operar, partiendo de una cola vacía. 
Se debe mostrar el resultado final. """

class ColaSobreArreglo:
    def __init__(self,tam):
        self.tam=tam
        self.data=[None]*tam
        self.front=0
        self.rear=-1
    
    def estaVacia(self):
        return self.data[self.front] == None 
    
    def estaFull(self):
        return (self.data[self.front] != None and (self.rear + 1)%self.tam == self.front)
    
    def enqueue(self,ele):
        if(self.estaFull()):
            print("Error, arreglo full")
        else:
            self.rear = (self.rear + 1)%self.tam
            self.data[self.rear] = ele
            print("enqueue: "+ str(ele))

    def dequeue(self):
        if(self.estaVacia()):
            print("Error, arreglo vacío")
        else:
            rta = self.data[self.front]
            self.data[self.front]=None
            self.front = (self.front + 1)%self.tam
            print("dequeue "+ str(rta))
            return rta

    def imprimir(self):
        if(self.estaVacia()==False):
            ini=self.front
            for i in range(self.tam):
                ele=self.data[ini]
                if ele != None:
                    print(ele)
                    ini = (ini+1)%self.tam
                    if self.data[ini]==None:
                        break
                   
        else:
            print("Cola vacía")


def ejecutarDesdeArch(ruta):
    capacity = 10
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = []
        for l in f:
            l = l.strip()
            if l:
                lineas.append(l)

    cola = ColaSobreArreglo(capacity)
    
    for ele in lineas:
        partes = ele.split()
        op = partes[0]

        if op == "ENQUEUE":
            cola.enqueue(int(partes[1]))

        elif op == "DEQUEUE":
            cola.dequeue()

    cola.imprimir()

ejecutarDesdeArch("02.EstructurasLineales/operacionesColas.txt")
