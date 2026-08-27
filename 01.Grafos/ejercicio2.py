import json


def cargar_json(ruta):
    with open(ruta) as f:
        estructura = json.load(f)

    nodos = estructura["P"]
    relaciones = {}

    for nodo in estructura["E"]:
        relaciones[nodo] = set(estructura["E"][nodo])

    return nodos, relaciones


def es_reflexiva(nodos, relaciones):
    for nodo in nodos:
        if nodo not in relaciones[nodo]:
            return False

    return True


def es_simetrica(nodos, relaciones):
    for nodo in nodos:
        for relacion in relaciones[nodo]:
            if nodo not in relaciones[relacion]:
                return False

    return True


def es_antisimetrica(nodos, relaciones):
    for nodo in nodos:
        for relacion in relaciones[nodo]:
            if nodo != relacion and nodo in relaciones[relacion]:
                return False

    return True


def es_transitiva(nodos, relaciones):
    for nodo in nodos:
        for relacion_nodo in relaciones[nodo]:
            if not relaciones[relacion_nodo].issubset(relaciones[nodo]):
                return False

    return True


def es_equivalencia(reflexiva, simetrica, transitiva):
    return reflexiva and simetrica and transitiva


def es_orden(reflexiva, antisimetrica, transitiva):
    return reflexiva and antisimetrica and transitiva


def main():
    ruta = input("Ingrese la ruta del archivo JSON: ").strip()

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

    reflexiva = es_reflexiva(nodos, relaciones)
    simetrica = es_simetrica(nodos, relaciones)
    antisimetrica = es_antisimetrica(nodos, relaciones)
    transitiva = es_transitiva(nodos, relaciones)

    orden = es_orden(
        reflexiva,
        antisimetrica,
        transitiva
    )

    equivalencia = es_equivalencia(
        reflexiva,
        simetrica,
        transitiva
    )

    print("\n--- Propiedades de la relación ---")
    print("Reflexiva:", reflexiva)
    print("Simétrica:", simetrica)
    print("Antisimétrica:", antisimetrica)
    print("Transitiva:", transitiva)

    print("\n--- Clasificación ---")
    print("Es orden:", orden)
    print("Es equivalencia:", equivalencia)


if __name__ == "__main__":
    main()