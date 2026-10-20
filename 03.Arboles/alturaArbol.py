
import sys

def calcular_altura(n, r):
    altura = 0
    total = 0
    nodos_nivel = 1

    while total < n:
        total = total + nodos_nivel
        nodos_nivel = nodos_nivel * r
        altura = altura + 1

    return altura


r = int(sys.argv[1])
nombre_archivo = sys.argv[2]
n = 0

with open(nombre_archivo, 'r') as archivo:
    for linea in archivo:
        if linea.strip() != "":
            n = n + 1

resultado = calcular_altura(n, r)
print(resultado)
