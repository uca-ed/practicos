import numpy as np
import timeit
import matplotlib.pyplot as plt
import random

EDIFICIOS = 4
PISOS = 5
ALAS = 2
AULAS = 25
BLOQUES = 17 * 5

TOTAL_SIZE = EDIFICIOS * PISOS * ALAS * AULAS * BLOQUES

INSCRIPTOS = np.zeros(TOTAL_SIZE, dtype=int)
CAPACIDAD = np.zeros(TOTAL_SIZE, dtype=int)

def get_index(edificio, piso, ala, aula, bloque):
    return (edificio * PISOS * ALAS * AULAS * BLOQUES + 
            piso * ALAS * AULAS * BLOQUES + 
            ala * AULAS * BLOQUES + 
            aula * BLOQUES + 
            bloque)

def get_coords(index):
    bloque = index % BLOQUES
    index = index // BLOQUES
    aula = index % AULAS
    index = index // AULAS
    ala = index % ALAS
    index = index // ALAS
    piso = index % PISOS
    edificio = index // PISOS
    return (edificio, piso, ala, aula, bloque)

def cargar_datos():
    for i in range(TOTAL_SIZE):
        CAPACIDAD[i] = random.randint(20, 80)
        INSCRIPTOS[i] = random.randint(0, CAPACIDAD[i])

def aula_mayor_ocupacion():
    max_porcentaje = -1
    max_index = -1
    
    for i in range(TOTAL_SIZE):
        if CAPACIDAD[i] > 0:
            porcentaje = (INSCRIPTOS[i] / CAPACIDAD[i]) * 100
            if porcentaje > max_porcentaje:
                max_porcentaje = porcentaje
                max_index = i
    
    edificio, piso, ala, aula, bloque = get_coords(max_index)
    ala_str = "Norte" if ala == 0 else "Sur"
    return {
        "edificio": edificio,
        "piso": piso,
        "ala": ala_str,
        "aula": aula,
        "bloque": bloque,
        "porcentaje": max_porcentaje
    }

def promedio_alumnos_por_piso(bloque):
    promedios = np.zeros(PISOS, dtype=float)
    conteos = np.zeros(PISOS, dtype=int)
    
    for i in range(TOTAL_SIZE):
        _, piso, _, _, bloque_actual = get_coords(i)
        if bloque_actual == bloque:
            promedios[piso] += INSCRIPTOS[i]
            conteos[piso] += EDIFICIOS * ALAS * AULAS
    
    for piso in range(PISOS):
        if conteos[piso] > 0:
            promedios[piso] /= conteos[piso]
    
    return promedios

def alumnos_por_ala(edificio, piso, bloque):
    norte = 0
    sur = 0
    
    for ala in range(ALAS):
        for aula in range(AULAS):
            index = get_index(edificio, piso, ala, aula, bloque)
            if ala == 0:
                norte += INSCRIPTOS[index]
            else:
                sur += INSCRIPTOS[index]
    
    return {"norte": norte, "sur": sur}

def realizar_pruebas():
    cargar_datos()
    
    tiempos = {
        "aula_mayor_ocupacion": [],
        "promedio_alumnos_por_piso": [],
        "alumnos_por_ala": []
    }
    
    tiempo_a = timeit.timeit(aula_mayor_ocupacion, number=10)
    tiempos["aula_mayor_ocupacion"].append(tiempo_a / 10)

    for bloque in [0, 42, 84]:
        tiempo_b = timeit.timeit(lambda: promedio_alumnos_por_piso(bloque), number=10)
        tiempos["promedio_alumnos_por_piso"].append(tiempo_b / 10)
    
    for params in [(0, 0, 0), (2, 3, 42), (3, 4, 84)]:
        tiempo_c = timeit.timeit(lambda: alumnos_por_ala(*params), number=10)
        tiempos["alumnos_por_ala"].append(tiempo_c / 10)
    
    return tiempos

if __name__ == "__main__":
    tiempos = realizar_pruebas()
    
    print("a. Aula con mayor ocupación:")
    resultado_a = aula_mayor_ocupacion()
    print(f"   Edificio {resultado_a['edificio']}, Piso {resultado_a['piso']}, Ala {resultado_a['ala']}, "
          f"Aula {resultado_a['aula']}, Bloque {resultado_a['bloque']}: {resultado_a['porcentaje']:.2f}%")
    
    print("\nb. Promedio de alumnos por piso (bloque 0):")
    promedios = promedio_alumnos_por_piso(0)
    for piso, promedio in enumerate(promedios):
        print(f"   Piso {piso}: {promedio:.2f} alumnos")
    
    print("\nc. Alumnos por ala (edificio 0, piso 0, bloque 0):")
    alumnos = alumnos_por_ala(0, 0, 0)
    print(f"   Ala Norte: {alumnos['norte']} alumnos")
    print(f"   Ala Sur: {alumnos['sur']} alumnos")
    print("\nTiempos de ejecución promedio (segundos):")
    print("{:<30} {:<15}".format("Función", "Tiempo"))
    print("-" * 45)
    print("{:<30} {:<15.6f}".format("aula_mayor_ocupacion", tiempos["aula_mayor_ocupacion"][0]))
    print("{:<30} {:<15.6f}".format("promedio_alumnos_por_piso (bloque 0)", tiempos["promedio_alumnos_por_piso"][0]))
    print("{:<30} {:<15.6f}".format("promedio_alumnos_por_piso (bloque 42)", tiempos["promedio_alumnos_por_piso"][1]))
    print("{:<30} {:<15.6f}".format("promedio_alumnos_por_piso (bloque 84)", tiempos["promedio_alumnos_por_piso"][2]))
    print("{:<30} {:<15.6f}".format("alumnos_por_ala (0,0,0)", tiempos["alumnos_por_ala"][0]))
    print("{:<30} {:<15.6f}".format("alumnos_por_ala (2,3,42)", tiempos["alumnos_por_ala"][1]))
    print("{:<30} {:<15.6f}".format("alumnos_por_ala (3,4,84)", tiempos["alumnos_por_ala"][2]))
    
    plt.figure(figsize=(10, 6))
    labels = [
        "Mayor ocupación", 
        "Promedio piso (blq 0)", 
        "Promedio piso (blq 42)", 
        "Promedio piso (blq 84)", 
        "Alumnos ala (0,0,0)", 
        "Alumnos ala (2,3,42)", 
        "Alumnos ala (3,4,84)"
    ]
    valores = [
        tiempos["aula_mayor_ocupacion"][0],
        tiempos["promedio_alumnos_por_piso"][0],
        tiempos["promedio_alumnos_por_piso"][1],
        tiempos["promedio_alumnos_por_piso"][2],
        tiempos["alumnos_por_ala"][0],
        tiempos["alumnos_por_ala"][1],
        tiempos["alumnos_por_ala"][2]
    ]
    
    plt.bar(labels, valores)
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de tiempos de ejecución")
    plt.tight_layout()
    plt.show()