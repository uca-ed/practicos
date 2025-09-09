"""2. Representar pilas sobre un arreglo. 
El algoritmo debe leer el archivo de operaciones sobre pilas y operar, partiendo de una pila vacía. 
Se debe mostrar el resultado final.  """


class PilaSobreArreglo:
    def __init__(self,tam):
        self.tam=tam
        self.data=[None]*tam
        self.TOS=-1
    
    def estaVacia(self):
        return self.TOS == -1
    
    def estaFull(self):
        return self.TOS == self.tam - 1
    
    def push(self,ele):
        if(self.estaFull()):
            print("Error, arreglo full")
        else:
            self.data[self.TOS + 1] = ele
            self.TOS += 1

    def pop(self):
        if(self.estaVacia()):
            print("Error, arreglo vacío")
        else:
            rta = self.data[self.TOS]
            self.data[self.TOS]=None
            self.TOS -= 1
            return rta

    def imprimir(self):
        if(self.estaVacia()==False):
            for ele in self.data[:self.TOS+1]:
                    print(ele)


def ejecutarDesdeArch(ruta):
    capacity = 10
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = []
        for l in f:
            l = l.strip()
            if l:
                lineas.append(l)

    pila = PilaSobreArreglo(capacity)
    
    for ele in lineas:
        partes = ele.split()
        op = partes[0]

        if op == "PUSH":
            pila.push(int(partes[1]))

        elif op == "POP":
            pila.pop()

    pila.imprimir()

ejecutarDesdeArch("02.EstructurasLineales/operacionesPilas.txt")
