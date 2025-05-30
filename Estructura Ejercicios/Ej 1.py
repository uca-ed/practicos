import json

# Configuración inicial de la cola
capacidad = 10
cola = [None] * capacidad
frente = 0
final = -1
num_elementos = 0

# Leer archivo JSON con operaciones
with open("Archivo para ej/operaciones_colas.json", "r", encoding="utf-8") as f:
    operaciones = json.load(f)

print("Operaciones cargadas:", operaciones)

# Procesamiento de operaciones
for op in operaciones:
    if op["operacion"] == "ENQUEUE":
        if num_elementos == capacidad:
            print("Error: Cola llena")
        else:
            final = (final + 1) % capacidad  # Manejo circular
            cola[final] = op["valor"]
            num_elementos += 1
    elif op["operacion"] == "DEQUEUE":
        if num_elementos == 0:
            print("Error: Cola vacía")
        else:
            frente = (frente + 1) % capacidad  # Avance circular
            num_elementos -= 1

# Reconstrucción y muestra del estado final
cola_final = []
indice = frente
for _ in range(num_elementos):
    cola_final.append(cola[indice])
    indice = (indice + 1) % capacidad

print("Cola final:", cola_final)
