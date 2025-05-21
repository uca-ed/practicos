#Ejercicio 6:
# Se modeliza en un arreglo “INSCRIPTOS” de 5 dimensiones la cantidad de alumnos que hay en las aulas de la universidad en cada bloque horario (según las listas de inscripción).
# A tal fin, se organiza el arreglo en 5 dimensiones:

# d0: edificio (4 edificios)  
# d1: piso (5 pisos por edificio)  
# d2: ala (norte o sur)  
# d3: aula (25 aulas por ala)  
# d4: bloque horario (85 - 17 bloques horarios por 5 días)  
# También se guarda un arreglo de similares características “CAPACIDAD” para guardar la capacidad de cada una de las aulas. Dado que es dato el vector de dimensiones, se quiere representar a los arreglos de 5 dimensiones sobre arreglos de única dimensión.

# Implementar:

# Creación de las estructuras
# Carga de datos en las mismas

# Dar algoritmos que respondan los siguientes interrogantes:
# a. Cuál es el aula/bloque horario con mayor porcentaje de ocupación

# b. Promedio de alumnos por piso en un bloque horario pasado como parámetro (entre todos los edificios – sólo 5 promedios)

# c. Dado como parámetro el edificio, el piso y el bloque horario, devolver la cantidad total de alumnos que están presentes en cada ala.

# Las pruebas deben también generar datos para las dimensiones requeridas Informe comparando los tiempos de respuesta de ambos desarrollos, tanto en forma tabular como gráficamente
import random

# Dimensiones
EDIFICIOS = 4
PISOS = 5
ALAS = 2
AULAS = 25
BLOQUES = 85
TOTAL = EDIFICIOS * PISOS * ALAS * AULAS * BLOQUES

def index_5d(e, p, a, u, h):
    return (((e * PISOS + p) * ALAS + a) * AULAS + u) * BLOQUES + h

# Crear arreglos 1D
INSCRIPTOS = [0] * TOTAL
CAPACIDAD = [0] * TOTAL

# Cargar datos aleatorios
for e in range(EDIFICIOS):
    for p in range(PISOS):
        for a in range(ALAS):
            for u in range(AULAS):
                cap = random.randint(20, 50)
                for h in range(BLOQUES):
                    idx = index_5d(e, p, a, u, h)
                    CAPACIDAD[idx] = cap
                    INSCRIPTOS[idx] = random.randint(0, cap)

# a) Aula/bloque con mayor % ocupación
def max_ocupacion():
    max_por = -1
    max_idx = -1
    for i in range(TOTAL):
        if CAPACIDAD[i] > 0:
            porc = INSCRIPTOS[i] / CAPACIDAD[i]
            if porc > max_por:
                max_por = porc
                max_idx = i
    if max_idx == -1:
        print("No hay aulas con capacidad > 0")
        return
    h = max_idx % BLOQUES
    max_idx //= BLOQUES
    u = max_idx % AULAS
    max_idx //= AULAS
    a = max_idx % ALAS
    max_idx //= ALAS
    p = max_idx % PISOS
    e = max_idx // PISOS
    print(f"Mayor ocupación: Edificio {e}, Piso {p}, Ala {a}, Aula {u}, Bloque {h} con {max_por*100:.2f}%")

# b) Promedio alumnos por piso en un bloque dado
def promedio_por_piso(bloque):
    for p in range(PISOS):
        suma = 0
        cnt = 0
        for e in range(EDIFICIOS):
            for a in range(ALAS):
                for u in range(AULAS):
                    idx = index_5d(e, p, a, u, bloque)
                    suma += INSCRIPTOS[idx]
                    cnt += 1
        print(f"Piso {p}: promedio {suma/cnt:.2f} alumnos")

# c) Cantidad de alumnos por ala dado edificio, piso y bloque
def alumnos_por_ala(edificio, piso, bloque):
    for a in range(ALAS):
        suma = 0
        for u in range(AULAS):
            idx = index_5d(edificio, piso, a, u, bloque)
            suma += INSCRIPTOS[idx]
        ala = "Norte" if a == 0 else "Sur"
        print(f"Ala {ala}: {suma} alumnos")

# Prueba rápida
if __name__ == "__main__":
    max_ocupacion()
    print()
    promedio_por_piso(10)
    print()
    alumnos_por_ala(1, 2, 20)
