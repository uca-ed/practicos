class Pila:
    def __init__(self, capacidad):
        self.datos = [None] * capacidad
        self.tope = 0

    def esta_vacia(self):
        return self.tope == 0

    def esta_llena(self):
        return self.tope == len(self.datos)

    def push(self, valor):
        if self.esta_llena():
            print("Error: pila llena")
            return
        self.datos[self.tope] = valor
        self.tope += 1

    def pop(self):
        if self.esta_vacia():
            print("Error: pila vacía")
            return None
        self.tope -= 1
        valor = self.datos[self.tope]
        self.datos[self.tope] = None
        return valor

    def mostrar(self):
        print(self.datos[:self.tope])


pila = Pila(100)

with open("op_pila.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        operacion = partes[0].upper()

        if operacion == "PUSH":
            pila.push(int(partes[1]))
        elif operacion == "POP":
            pila.pop()

print("Pila final:")
pila.mostrar()
