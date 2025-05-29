## Ejercicio 1


# árbol
arbol = {
    "grado": 2,
    "nodos": [
        "Animales",
        "Mamíferos", "Aves",
        "Felinos", "Caninos", "Rapaces", "Cantoras",
        "León", "Tigre", "Lobo", "Perro",
        "Águila", "Búho", "Canario", "Jilguero"
    ]
}

def alturaCalculo(n, grado):
    h = 0
    while (grado ** (h + 1) - 1) // (grado - 1) < n:
        h += 1
    return h

def arregloPreorden(nodos, grado, indice=0):
    if indice >= len(nodos):
        return []
    recorrido = [nodos[indice]]
    for i in range(1, grado + 1):
        hijo = grado * indice + i
        recorrido.extend(arregloPreorden(nodos, grado, hijo))
    return recorrido

grado = arbol["grado"]
nodos = arbol["nodos"]

# Calculo de la altura y recorrido preorden
altura = alturaCalculo(len(nodos), grado)
preorden = arregloPreorden(nodos, grado)

print("Altura del árbol:", altura)
print("Recorrido en preorden:")
print(" -> ".join(preorden))