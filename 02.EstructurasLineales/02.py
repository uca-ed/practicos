class Pila:
    def __init__(self,largo):
        self.arr = [None]*largo
        self.tope = -1
        self.max = largo
        
    def push(self,valor):
        if self.tope+1 >= self.max:
            print("Pila llena!")
        else:
            self.tope += 1
            self.arr[self.tope] = valor
        
    def pop(self):
        if self.tope == -1:
            print("Pila vacia!")
        else:
            valor = self.arr[self.tope]
            self.arr[self.tope] = None
            self.tope -= 1
            return valor
        
    def imprimir(self):
        for k in self.arr:
            print(k)
        
def leerInstrucciones():
    instrucciones = []
    archivo = open('pilas.txt','r')
    for linea in archivo:
        linea = linea.strip().rstrip(",")
        if not linea:
            continue

        partes = linea.split()
        if partes[0] == "PUSH":
            instrucciones.append(("PUSH", int(partes[1])))
        elif partes[0] == "POP":
            instrucciones.append(("POP", None))
        else:
            print(f"Instrucción desconocida: {linea}")
    
    archivo.close()
    return instrucciones

def ejecutarInstrucciones(pila, instrucciones):
    for i in instrucciones:
        if i[0] == "PUSH":
            pila.push(i[1])
        elif i[0] == "POP":
            pila.pop()
            
instrucciones = leerInstrucciones()
pila = Pila(5)
ejecutarInstrucciones(pila,instrucciones)
pila.imprimir()