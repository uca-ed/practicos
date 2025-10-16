#6)
import random
import time
import time
import matplotlib.pyplot as plt

D0_EDIFICIO=4
D1_PISO=5
D2_ALA=2 #aca se define el rango 0 y 1 (norte y sur)
D3_AULA=25
D4_BLOQUE_HORARIO=85
#tamaño total
tam_total= D0_EDIFICIO*D1_PISO*D2_ALA*D3_AULA*D4_BLOQUE_HORARIO
INSCRIPTOS= [0]*tam_total
CAPACIDAD= [0]*tam_total
#mapeo (vamos a convertir el indice de 5d a 1d)

def mapear_indice(i0, i1, i2, i3, i4):
    """
    Convierte el índice 5D (i0, i1, i2, i3, i4) a un índice 1D (k).
    k = i4 + D4 * (i3 + D3 * (i2 + D2 * (i1 + D1 * i0)))
    """
    if not (0 <= i0 < D0_EDIFICIO and 
            0 <= i1 < D1_PISO and 
            0 <= i2 < D2_ALA and 
            0 <= i3 < D3_AULA and 
            0 <= i4 < D4_BLOQUE_HORARIO):
        raise IndexError("Índices fuera de rango en la estructura 5D.")
    
    k = i4
    k += D4_BLOQUE_HORARIO * i3
    k += D4_BLOQUE_HORARIO * D3_AULA * i2
    k += D4_BLOQUE_HORARIO * D3_AULA * D2_ALA * i1
    k += D4_BLOQUE_HORARIO * D3_AULA * D2_ALA * D1_PISO * i0
    return k

def cargar_datos():
    for i0 in range(D0_EDIFICIO):
        for i1 in range(D1_PISO):
            for i2 in range(D2_ALA):
                for i3 in range(D3_AULA):
                    capacidad_aula=random.randint(20,80) #para que la capacidad del aula sea cte
                    for i4 in range(D4_BLOQUE_HORARIO):
                        k=mapear_indice(i0,i1,i2,i3,i4)
                        CAPACIDAD[k]=capacidad_aula
                        INSCRIPTOS[k]=random.randint(0,capacidad_aula)
cargar_datos()

def mayor_porcentaje_ocupacion():
    max_porcentaje=-1.0
    mejor_ubicacion= None
    for k in range(tam_total):
        inscriptos= INSCRIPTOS[k]
        capacidad= CAPACIDAD[k]
        if capacidad >0:
            porcentaje= (inscriptos/capacidad)*100
            if porcentaje >max_porcentaje:
                max_porcentaje= porcentaje
                mejor_ubicacion=k
    return max_porcentaje, mejor_ubicacion
# aca probamos
porcentaje, indice_1d = mayor_porcentaje_ocupacion()
print(f"\na) Mayor porcentaje de ocupación: {porcentaje:.2f}% en el índice 1D: {indice_1d}")

def promedio_alumnos_por_piso(bloque_horario):
    promedios_por_piso={} #{piso: (total_alumnos,total_aulas)}
    i4=bloque_horario #el bloque que nos interesa
    for i1 in range(D1_PISO): # Iteramos sobre los 5 pisos
        total_alumnos_piso = 0
        total_aulas_piso = 0
        for i0 in range(D0_EDIFICIO):
            for i2 in range(D2_ALA):
                for i3 in range(D3_AULA):
                    k = mapear_indice(i0, i1, i2, i3, i4)
                    total_alumnos_piso += INSCRIPTOS[k]
                    total_aulas_piso += 1
        
        if total_aulas_piso > 0:
            promedio = total_alumnos_piso / total_aulas_piso
        else:
            promedio = 0
        promedios_por_piso[i1]=promedio
    return promedios_por_piso
# aca probamos
bloque_ejemplo = random.randint(0, D4_BLOQUE_HORARIO - 1)
promedios = promedio_alumnos_por_piso(bloque_ejemplo)
print(f"\nb) Promedio de alumnos por piso para el Bloque Horario {bloque_ejemplo}:")
for piso, promedio in promedios.items():
   print(f"  Piso {piso}: {promedio:.2f} alumnos en promedio")

def alumnos_por_ala (edificio,piso,bloque_horario):
    alumnos_ala_norte= 0 #i2=0
    alumnos_ala_sur=0 #i2=1
    i0,i1,i4=edificio,piso,bloque_horario
    #ala norte
    for i3 in range (D3_AULA):
        k_norte= mapear_indice(i0,i1,0,i3,i4) #cuando ponemos 0 en la posicion del ala i2, la funcion mapear_indice sabe que nos referimos al ala norte (esta funcion solo sabe que i2 que es el ala debe ser 0 o 1)
        alumnos_ala_norte+=INSCRIPTOS[k_norte]
    #ala sur
    for i3 in range (D3_AULA):
        k_sur=mapear_indice(i0,i1,1,i3,i4)
        alumnos_ala_sur+=INSCRIPTOS[k_sur]
    return {"Norte": alumnos_ala_norte, "Sur": alumnos_ala_sur}
# aca probamos
edif_ej = random.randint(0, D0_EDIFICIO - 1)
piso_ej = random.randint(0, D1_PISO - 1)
bloque_ej_c = random.randint(0, D4_BLOQUE_HORARIO - 1)

alas = alumnos_por_ala(edif_ej, piso_ej, bloque_ej_c)
print(f"\nc) Total de alumnos en Edificio {edif_ej}, Piso {piso_ej}, Bloque {bloque_ej_c}:")
print(f"  Ala Norte: {alas['Norte']} alumnos")
print(f"  Ala Sur: {alas['Sur']} alumnos")

#medicion de tiempos
t1=time.time() #esta funcion devuelve el tiempo actual en segundos
mayor_porcentaje_ocupacion()
t2=time.time()
t3=time.time()
promedio_alumnos_por_piso(random.randint(0,D4_BLOQUE_HORARIO-1)) #usamos random porque hay 85 bloques horarios numerados 0-84, entonces eige uno al azar sin tener que escribir manualmente
t4=time.time()
t5=time.time()
alumnos_por_ala(random.randint(0,D0_EDIFICIO-1), random.randint(0,D1_PISO-1), random.randint(0, D4_BLOQUE_HORARIO-1))
t6=time.time()
tiempos = {
    "Mayor % ocupacion": t2 - t1, #t1 se guarda justo antes de ejecutar la funcion, t2 se guarda justo despues de ejecutar la funcion, entonces la resta te da cuanto tardo la funcion en ejecutarse
    "Promedio por piso": t4 - t3,
    "Alumnos por ala": t6 - t5
}

# informe tabular
print("\n--- INFORME DE TIEMPOS ---")
print(f"{'Consulta':30} {'Tiempo (segundos)':>20}")
print("-" * 55)
for nombre, t in tiempos.items():
    print(f"{nombre:30} {t:>20.6f}")

# gráfico
plt.bar(tiempos.keys(), tiempos.values())
plt.title("Comparación de tiempos de respuesta")
plt.ylabel("Tiempo (segundos)")
plt.show()
