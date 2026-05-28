tamaño_maximo = int(input("Tamaño máximo de la cola: "))

cola = {
    "datos": [None] * tamaño_maximo,
    "frente": 0,
    "fin": 0,
    "tamaño": 0
}

def enqueue(valor):
    cola["datos"][cola["fin"]] = valor
    cola["fin"] = (cola["fin"] + 1) % tamaño_maximo
    cola["tamaño"] += 1

def dequeue():
    cola["frente"] = (cola["frente"] + 1) % tamaño_maximo
    cola["tamaño"] -= 1

with open("operaciones.txt") as f:
    for linea in f:
        partes = linea.strip().split(",")
        op = partes[0].strip().upper()
        if op == "ENQUEUE":
            enqueue(partes[1].strip())
        elif op == "DEQUEUE":
            dequeue()

print("Estado final:", [cola["datos"][(cola["frente"] + i) % tamaño_maximo] for i in range(cola["tamaño"])])
