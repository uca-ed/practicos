import random
import time
import matplotlib.pyplot as plt

# Constantes de dimensión
EDIFICIOS = 4
PISOS = 5
ALAS = 2
AULAS = 25
BLOQUES = 85
TOTAL = EDIFICIOS * PISOS * ALAS * AULAS * BLOQUES #es 85000

def index_5d(e, p, a, u, h):
    return (((e * PISOS + p) * ALAS + a) * AULAS + u) * BLOQUES + h

# Creación de estructuras unidimensionales
INSCRIPTOS = [0] * TOTAL
CAPACIDAD = [0] * TOTAL

# Carga de datos aleatorios simulados
for e in range(EDIFICIOS):
    for p in range(PISOS):
        for a in range(ALAS):
            for u in range(AULAS):
                cap = random.randint(20, 50)
                for h in range(BLOQUES):
                    idx = index_5d(e, p, a, u, h)
                    CAPACIDAD[idx] = cap
                    INSCRIPTOS[idx] = random.randint(0, cap)

# a) Aula/bloque horario con mayor porcentaje de ocupación
def max_ocupacion():
    max_porcentaje = -1
    mejor_idx = -1
    for idx in range(TOTAL):
        if CAPACIDAD[idx] > 0:
            porcentaje = INSCRIPTOS[idx] / CAPACIDAD[idx]
            if porcentaje > max_porcentaje:
                max_porcentaje = porcentaje
                mejor_idx = idx

    if mejor_idx != -1:
        e = mejor_idx // (PISOS * ALAS * AULAS * BLOQUES)
        rem = mejor_idx % (PISOS * ALAS * AULAS * BLOQUES)
        p = rem // (ALAS * AULAS * BLOQUES)
        rem %= (ALAS * AULAS * BLOQUES)
        a = rem // (AULAS * BLOQUES)
        rem %= (AULAS * BLOQUES)
        u = rem // BLOQUES
        h = rem % BLOQUES

        print(f"[a] Mayor ocupación: Edificio {e}, Piso {p}, Ala {a}, Aula {u}, Bloque {h}")
        print(f"    Porcentaje de ocupación: {max_porcentaje * 100:.2f}%")
    else:
        print("[a] No se encontró ninguna aula con capacidad mayor a 0")

# b) Promedio de alumnos por piso para un bloque horario dado
def promedio_por_piso(bloque):
    print(f"[b] Promedio de alumnos por piso en el bloque horario {bloque}:")
    for piso in range(PISOS):
        total_alumnos = 0
        cantidad = 0
        for e in range(EDIFICIOS):
            for a in range(ALAS):
                for u in range(AULAS):
                    idx = index_5d(e, piso, a, u, bloque)
                    total_alumnos += INSCRIPTOS[idx]
                    cantidad += 1
        promedio = total_alumnos / cantidad
        print(f"    Piso {piso}: {promedio:.2f} alumnos")

# c) Cantidad de alumnos por ala, dado edificio, piso y bloque horario
def alumnos_por_ala(edificio, piso, bloque):
    print(f"[c] Alumnos por ala en edificio {edificio}, piso {piso}, bloque {bloque}:")
    for a in range(ALAS):
        total = 0
        for u in range(AULAS):
            idx = index_5d(edificio, piso, a, u, bloque)
            total += INSCRIPTOS[idx]
        ala_nombre = "Norte" if a == 0 else "Sur"
        print(f"    Ala {ala_nombre}: {total} alumnos")


# ----------- EJECUCIÓN Y MEDICIÓN -----------

if __name__ == "__main__":
    start = time.time()
    max_ocupacion()
    promedio_por_piso(10)
    alumnos_por_ala(2, 3, 50)
    end = time.time()

    print(f"\nTiempo total: {end - start:.4f} segundos")


def medir_tiempo(func, *args):
    t0 = time.time()
    func(*args)
    t1 = time.time()
    return t1 - t0

tiempos = [
    medir_tiempo(max_ocupacion),
    medir_tiempo(promedio_por_piso, 10),
    medir_tiempo(alumnos_por_ala, 2, 3, 50)
]

# Mostrar en tabla
print("\n🔍 Comparación de tiempos:")
print("Función".ljust(40), "Tiempo (s)")
print("-" * 50)
print("Mayor ocupación".ljust(40), f"{tiempos[0]:.5f}")
print("Promedio por piso (bloque 10)".ljust(40), f"{tiempos[1]:.5f}")
print("Alumnos por ala (Ed 2, P 3, B 50)".ljust(40), f"{tiempos[2]:.5f}")

# Mostrar en gráfico
plt.bar(["Mayor ocupación", "Promedio por piso", "Alumnos por ala"], tiempos, color="skyblue")
plt.ylabel("Tiempo (segundos)")
plt.title("Comparación de tiempos de ejecución")
plt.grid(True)
plt.tight_layout()
plt.show()

