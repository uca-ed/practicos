def inicializar():
    return []

def enqueue(cola, valor):
    cola.append(valor)
    print(f"ENQUEUE {valor}")

def dequeue(cola):
    if not cola:
        print("Cola vacía, no se puede desencolar")
        return None
    valor = cola.pop(0)
    print(f"DEQUEUE -> {valor}")
    return valor

def mostrar_cola(cola):
    if not cola:
        print("Cola vacía")
    else:
        print(f"Cola (frente -> fin): {' '.join(map(str, cola))}")

def main():
    cola = inicializar()

    try:
        with open("operaciones_ej1.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue

                partes = linea.split(",")
                operacion = partes[0].strip()
                valor = int(partes[1].strip()) if len(partes) > 1 and partes[1].strip() else None

                if operacion == "ENQUEUE" and valor is not None:
                    enqueue(cola, valor)
                elif operacion == "DEQUEUE":
                    dequeue(cola)
                else:
                    print(f"Operación desconocida: {operacion}")

    except FileNotFoundError:
        print("Error: no se encontró el archivo 'operaciones_ej1.txt'")
        return

    print("\nResultado final:")
    mostrar_cola(cola)

if __name__ == "__main__":
    main()
