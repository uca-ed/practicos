#Ejercicio 1:Representar colas sobre un arreglo. El algoritmo debe leer el archivo de operaciones sobre colas y operar, partiendo de una cola vacía. Se debe mostrar el resultado final.
def procesar_operaciones_cola(nombre_archivo):
    cola = []

    with open(nombre_archivo, 'r') as archivo:
        for linea_num, linea in enumerate(archivo, 1):
            partes = linea.strip().split()
            if not partes:
                continue

            operacion = partes[0]

            if operacion == "ENQUEUE":
                if len(partes) != 2:
                    print(f"Error en línea {linea_num}: falta valor para ENQUEUE")
                    continue
                valor = partes[1]
                cola.append(valor)

            elif operacion == "DEQUEUE":
                if cola:
                    eliminado = cola.pop(0)
                    print(f"DEQUEUE -> {eliminado}")
                else:
                    print(f"DEQUEUE en línea {linea_num} ignorado: cola vacía")

            else:
                print(f"Operación desconocida en línea {linea_num}: '{linea.strip()}'")

    print("\nEstado final de la cola:", cola)

if __name__ == "__main__":
    procesar_operaciones_cola("operaciones_cola.txt")
