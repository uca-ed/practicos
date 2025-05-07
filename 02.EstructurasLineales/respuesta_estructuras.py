"""ESTRUCTURAS LINEALES

EJERCICIO 1:
Representar colas sobre un arreglo. El algoritmo debe leer el archivo de operaciones sobre colas y operar, partiendo de una cola vacía. Se debe mostrar el resultado final.
"""

def arreglo_cola(archivo):
    cola = []
    with open(archivo, 'r') as f:
        for linea in f:
            partes = linea.strip().split()
            if not partes:
                continue

            operacion = partes[0].upper()

            if operacion == 'ENQUEUE':
                valor = partes[1]
                cola.append(valor)
                print(f'ENQUEUE {valor} -> {cola}')

            elif operacion == 'DEQUEUE':
                if cola:
                    eliminado = cola.pop(0)
                    print(f'DEQUEUE ({eliminado}) -> {cola}')
                else:
                    print('DEQUEUE falló: cola vacía')

    print('\nCola final:', cola)

arreglo_cola('cola.txt')

"""EJERCICIO 2: Representar pilas sobre un arreglo. El algoritmo debe leer el archivo de operaciones sobre pilas y operar, partiendo de una pila vacía. Se debe mostrar el resultado final.


"""

def arreglo_pila(archivo):
    pila = []

    with open(archivo, 'r') as f:
        for linea in f:
            partes = linea.strip().split()
            if not partes:
                continue

            operacion = partes[0].upper()

            if operacion == 'PUSH':
                valor = partes[1]
                pila.append(valor)
                print(f'PUSH {valor} -> {pila}')

            elif operacion == 'POP':
                if pila:
                    eliminado = pila.pop()
                    print(f'POP ({eliminado}) -> {pila}')
                else:
                    print('POP falló: pila vacía')

    print('\nPila final:', pila)


arreglo_pila('pila.txt')

"""EJERCICIO 3: Representar listas por medio de celdas con enlace simple.


"""

def crear_nodo(valor):
    return {"valor": valor, "siguiente": None}

def agregar_al_final(primer, valor):
    nuevo = crear_nodo(valor)
    if primer is None:
        return nuevo
    actual = primer
    while actual["siguiente"] is not None:
        actual = actual["siguiente"]
    actual["siguiente"] = nuevo
    return primer

def mostrar_lista(nodo):
    actual = nodo
    while actual is not None:
        print(actual["valor"], end=" -> ")
        actual = actual["siguiente"]
    print("None")

#########

#EJEMPLO

lista = None
lista = agregar_al_final(lista, 10)
lista = agregar_al_final(lista, 20)
lista = agregar_al_final(lista, 30)

mostrar_lista(lista)

"""EJERCICIO 4:

Implementar Radix Sort y ordenar las palabras de los archivos indicados.
"""

def rellenar_con_espacios(palabra, largo):
    diferencia = largo - len(palabra)
    return palabra + " " * diferencia

def radix_sort_palabras(palabras):
    if not palabras:
        return []


    max_len = 0
    for palabra in palabras:
        if len(palabra) > max_len:
            max_len = len(palabra)

    palabras_con_espacios = []
    for palabra in palabras:
        nueva = palabra
        while len(nueva) < max_len:
            nueva += " "
        palabras_con_espacios.append(nueva)

    for pos in range(max_len - 1, -1, -1):
        conteo = [[] for _ in range(256)]
        for palabra in palabras_con_espacios:
            indice = ord(palabra[pos])
            conteo[indice].append(palabra)

        palabras_con_espacios = []
        for grupo in conteo:
            for palabra in grupo:
                palabras_con_espacios.append(palabra)

    palabras_ordenadas = []
    for palabra in palabras_con_espacios:
        nueva = ""
        for caracter in palabra:
            if caracter != " ":
                nueva += caracter
        palabras_ordenadas.append(nueva)

    return palabras_ordenadas

