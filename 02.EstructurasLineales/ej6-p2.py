#Se modeliza en un arreglo “INSCRIPTOS” de 5 dimensiones la cantidad de alumnos que hay en las aulas de la universidad en cada bloque horario (según las listas de inscripción).
#También se guarda un arreglo de similares características “CAPACIDAD” para guardar la capacidad de cada una de las aulas. Dado que es dato el vector de dimensiones, se quiere representar a los arreglos de 5 dimensiones sobre arreglos de única dimensión.

#d0: edificio (4 edificios)  
#d1: piso (5 pisos por edificio)  
#d2: ala (norte o sur)  
#d3: aula (25 aulas por ala)  
#d4: bloque horario (85 - 17 bloques horarios por 5 días)  

#Implementar:

#Creación de las estructuras
#Carga de datos en las mismas
#Dar algoritmos que respondan los siguientes interrogantes:
#a. Cuál es el aula/bloque horario con mayor porcentaje de ocupación

#b. Promedio de alumnos por piso en un bloque horario pasado como parámetro (entre todos los edificios – sólo 5 promedios)

#c. Dado como parámetro el edificio, el piso y el bloque horario, devolver la cantidad total de alumnos que están presentes en cada ala.

#calculo de dimensiones: i0*d1*d2*d3*d4+i1*d2*d3*d4+i2*d3*d4+i3*d4+i4

import random

#a
def ocupacion(inscriptos,capacidad,tamaño,edificio,piso,ala,aula):
    max=-1.0
    indice=-1
    for i in range(tamaño):
        if capacidad[i]>0:
            porcentaje=(inscriptos[i]/capacidad[i])*100
            if porcentaje>max:
                max=porcentaje
                indice=i
    i0=indice//edificio
    resto=indice%edificio
    i1=resto//piso
    resto%=piso
    i2=resto//ala
    resto%=ala
    i3=resto//aula
    i4=resto%aula
    print(f"Mayor ocupación: {max:.2f}%")
    print(f"Indice Lineal: {indice} -> [Edificio: {i0}, Piso: {i1}, Ala: {'Norte' if i2==0 else 'Sur'}, Aula: {i3}, Bloque: {i4}]\n")

#b
def promedio(inscriptos,edificio,piso,ala,aula,horario,d0,d1,d2,d3):
    print(f"Promedio de alumnos por piso en el bloque horario {horario}:\n")
    for i1 in range(d1):
        alumnos=0
        aulas=0
        for i0 in range(d0):
            base_edificio=i0*edificio+i1*piso+horario
            for i2 in range(d2):
                base_ala=base_edificio+i2*ala
                inicio_aulas=base_ala
                fin_aulas=base_ala+(d3*aula)
                for i in range(inicio_aulas,fin_aulas,aula):
                    alumnos+=inscriptos[i]
                    aulas+=1
        if aulas>0:
            promedio=round(alumnos/aulas) #redondeo porque si no me da con decimales y no sé que tan posible es que haya 0.42 de una persona en un aula 
        else:
            promedio=0
        print(f"Piso {i1}: {promedio:.0f} alumnos en promedio")

#c
def total_alumnos_por_ala(par_edificio,par_piso,edificio,piso,ala,aula,horario,d3,inscriptos):
    base=par_edificio*edificio+par_piso*piso+horario
    inicio_norte=base+(0*ala)
    fin_norte=inicio_norte+(d3*aula)
    norte=sum(inscriptos[i] for i in range(inicio_norte,fin_norte,aula))

    inicio_sur=base+(1*ala)
    fin_sur=inicio_sur+(d3*aula)
    sur=sum(inscriptos[i] for i in range(inicio_sur,fin_sur,aula))
    
    print(f"\nTotal de alumnos en Edificio {par_edificio}, Piso {par_piso}, Bloque {horario}:\n")
    print(f"Ala Norte: {norte} alumnos")
    print(f"Ala Sur: {sur} alumnos")

def main():
    d0,d1,d2,d3,d4=4,5,2,25,85
    tamaño=d0*d1*d2*d3*d4
    edificio=d1*d2*d3*d4
    piso=d2*d3*d4
    ala=d3*d4
    aula=d4
    incriptos=[0]*tamaño
    capacidad=[0]*tamaño
    random.seed(1)
    for i in range(tamaño):
        x=random.randint(30,50)
        capacidad[i]=x 
        incriptos[i]=random.randint(0,x)

    ocupacion(incriptos,capacidad,tamaño,edificio,piso,ala,aula)
    horario=random.randint(0,d4-1)
    promedio(incriptos,edificio,piso,ala,aula,horario,d0,d1,d2,d3)
    par_edificio=random.randint(0,d0-1)
    par_piso=random.randint(0,d1-1)
    total_alumnos_por_ala(par_edificio,par_piso,edificio,piso,ala,aula,horario,d3,incriptos)
main()