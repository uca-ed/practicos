import random

# ============================================
# Funciones auxiliares
# ============================================

def indexar(dims, indices):
    index = 0
    for i, dim in enumerate(dims):
        producto_restante = 1
        for j in range(i+1, len(dims)):
            producto_restante *= dims[j]
        index += indices[i] * producto_restante
    return index

def create_arrays(dims):
    size = 1
    for dim in dims:
        size *= dim
    inscripciones = [0] * size
    capacidad = [random.randint(20, 50) for _ in range(size)]
    return inscripciones, capacidad

# ============================================
# Funciones principales
# ============================================

def max_occupation(inscripciones, capacidad, dims):
    max_ocupacion = 0
    max_index = 0
    for i in range(len(inscripciones)):
        if capacidad[i] > 0:
            ocupacion = inscripciones[i] / capacidad[i]
            if ocupacion > max_ocupacion:
                max_ocupacion = ocupacion
                max_index = i

    indices = []
    for dim in reversed(dims):
        indices.append(max_index % dim)
        max_index //= dim
    indices.reverse()
    return indices, max_ocupacion

def avg_students_per_floor(inscripciones, dims, bloque_horario):
    total_pisos = dims[1]
    promedios = [0] * total_pisos
    for edificio in range(dims[0]):
        for piso in range(total_pisos):
            for ala in range(dims[2]):
                for aula in range(dims[3]):
                    idx = indexar(dims, [edificio, piso, ala, aula, bloque_horario])
                    promedios[piso] += inscripciones[idx]
    divisor = dims[0] * dims[2] * dims[3]
    return [p / divisor for p in promedios]

def total_students_per_wing(inscripciones, dims, edificio, piso, bloque_horario):
    resultados = [0] * dims[2]
    for ala in range(dims[2]):
        for aula in range(dims[3]):
            idx = indexar(dims, [edificio, piso, ala, aula, bloque_horario])
            resultados[ala] += inscripciones[idx]
    return resultados

# ============================================
# Programa principal
# ============================================

def main():
    dims = [4, 5, 2, 25, 85]
    inscripciones, capacidad = create_arrays(dims)

    # 🔄 Simular 100,000 inscripciones para mejor distribución
    for _ in range(100000):
        indices = [random.randint(0, dim - 1) for dim in dims]
        idx = indexar(dims, indices)
        inscripciones[idx] += 1

    # a) Aula con mayor ocupación
    indices, ocupacion = max_occupation(inscripciones, capacidad, dims)
    print("Aula con mayor porcentaje de ocupación:")
    print("Edificio:", indices[0], "| Piso:", indices[1], "| Ala:", indices[2],
          "| Aula:", indices[3], "| Bloque horario:", indices[4])
    print(f"Porcentaje de ocupación: {ocupacion * 100:.2f}%\n")

    # b) Promedio de alumnos por piso en bloque horario 5
    bloque = 5
    promedios = avg_students_per_floor(inscripciones, dims, bloque)
    print(f"Promedio de alumnos por piso en el bloque horario {bloque}:")
    for piso, promedio in enumerate(promedios):
        print(f"Piso {piso}: {promedio:.2f} alumnos en promedio")
    print()

    # c) Total de alumnos por ala en edificio/piso/bloque
    edificio = 2
    piso = 3
    bloque = 10
    totales = total_students_per_wing(inscripciones, dims, edificio, piso, bloque)
    print(f"Cantidad total de alumnos por ala en edificio {edificio}, piso {piso}, bloque horario {bloque}:")
    print(f"Ala norte (0): {totales[0]} alumnos")
    print(f"Ala sur   (1): {totales[1]} alumnos")

# Ejecutar
if __name__ == "__main__":
    main()
