
import random 
import time

EDIFICIOS = 4
PISOS = 5
ALAS = 2
AULAS = 25
BLOQUES = 85

TAM_ARRLINEAL= EDIFICIOS * PISOS * ALAS * AULAS * BLOQUES #esto nos da 85000

#Creación de las estructuras y carga de datos en las mismas

def indiceLineal(ed, pi, al, au, bl):
    return (ed*(PISOS*ALAS*AULAS*BLOQUES) + pi*(ALAS*AULAS*BLOQUES) + al*(AULAS*BLOQUES) + au*(BLOQUES) + bl)

INSCRIPTOS = [random.randint(0, 50) for _ in range(TAM_ARRLINEAL)]
CAPACIDAD = [random.randint(40, 60) for _ in range(TAM_ARRLINEAL)]

print(f"Los datos se generaron con exito. Total de registros: {TAM_ARRLINEAL}\n")

#a. Cuál es el aula/bloque horario con mayor porcentaje de ocupación

def aulaMayorOcupacion():
    porcentajeMax= -1
    indice_porcMax= 0 
    for i in range(TAM_ARRLINEAL):
        if CAPACIDAD[i]>0:
            porcentaje = INSCRIPTOS[i] / CAPACIDAD[i]
            if porcentaje > porcentajeMax:
                porcentajeMax = porcentaje
                indice_porcMax = i

    #descompongo indice lineal a coordenadas
    bloque = indice_porcMax % BLOQUES
    aula =  (indice_porcMax // BLOQUES) % AULAS
    ala = (indice_porcMax // (AULAS*BLOQUES)) % ALAS
    piso = (indice_porcMax // (ALAS*AULAS*BLOQUES)) % PISOS
    edificio= (indice_porcMax // (PISOS*ALAS*AULAS*BLOQUES))

    return (edificio, piso, ala, aula, bloque, porcentajeMax)

#b. Promedio de alumnos por piso en un bloque horario pasado como parámetro (entre todos los edificios – sólo 5 promedios)

def promedioPorPiso(bloque):
    promedios = []
    for p in range(PISOS):
        total = 0
        contador = 0
        for e in range(EDIFICIOS):
            for a in range(ALAS):
                for au in range(AULAS):
                    indice = indiceLineal(e, p , a , au, bloque)
                    total += INSCRIPTOS[indice]
                    contador +=1
        promedios.append(total / contador if contador>0 else 0)
    return promedios

#c. Dado como parámetro el edificio, el piso y el bloque horario, devolver la cantidad total de alumnos que están presentes en cada ala.

def totalPorAla(edificio, piso, bloque):
    totales = [0, 0]
    for a in range(ALAS):
        total = 0
        for au in range (AULAS):
            indice = indiceLineal(edificio, piso, a, au, bloque)
            total += INSCRIPTOS[indice]
        totales[a] = total
    return totales

# Comparo los tiempos de respuesta

#Aula/bloque con mayor ocupaxion
inicio1 = time.time()
aulaMayorOcupacion()
t1 = time.time() - inicio1

#Promedio de alumnos por piso en un bloque dado
bloque = 10
inicio2 = time.time()
promedioPorPiso(bloque)
t2 = time.time() - inicio2

#Total de alumnos por ala dado edificio, piso y bloque
edificio = 2
piso = 4
bloque = 20
inicio3 = time.time()
totalPorAla(edificio, piso, bloque)
t3 = time.time() - inicio3

print("-"*50)
print("COMPARACION DE TIEMPOS DE RESPUESTA")
print("-"*50)
print(f"{'Función':40} | {'Tiempo (segundos)':>17}")
print("-"*50)
print(f"{'a) Aula con mayor ocupación':40} | {t1:>17.6f}")
print(f"{'b) Promedio por piso':40} | {t2:>17.6f}")
print(f"{'c) Alumnos por ala':40} | {t3:>17.6f}")
print("-"*50)
print(f"{'TOTAL':40} | {(t1 + t2 + t3):>17.6f}")
print("-"*50)
print(" Las pruebas finalizaron correctamente.")
print("-"*50 + "\n")
