import json
import sys

def leerJSON(nombre):
    """
    Lee un archivo JSON y retorna:
      - X: lista de elementos
      - R: lista de pares (x,x) para cada elemento
    """
    try:
        with open(nombre, 'r',encoding="utf-8") as f:
            estructura = json.load(f)
        X = estructura["P"]  # lista de elementos
        # Generamos R como relación de igualdad (x se relaciona consigo mismo)
        R = []
        for origen, destinos in estructura["E"].items():
            for d in destinos:
                R.append((origen, d))
        return X, R
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre}' no fue encontrado.")
        return None, None
    except KeyError:
        print(f"Error: El archivo '{nombre}' no tiene las claves esperadas.")
        return None, None

def es_reflexiva(X,R):
    for x in X:
        if (x,x) not in R:
            return False
    return True

def es_simetrica(R):
    for(x,y) in R:
        if (y,x) not in R:
            return False
    return True

def es_antisimetrica(R):
    for (x, y) in R:
        if x != y and (y, x) in R:
            return False
    return True

def es_transitiva(R):
    for (x,y) in R:
        for(y2,z) in R:
            if y==y2:
                if(x,z) not in R:
                    return False
    return True

def son_comparables(x,y,R):
    return (x,y) in R or (y,x) in R

def es_comparable(X,R):
    for x in X:
        for y in X:
            if x!=y and not son_comparables(x,y,R):
                return False
    return True

def clasificar_relacion(X,R):
    reflexiva = es_reflexiva(X, R)
    simetrica = es_simetrica(R)
    antisimetrica = es_antisimetrica(R)
    transitiva = es_transitiva(R)
    comparable = es_comparable (X,R)
    if reflexiva and antisimetrica and transitiva:
        print("La relacion es de orden parcial", end=" ")
    elif reflexiva and antisimetrica and transitiva and comparable:
        print("La relacion es de orden total", end=" ")
    elif reflexiva and simetrica and transitiva:
        print("La relacion es una relacion de quivalencia", end=" ")


def main():
    nombre_archivo = "archivos_ej2/01.json"

    X, R = leerJSON(nombre_archivo)
    
    if X is None or R is None:
        return

    print(f"\nVerificando propiedades del grafo en '{nombre_archivo}':")
    print(f"Reflexivo: {es_reflexiva(X,R)}")
    print(f"Simétrico: {es_simetrica(R)}")
    print(f"Antisimétrico: {es_antisimetrica(R)}")
    print(f"Transitivo: {es_transitiva(R)}")
    print(f"Todos los elementos comparables: {es_comparable(X,R)}\n")

    clasificar_relacion(X,R)

if __name__ == '__main__':
    main()