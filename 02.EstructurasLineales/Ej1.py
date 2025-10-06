def procesarCola(arch):
    cola = []  # Representa la cola
    with open(arch, 'r') as f:
        for linea in f:
            partes = linea.strip().split()
            if not partes:
                continue
            operacion = partes[0].upper()
            
            if operacion == "ENCOLAR" and len(partes) > 1:
                elemento = partes[1]
                cola.append(elemento)
                print(f"Elemento encolado: {elemento}")
            elif operacion == "DESENCOLAR":
                if cola:
                    print(f"Elemento desencolado: {cola.pop(0)}")
            else:
                print(f"Operación inválida: {linea.strip()}")

    print("Cola final:", cola)


def main():
    archivo="opsCola.txt"
    procesarCola(archivo)
main()