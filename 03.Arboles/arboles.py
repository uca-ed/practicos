import math
import json

def calcular_altura(n, d): # n (numero de nodos), d (grado del árbol)
    if d == 1:
        return n - 1 
    return math.floor(math.log(n * (d - 1) + 1, d)) - 1

def preorden(arreglo, d, i=0, resultado=None): # arreglo(lista de nodos), d(grado del árbol), i(indice actual), resultado(lista para acumular el resultado)
    if resultado is None:
        resultado = []
    if i >= len(arreglo):
        return resultado
    resultado.append(arreglo[i])
    for k in range(1, d + 1):
        hijo = d * i + k
        if hijo < len(arreglo):
            preorden(arreglo, d, hijo, resultado)
    return resultado

def main():
    with open("01.json", 'r') as f:
        datos = json.load(f)
        d = datos["grado"]
        arreglo = datos["nodos"]

    altura = calcular_altura(len(arreglo), d)
    print("Altura del árbol:", altura)

    recorrido_preorden = preorden(arreglo, d)
    print("Recorrido preorden:", recorrido_preorden)

if __name__ == "__main__":
    main()