def procesar_archivo_y_ordenar(archivo):
    palabras = []
    with open(archivo, 'r') as f:
        for linea in f:
            partes = linea.strip().split()
            for palabra in partes:
                palabras.append(palabra)

    print("\nPalabras originales:", palabras)

    ordenadas = radix_sort_palabras(palabras)

    print("\nPalabras ordenadas con Radix Sort:")
    for palabra in ordenadas:
        print(palabra)

procesar_archivo_y_ordenar("palabras.txt")

"""EJERCICIO 5

Implementar en un lenguaje de programación el algoritmo de cálculo de T-Sort basado en un grafo. De no ser posible calcularlo, indicar que la estructura es cíclica.
"""

def t_sort(grafo):
    grados = {}
    for nodo in grafo:
        grados[nodo] = 0

    for nodo in grafo:
        for vecino in grafo[nodo]:
            if vecino not in grados:
                grados[vecino] = 0
            grados[vecino] += 1

    cola = []
    for nodo in grados:
        if grados[nodo] == 0:
            cola.append(nodo)

    orden = []
    while cola:
        actual = cola.pop(0)
        orden.append(actual)

        for vecino in grafo.get(actual, []):
            grados[vecino] -= 1
            if grados[vecino] == 0:
                cola.append(vecino)


    if len(orden) != len(grados):
        print("La estructura es ciclica, no se puede aplicar t-sort")
    else:
        print("Orden topologico:", orden)

grafo_aciclico = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': [],
}
grafo_ciclico = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],
}

print("grafo sin ciclo:")
t_sort(grafo_aciclico)

print("\ngrafo con ciclo:")
t_sort(grafo_ciclico)

"""EJERCICIO 6

Se modeliza en un arreglo “INSCRIPTOS” de 5 dimensiones la cantidad de alumnos que hay en las aulas de la universidad en cada bloque horario (según las listas de inscripción).
"""

import random

D0, D1, D2, D3, D4 = 4, 5, 2, 25, 85
TAM = D0 * D1 * D2 * D3 * D4
FACTOR = [D1 * D2 * D3 * D4,
          D2 * D3 * D4,
          D3 * D4,
          D4,
          1]
def calcular_indice(i0, i1, i2, i3, i4):
    return (i0 * FACTOR[0] +
            i1 * FACTOR[1] +
            i2 * FACTOR[2] +
            i3 * FACTOR[3] +
            i4 * FACTOR[4])

inscriptos = [0] * TAM
capacidad = [0] * TAM

for e in range(D0):
    for p in range(D1):
        for a in range(D2):
            for au in range(D3):
                for bh in range(D4):
                    cap = random.randint(20, 100)
                    ocup = random.randint(0, cap)
                    idx = calcular_indice(e, p, a, au, bh)
                    capacidad[idx] = cap
                    inscriptos[idx] = ocup

# A
def mayor_ocupacion():
    max_porcentaje = -1
    mejor = None
    for e in range(D0):
        for p in range(D1):
            for a in range(D2):
                for au in range(D3):
                    for bh in range(D4):
                        idx = calcular_indice(e, p, a, au, bh)
                        cap = capacidad[idx]
                        if cap == 0:
                            continue
                        ocup = inscriptos[idx]
                        porcentaje = ocup / cap
                        if porcentaje > max_porcentaje:
                            max_porcentaje = porcentaje
                            mejor = (e, p, a, au, bh, porcentaje)
    return mejor

# B
def promedio_por_piso(bloque):
    promedios = []
    for piso in range(D1):
        total_alumnos = 0
        total_aulas = 0
        for e in range(D0):
            for a in range(D2):
                for au in range(D3):
                    idx = calcular_indice(e, piso, a, au, bloque)
                    total_alumnos += inscriptos[idx]
                    total_aulas += 1
        promedios.append(round(total_alumnos / total_aulas, 2))
    return promedios

