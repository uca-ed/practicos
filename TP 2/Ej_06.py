#Ej_06

import random

#Crea y llena una tupla de n elementos, s y f son el minimo y maximo de numeros que acepta
def rand_t(n, s, f): 
    l = []
    for i in range(n):
        l.append(random.randrange(s, f, 1)) #s es el numero minimo, f es el el max, 1 es el step entre elementos
    tuple(l)
    return l

def max_ocup(Ins, Cap):
    max_porcentaje = 0
    mejor_info: None
    
    #Estaba casi bien como lo pense, osea en concepto estabamos muy cerca carajo
    
    for edi in range(4):
        for piso in range(5):
            for ala in range(2):
                for aula in range(25):
                    cap_index = edi*(5*2*25) + piso*(2*25) + ala*25 + aula
                    capacidad = Cap[cap_index]
                    
                    if capacidad == 0:
                        continue
                    
                    for horario in range(85):
                        h = edi*(5*2*25*85) + piso*(2*25*85) + ala*(25*85) + aula*85 + horario
                        inscriptos = Ins[h]
                        porcentaje = inscriptos/capacidad
                        
                        if porcentaje>max_porcentaje:
                            max_porcentaje = porcentaje
                            mejor_info = (edi, piso, ala, aula, horario)
    if mejor_info:
        edi, piso, ala, aula, horario = mejor_info
        return f"Mayor % de ocupación {max_porcentaje:.2%} en Aula {aula} y horario {horario}"
    

# b. Promedio de alumnos por piso en un bloque horario pasado como parámetro (entre todos los edificios – sólo 5 promedios)
#Osea quiere cantidad de alumnos//5 en el bloque x La suma de alumnos va a suceder un mismo bloque horario se repite 5 veces a la semana
#si yo le paso el bloque 2, osea 2 va a ser constante, no tengo porque hacer range
def alum_piso(Ins, bloque):
    prom = []
    
    for piso in range(5):
        #Estaba sacando 20 resultados porque 4*5, podes cambiar las cosas, la suma es conmutativa y va a hacer los 5 ciclos que le corresponde
        cant=0
        for edi in range(4):
            for ala in range (2):
                for aula in range(25):
                    h = edi*(5*2*25*85) + piso*(2*25*85) + ala*(25*85) + aula*85 + bloque
                    cant += Ins[h]
            
        promedio = cant/4
        prom.append(promedio)
    
    if prom:
        print (f"El promedio de alumnos por piso en el bloque de horarios {bloque}, es:")
        cont = 0
        for x in prom:
            print ( f"En el piso {cont}, hay en promedio, {x} estudiantes")
            cont +=1


# c. Dado como parámetro el edificio, el piso y el bloque horario, devolver la cantidad total de alumnos que están presentes en cada ala.
#Este salio de taquito papa, dios python pionera qsy carajooo
def total_alum(edi, piso, bloque, Ins):
    dicc = {}
    for ala in range(2):
        cant = 0
        for aula in range(25):
            h = edi*(5*2*25*85) + piso*(2*25*85) + ala*(25*85) + aula*85 + bloque
            cant += Ins[h]
        dicc[ala] = cant
        
    print ( f"En el Edificio {edi} en el piso {piso} para el Bloque horario {bloque}:")
    for x in dicc:
        print ( f"Para el ala {x} se insicribieron: {dicc[x]}")



def main():
    N = 4*5*2*25*85 #Cantidad de estu
    INSCRIPTOS = rand_t(N, 0, 75) # cantidad de alumnos que hay en las aulas
    CAPACIDAD = rand_t(4*5*2*25, 10, 100) #Capacidad de las aulas
    
    print(INSCRIPTOS, "El n es=", len(INSCRIPTOS))
    print(CAPACIDAD, "El n es=", len(CAPACIDAD))
    
    #Ej_06 a)
    print (max_ocup(INSCRIPTOS, CAPACIDAD))
    
    #Ej_06 b)
    bloque = 6
    print (alum_piso(INSCRIPTOS, bloque))
    
    #Ej_06 c)
    print (total_alum(1,2,6, INSCRIPTOS)) #Edificio, piso, bloque horario, arreglo
    
    
main()