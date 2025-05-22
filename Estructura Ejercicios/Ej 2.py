import json

# Capacidad máxima de la pila
capacidad = 10
pila = [None] * capacidad
top = -1

# Leer archivo JSON con operaciones
with open("Archivo para ej/operaciones_pila.json", "r", encoding="utf-8") as f:
    operaciones = json.load(f)

print("Operaciones cargadas:", operaciones)

# Procesar operaciones
for op in operaciones:
    if op["operacion"] == "PUSH":
        if top + 1 >= capacidad:
            print("Error: Pila llena")
        else:
            top += 1
            pila[top] = op["valor"]
    elif op["operacion"] == "POP":
        if top == -1:
            print("Error: Pila vacía")
        else:
            valor = pila[top]
            top -= 1

# Mostrar estado final de la pila
print("Pila final:", pila[:top + 1])