# C
def alumnos_por_ala(edificio, piso, bloque):
    norte = 0
    sur = 0
    for ala in range(D2):
        total = 0
        for aula in range(D3):
            idx = calcular_indice(edificio, piso, ala, aula, bloque)
            total += inscriptos[idx]
        if ala == 0:
            norte = total
        else:
            sur = total
    return {"norte": norte, "sur": sur}

# Resultados
print("Aula/bloque con mayor porcentaje de ocupación:", mayor_ocupacion())
print("Promedios por piso en bloque horario 10:", promedio_por_piso(10))
print("Alumnos por ala en edificio 1, piso 3, bloque 12:", alumnos_por_ala(1, 3, 12))

"""Las pruebas deben también generar datos para las dimensiones requeridas Informe comparando los tiempos de respuesta de ambos desarrollos, tanto en forma tabular como gráficamente"""

import time
import pandas as pd

#mayor_ocupacion
start_time = time.perf_counter()
mayor_ocupacion()
end_time = time.perf_counter()
tiempo_mayor_ocupacion = end_time - start_time

#promedio_por_piso
start_time = time.perf_counter()
promedio_por_piso(10)
end_time = time.perf_counter()
tiempo_promedio_por_piso = end_time - start_time

#alumnos_por_ala
start_time = time.perf_counter()
alumnos_por_ala(1, 3, 12)
end_time = time.perf_counter()
tiempo_alumnos_por_ala = end_time - start_time


tiempos = {
    "Mayor ocupacion": tiempo_mayor_ocupacion,
    "Promedio por piso": tiempo_promedio_por_piso,
    "Alumnos por ala": tiempo_alumnos_por_ala
}

tabla_tiempos = pd.DataFrame.from_dict(tiempos, orient='index', columns=['tiempo (segundos)'])
tabla_tiempos.index.name = 'Funcion'
tabla_tiempos

import matplotlib.pyplot as plt
tiempos = {
    "Mayor ocupacin": tiempo_mayor_ocupacion,
    "Promedio por piso": tiempo_promedio_por_piso,
    "Alumnos por ala": tiempo_alumnos_por_ala
}
plt.figure(figsize=(8, 6))
plt.bar(tiempos.keys(), tiempos.values(), color='blue')
plt.title('Comparación de Tiempos de Ejecución por Función', fontsize=14)
plt.xlabel('Función', fontsize=12)
plt.ylabel('Tiempo (segundos)', fontsize=12)
plt.show()

"""EJERCICIO 7

Implementar Sort topológico sobre un grafo dado como dato en un archivo.
"""

from collections import deque

def leer_grafo(archivo):
    grafo = {}
    grados_entrada = {}

    with open(archivo, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if len(linea) == 0 or linea[0] == '#':
                pass
            else:
                partes = linea.split()
                u = int(partes[0])
                v = int(partes[1])

                if u not in grafo:
                    grafo[u] = []

                if v not in grados_entrada:
                    grados_entrada[v] = 0
                if u not in grados_entrada:
                    grados_entrada[u] = 0

                grafo[u].append(v)
                grados_entrada[v] += 1

    return grafo, grados_entrada

def ordenacion_topologica(grafo, grados_entrada):
    cola = deque([nodo for nodo, grado in grados_entrada.items() if grado == 0])
    orden = []

    while len(cola) > 0:
        nodo = cola.popleft()
        orden.append(nodo)

        for vecino in grafo.get(nodo, []):
            grados_entrada[vecino] -= 1
            if grados_entrada[vecino] == 0:
                cola.append(vecino)
    if len(orden) == len(grados_entrada):
        return orden
    else:
        return "el grafo tiene un ciclo, no se puede ordenar topologicamente"
def main():
    archivo = 'grafo.txt'
    grafo, grados_entrada = leer_grafo(archivo)
    orden = ordenacion_topologica(grafo, grados_entrada)
    print("Ordenación topologica:", orden)

if __name__ == '__main__':
    main()
