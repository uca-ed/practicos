tamaño_maximo = int(input("Tamaño máximo de la pila: "))

pila = {
    "datos": [None] * tamaño_maximo,
    "tope": -1
}

def push(valor):
    pila["tope"] += 1
    pila["datos"][pila["tope"]] = valor

def pop():
    pila["tope"] -= 1

with open("operaciones.txt") as f:
    for linea in f:
        partes = linea.strip().split(",")
        op = partes[0].strip().upper()
        if op == "PUSH":
            push(partes[1].strip())
        elif op == "POP":
            pop()

print("Estado final:", pila["datos"][:pila["tope"] + 1])
