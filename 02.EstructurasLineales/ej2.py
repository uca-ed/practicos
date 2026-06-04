def inicializar():
    return []

def push(pila, valor):
    pila.append(valor)
    print(f"PUSH {valor}")

def pop(pila):
    if not pila:
        print("Pila vacía, no se puede desapilar")
        return None
    valor = pila.pop()
    print(f"POP -> {valor}")
    return valor

def mostrar_pila(pila):
    if not pila:
        print("Pila vacía")
    else:
        print(f"Pila (tope -> base): {' '.join(map(str, reversed(pila)))}")

def main():
    pila = inicializar()

    try:
        with open("operaciones_ej2.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue

                partes = linea.split(",")
                operacion = partes[0].strip()
                valor = int(partes[1].strip()) if len(partes) > 1 and partes[1].strip() else None

                if operacion == "PUSH" and valor is not None:
                    push(pila, valor)
                elif operacion == "POP":
                    pop(pila)
                else:
                    print(f"Operación desconocida: {operacion}")

    except FileNotFoundError:
        print("Error: no se encontró el archivo 'operaciones_ej2.txt'")
        return

    print("\nResultado final:")
    mostrar_pila(pila)

if __name__ == "__main__":
    main()
