import json


def cargar_json(ruta):
    with open(ruta) as f:
        estructura = json.load(f)

    nodos = estructura["P"]
    relaciones = {}

    for nodo in estructura["E"]:
        relaciones[nodo] = set(estructura["E"][nodo])

    return nodos, relaciones


def reconstruir_camino(anterior, origen, destino):
    camino = [destino]
    nodo_actual = destino

    while nodo_actual != origen:
        nodo_actual = anterior[nodo_actual]
        camino.append(nodo_actual)

    camino.reverse()

    return camino


def buscar_camino(nodos, relaciones, origen, destino):

    if origen not in nodos or destino not in nodos:
        return None

    if origen == destino:
        return [origen]

    cola = [origen]
    indice = 0

    visitados = {origen}
    anterior = {}

    while indice < len(cola):
        nodo_actual = cola[indice]
        indice += 1

        for vecino in relaciones.get(nodo_actual, []):

            if vecino not in visitados:
                visitados.add(vecino)

                anterior[vecino] = nodo_actual

                cola.append(vecino)

                if vecino == destino:
                    return reconstruir_camino(
                        anterior,
                        origen,
                        destino
                    )

    return None


def main():
    ruta = input(
        "Ingrese la ruta del archivo JSON: "
    ).strip()

    try:
        nodos, relaciones = cargar_json(ruta)

    except FileNotFoundError:
        print("No se encontró el archivo indicado")
        return

    except json.JSONDecodeError:
        print("El archivo no tiene un formato JSON válido")
        return

    except KeyError:
        print("El archivo JSON no contiene las claves esperadas")
        return

    origen = input("Ingrese el nodo de origen: ").strip()
    destino = input("Ingrese el nodo de destino: ").strip()

    if origen not in nodos:
        print("El nodo de origen no pertenece al grafo")
        return

    if destino not in nodos:
        print("El nodo de destino no pertenece al grafo")
        return

    camino = buscar_camino(
        nodos,
        relaciones,
        origen,
        destino
    )

    if camino is None:
        print(
            "No existe un paso desde",
            origen,
            "hasta",
            destino
        )

    else:
        print("Paso encontrado:")
        print(" -> ".join(camino))


if __name__ == "__main__":
    main()