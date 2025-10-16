class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.items = [None]*capacidad
        self.tope = -1
        self.contador = 0

    def estaVacia(self): 
        return self.contador == 0 
    
    def estaLlena(self):
        return self.contador == self.capacidad
    
    def push(self, valor):
        if self.estaLlena():
            print("ERROR: esta llena")
            return
        self.tope = (self.tope + 1) % self.capacidad
        self.items[self.tope] = valor
        self.contador +=1

    def pop(self):
        if self.estaVacia():
            print("Error: la cola esta vacia")
            return None
        valor = self.items[self.tope]
        self.items[self.tope] = None
        self.tope = (self.tope -1 + self.capacidad) % self.capacidad
        self.contador -=1
        return valor
    
    def cima(self):
        if self.estaVacia():
            return None
        return self.items[self.tope]
    

    def mostrar(self):
        print("Contenido de la pila de base a tope: ")
        if self.estaVacia():
            print("Vacia")
            return
        i = (self.tope - self.contador +1 + self.capacidad) % self.capacidad
        for _ in range(self.contador):
            print(self.items[i], end=" ")
            i = (i+1)%self.capacidad
        print()


def procesar_operaciones(nombre_archivo, capacidad):
    pila = Pila(capacidad)
    try:
        with open(nombre_archivo, "r") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
            
                partes = linea.split()
                operacion = partes[0].upper()

                if operacion == "PUSH":
                    if len(partes) > 1:
                        valor = partes[1]
                        print(f"PUSH {valor}")
                        pila.push(valor)
                    
                    else:
                        print("Falta valor para PUSH")
                
                elif operacion == "POP":
                    valor = pila.pop()
                    print(f"POP - {valor}")
                
                elif operacion == "TOP":
                    print(f"TOP - {pila.cima()}")
                
                else: 
                    print("Operacion desconocida: {operacion}")
        print("\nResultado final: ")
        pila.mostrar()
    except FileNotFoundError:
        print(f"No se encontro el nombre del archivo: {nombre_archivo}")


if __name__ == "__main__":
    procesar_operaciones("operacionesPila.txt", capacidad=5)

