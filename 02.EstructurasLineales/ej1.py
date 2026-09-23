class Cola:
    def __init__(self, capacidad):
        self.datos = [None] * capacidad
        self.frente = 0
        self.final = 0
        self.cantidad = 0

    def esta_vacia(self):
        return self.cantidad == 0

    def esta_llena(self):
        return self.cantidad == len(self.datos)

    def enqueue(self, valor):
        if self.esta_llena():
            print("Error: cola llena")
            return
        self.datos[self.final] = valor
        self.final = (self.final + 1) % len(self.datos)
        self.cantidad += 1

    def dequeue(self):
        if self.esta_vacia():
            print("Error: cola vacía")
            return None
        valor = self.datos[self.frente]
        self.datos[self.frente] = None
        self.frente = (self.frente + 1) % len(self.datos)
        self.cantidad -= 1
        return valor

    def mostrar(self):
        resultado = []
        pos = self.frente
        for _ in range(self.cantidad):
            resultado.append(self.datos[pos])
            pos = (pos + 1) % len(self.datos)
        print(resultado)


cola = Cola(100)

with open("op_cola.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        operacion = partes[0].upper()

        if operacion == "ENQUEUE":
            cola.enqueue(int(partes[1]))
        elif operacion == "DEQUEUE":
            cola.dequeue()

print("Cola final:")
cola.mostrar()
