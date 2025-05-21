# EJERCICIO 3

# Nodo base
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __repr__(self):
        return f"[{self.valor}]"

# Pila (LIFO)
class Pila:
    def __init__(self):
        self.top = None

    def push(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.top
        self.top = nuevo

    def pop(self):
        if self.top is None:
            raise Exception("Error: pila vacía")
        valor = self.top.valor
        self.top = self.top.siguiente
        return valor

    def __repr__(self):
        nodos = []
        actual = self.top
        while actual:
            nodos.append(str(actual.valor))
            actual = actual.siguiente
        return "TOP → " + " → ".join(nodos) + " → None"

# Cola (FIFO)
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def enqueue(self, valor):
        nuevo = Nodo(valor)
        if self.frente is None:
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def dequeue(self):
        if self.frente is None:
            raise Exception("Error: cola vacía")
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return valor

    def __repr__(self):
        nodos = []
        actual = self.frente
        while actual:
            nodos.append(str(actual.valor))
            actual = actual.siguiente
        return "FRENTE → " + " → ".join(nodos) + " → None"

def pila():
    pila = Pila()
    pila.push(10)
    pila.push(20)
    pila.push(30)
    print(pila)
    # Salida: TOP → 30 → 20 → 10 → None

    print(pila.pop())  # 30
    print(pila)
    # Salida: TOP → 20 → 10 → None

def cola():
    cola = Cola()
    cola.enqueue(100)
    cola.enqueue(200)
    cola.enqueue(300)
    print(cola)
    # Salida: FRENTE → 100 → 200 → 300 → None

    print(cola.dequeue())  # 100
    print(cola)
    #Salida: FRENTE → 200 → 300 → None

if __name__ == "__main__":
    print("Ejercicio 3: Implementación de Pila y Cola")
    print("1. Pila")
    pila()
    print("\n2. Cola")
    cola()


