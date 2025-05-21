
#Ejercicio 2: Representar pilas sobre un arreglo. El algoritmo debe leer el archivo de operaciones sobre pilas y operar, partiendo de una pila vacía. Se debe mostrar el resultado final.
def procesar_operaciones_pila(nombre_archivo):
    pila = []

    with open(nombre_archivo, 'r') as archivo:
        for linea_num, linea in enumerate(archivo, 1):
            partes = linea.strip().split()
            if not partes:
                continue

            operacion = partes[0]

            if operacion == "PUSH":
                if len(partes) != 2:
                    print(f"Error en línea {linea_num}: falta valor para PUSH")
                    continue
                valor = partes[1]
                pila.append(valor)

            elif operacion == "POP":
                if pila:
                    eliminado = pila.pop()
                    print(f"POP -> {eliminado}")
                else:
                    print(f"POP en línea {linea_num} ignorado: pila vacía")

            else:
                print(f"Operación desconocida en línea {linea_num}: '{linea.strip()}'")

    print("\nEstado final de la pila:", pila)

if __name__ == "__main__":
    procesar_operaciones_pila("operaciones_pila.txt")
