import sys

def procesar_operaciones_cola(ruta):
    datos = []
    inicio = 0
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split()
            if not partes:
                continue
            operacion = partes[0].upper()
            if operacion == "ENQUEUE" and len(partes) > 1:
                valor = " ".join(partes[1:])
                datos.append(valor)
            elif operacion == "DEQUEUE" and inicio < len(datos):
                inicio += 1
                if inicio > len(datos) // 2:
                    datos = datos[inicio:]
                    inicio = 0
    return datos[inicio:]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python cola_arreglo.py archivo_operaciones")
        sys.exit(1)
    resultado = procesar_operaciones_cola(sys.argv[1])
    print(resultado)
