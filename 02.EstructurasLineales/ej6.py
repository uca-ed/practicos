import random
import time
import matplotlib.pyplot as plt

dim = [4, 5, 2, 25, 85]
TOTAL = dim[0] * dim[1] * dim[2] * dim[3] * dim[4]

def h(i0, i1, i2, i3, i4):
    #de multidimensional a lineal
    return (i0 * dim[1] * dim[2] * dim[3] * dim[4] +
            i1 * dim[2] * dim[3] * dim[4] +
            i2 * dim[3] * dim[4] +
            i3 * dim[4] +
            i4)

def h_inv(index):
    #de lineal a multidimensional
    n1, n2, n3, n4 = dim[1], dim[2], dim[3], dim[4]
    i0 = index // (n1*n2*n3*n4)
    index %= (n1*n2*n3*n4)
    i1 = index // (n2*n3*n4)
    index %= (n2*n3*n4)
    i2 = index // (n3*n4)
    index %= (n3*n4)
    i3 = index // n4
    i4 = index % n4
    return i0, i1, i2, i3, i4

INSCRIPTOS = [0] * TOTAL
CAPACIDAD = [0] * TOTAL

for i in range(TOTAL):
    CAPACIDAD[i] = random.randint(20, 60)
    INSCRIPTOS[i] = random.randint(0, CAPACIDAD[i])

print("Datos generados correctamente.")
print(f"Total de posiciones: {TOTAL}")

def mayor_ocupacion():
    max_porcentaje = -1
    mejor_idx = None
    for i in range(TOTAL):
        if CAPACIDAD[i] > 0:
            porc = INSCRIPTOS[i] / CAPACIDAD[i]
            if porc > max_porcentaje:
                max_porcentaje = porc
                mejor_idx = i
    print("\n(a) Aula/bloque horario con mayor porcentaje de ocupación:")
    print(f"   Índice lineal: {mejor_idx}")
    print(f"   Coordenadas (edificio, piso, ala, aula, bloque): {h_inv(mejor_idx)}")
    print(f"   Porcentaje: {max_porcentaje * 100:.2f}%")
    return mejor_idx

def promedio_por_piso(bloque):
    resultados = []
    for piso in range(dim[1]):
        total = 0
        count = 0
        for edificio in range(dim[0]):
            for ala in range(dim[2]):
                for aula in range(dim[3]):
                    idx = h(edificio, piso, ala, aula, bloque)
                    total += INSCRIPTOS[idx]
                    count += 1
        resultados.append(total / count)
    print(f"\n(b) Promedio de alumnos por piso para el bloque {bloque}:")
    for i, prom in enumerate(resultados):
        print(f"   Piso {i}: {prom:.2f} alumnos")
    return resultados

def total_por_ala(edificio, piso, bloque):
    totales = []
    for ala in range(dim[2]):
        total = 0
        for aula in range(dim[3]):
            idx = h(edificio, piso, ala, aula, bloque)
            total += INSCRIPTOS[idx]
        totales.append(total)
    print(f"\n(c) Total de alumnos por ala (edificio={edificio}, piso={piso}, bloque={bloque}):")
    print(f"   Norte: {totales[0]} alumnos")
    print(f"   Sur: {totales[1]} alumnos")
    return totales


def comparar_tiempos():
    t0 = time.time()
    for i in range(TOTAL):
        x = INSCRIPTOS[i]
    t_lineal = time.time() - t0

    t0 = time.time()
    for e in range(dim[0]):
        for p in range(dim[1]):
            for a in range(dim[2]):
                for au in range(dim[3]):
                    for b in range(dim[4]):
                        idx = h(e, p, a, au, b)
                        x = INSCRIPTOS[idx]
    t_multi = time.time() - t0

    print("\nComparación de tiempos:")
    print(f"   Acceso lineal: {t_lineal:.4f} s")
    print(f"   Acceso multidimensional: {t_multi:.4f} s")

    plt.bar(["Lineal", "Multidimensional"], [t_lineal, t_multi], color=["green", "orange"])
    plt.title("Comparación de tiempos de acceso")
    plt.ylabel("Segundos")
    plt.show()

if __name__ == "__main__":
    idx_mejor = mayor_ocupacion()
    bloque_ejemplo = 10
    promedio_por_piso(bloque_ejemplo)
    total_por_ala(1, 2, bloque_ejemplo)
    comparar_tiempos()
  