from itertools import product
from random import randint, seed

dimensiones = (4, 5, 2, 25, 85)

def tamano_total(dims):
    total = 1
    for dimension in dims:
        total *= dimension
    return total

def indice_lineal(indices, dims):
    factor = 1
    indice = 0
    for posicion in range(len(dims) - 1, -1, -1):
        indice += indices[posicion] * factor
        factor *= dims[posicion]
    return indice

def crear_arreglo(dims, valor=0):
    return [valor] * tamano_total(dims)

def cargar_dato(arreglo, dims, indices, valor):
    arreglo[indice_lineal(indices, dims)] = valor

def aula_maxima_ocupacion(inscriptos, capacidad, dims):
    mejor_indices = None
    mejor_porcentaje = -1.0
    for indices in product(*[range(d) for d in dims]):
        cap = capacidad[indice_lineal(indices, dims)]
        if cap == 0:
            continue
        ocupacion = inscriptos[indice_lineal(indices, dims)] / cap
        if ocupacion > mejor_porcentaje:
            mejor_porcentaje = ocupacion
            mejor_indices = indices
    return mejor_indices, mejor_porcentaje

def promedio_por_piso(inscriptos, dims, bloque):
    edificios, pisos, alas, aulas, bloques = dims
    promedios = []
    for piso in range(pisos):
        acumulado = 0
        contador = 0
        for edificio in range(edificios):
            for ala in range(alas):
                for aula in range(aulas):
                    indices = (edificio, piso, ala, aula, bloque)
                    acumulado += inscriptos[indice_lineal(indices, dims)]
                    contador += 1
        promedios.append(acumulado / contador if contador else 0)
    return promedios

def total_por_ala(inscriptos, dims, edificio, piso, bloque):
    alas = dims[2]
    aulas = dims[3]
    totales = []
    for ala in range(alas):
        acumulado = 0
        for aula in range(aulas):
            indices = (edificio, piso, ala, aula, bloque)
            acumulado += inscriptos[indice_lineal(indices, dims)]
        totales.append(acumulado)
    return totales

def generar_datos_prueba(dims, max_capacidad=60, semilla=42):
    seed(semilla)
    inscriptos = crear_arreglo(dims, 0)
    capacidad = crear_arreglo(dims, 0)
    for indices in product(*[range(d) for d in dims]):
        cap = randint(max_capacidad // 2, max_capacidad)
        ins = randint(0, cap)
        cargar_dato(capacidad, dims, indices, cap)
        cargar_dato(inscriptos, dims, indices, ins)
    return inscriptos, capacidad

if __name__ == "__main__":
    inscriptos, capacidad = generar_datos_prueba(dimensiones)
    indices, porcentaje = aula_maxima_ocupacion(inscriptos, capacidad, dimensiones)
    print(f"Aula con mayor ocupacion: {indices} con {porcentaje:.2%}")
    bloque = 0
    promedios = promedio_por_piso(inscriptos, dimensiones, bloque)
    print(f"Promedios por piso en bloque {bloque}: {promedios}")
    edificio = 0
    piso = 0
    totales = total_por_ala(inscriptos, dimensiones, edificio, piso, bloque)
    print(f"Totales por ala en edificio {edificio}, piso {piso}, bloque {bloque}: {totales}")
