def procesarPila(archivo):
    pila = []  # Representa la pila como lista
    with open(archivo, 'r') as f:
        for linea in f:
            partes = linea.strip().split()
            if not partes:
                continue

            operacion = partes[0].upper()

            if operacion == "APILAR" and len(partes) > 1:
                elemento = partes[1]
                pila.append(elemento)
                print(f"Elemento apilado: {elemento}")
            elif operacion == "DESAPILAR":
                if pila:
                    print(f"Elemento desapilado: {pila.pop()}")
            else:
                print(f"Operación inválida: {linea.strip()}")

    print("Pila final:", pila)

def main():
    archivo="opsPila.txt"
    procesarPila(archivo)
main()