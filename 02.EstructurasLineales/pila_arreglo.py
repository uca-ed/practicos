import sys

def procesar_operaciones_pila(ruta):
    pila = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split()
            if not partes:
                continue
            operacion = partes[0].upper()
            if operacion == "PUSH" and len(partes) > 1:
                valor = " ".join(partes[1:])
                pila.append(valor)
            elif operacion == "POP" and pila:
                pila.pop()
    return pila

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python pila_arreglo.py archivo_operaciones")
        sys.exit(1)
    resultado = procesar_operaciones_pila(sys.argv[1])
    print(resultado)
