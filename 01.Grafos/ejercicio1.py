import json


def cargar_json(ruta):
    with open(ruta) as f:
        estructura = json.load(f)
        return estructura["P"], estructura["E"]


def generar_matriz_json(nodos, relaciones):
    matriz = []

    for nodo in nodos:
        fila = []

        # Set permite buscar más rápido si un nodo es vecino
        vecinos = set(relaciones.get(nodo, []))

        for posible_vecino in nodos:
            if posible_vecino in vecinos:
                fila.append(1)
            else:
                fila.append(0)

        matriz.append(fila)

    return matriz


def cargar_csv(ruta):
    matriz = []

    with open(ruta) as f:
        datos_csv = f.readlines()

        for linea_csv in datos_csv:
            fila_csv = linea_csv.strip().split(",")

            fila_csv_int = []

            for dato in fila_csv:
                fila_csv_int.append(int(dato))

            matriz.append(fila_csv_int)

    return matriz


def generar_nodos(matriz):
    return [str(i + 1) for i in range(len(matriz))]


# Literal c
def vecindad_derecha(matriz, nodos, nodo):
    lista_nodos = []

    try:
        indice = nodos.index(nodo)
        fila_adyacencia = matriz[indice]

        for i in range(len(fila_adyacencia)):
            if fila_adyacencia[i] == 1:
                lista_nodos.append(nodos[i])

    except ValueError:
        print("No se encuentra ese nodo en la matriz")

    return lista_nodos


# Literal d
def vecindad_izquierda(matriz, nodos, nodo):
    lista_nodos = []

    try:
        indice = nodos.index(nodo)

        for i in range(len(matriz)):
            fila_matriz = matriz[i]

            if fila_matriz[indice] == 1:
                lista_nodos.append(nodos[i])

    except ValueError:
        print("No se encuentra ese nodo en la matriz")

    return lista_nodos


# Literal a
def minimales(matriz, nodos):
    lista_nodos = []

    for i in range(len(matriz)):
        nodo = nodos[i]

        vecinos_izquierda = vecindad_izquierda(
            matriz,
            nodos,
            nodo
        )

        es_minimal = True

        for vecino in vecinos_izquierda:
            if vecino != nodo:
                es_minimal = False
                break

        if es_minimal:
            lista_nodos.append(nodo)

    return lista_nodos


# Literal b
def maximales(matriz, nodos):
    lista_nodos = []

    for i in range(len(matriz)):
        nodo = nodos[i]

        vecinos_derecha = vecindad_derecha(
            matriz,
            nodos,
            nodo
        )

        es_maximal = True

        for vecino in vecinos_derecha:
            if vecino != nodo:
                es_maximal = False
                break

        if es_maximal:
            lista_nodos.append(nodo)

    return lista_nodos


def cargar_grafo(ruta):

    if ruta.lower().endswith(".csv"):
        matriz = cargar_csv(ruta)
        nodos = generar_nodos(matriz)

    elif ruta.lower().endswith(".json"):
        nodos, relaciones = cargar_json(ruta)
        matriz = generar_matriz_json(nodos, relaciones)

    else:
        raise ValueError(
            "Formato no soportado. Use un archivo .csv o .json"
        )

    return matriz, nodos


def mostrar_menu(matriz, nodos):

    while True:
        print("\n--- Ejercicio 1 - Grafos ---")
        print("1. Mostrar minimales")
        print("2. Mostrar maximales")
        print("3. Vecindad derecha de un nodo")
        print("4. Vecindad izquierda de un nodo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("Minimales:", minimales(matriz, nodos))

        elif opcion == "2":
            print("Maximales:", maximales(matriz, nodos))

        elif opcion == "3":
            nodo = input("Ingrese el nodo: ").strip()

            if nodo not in nodos:
                print("No se encuentra ese nodo en el grafo")
            else:
                print(
                    "Vecindad derecha:",
                    vecindad_derecha(
                        matriz,
                        nodos,
                        nodo
                    )
                )

        elif opcion == "4":
            nodo = input("Ingrese el nodo: ").strip()

            if nodo not in nodos:
                print("No se encuentra ese nodo en el grafo")
            else:
                print(
                    "Vecindad izquierda:",
                    vecindad_izquierda(
                        matriz,
                        nodos,
                        nodo
                    )
                )

        elif opcion == "5":
            print("Fin del programa.")
            break

        else:
            print("Opción inválida")


def main():
    ruta = input(
        "Ingrese la ruta del archivo .csv o .json: "
    ).strip()

    try:
        matriz, nodos = cargar_grafo(ruta)

    except FileNotFoundError:
        print("No se encontró el archivo indicado")
        return

    except ValueError as error:
        print(error)
        return

    except json.JSONDecodeError:
        print("El archivo JSON no tiene un formato válido")
        return

    except KeyError:
        print("El archivo JSON no contiene las claves P y E")
        return

    print("\nGrafo cargado correctamente")
    print("Cantidad de nodos:", len(nodos))

    mostrar_menu(matriz, nodos)


if __name__ == "__main__":
    main()