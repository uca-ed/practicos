"""6. Se modeliza en un arreglo “INSCRIPTOS” de 5 dimensiones 
la cantidad de alumnos que hay en las aulas de la universidad en cada bloque horario (según las listas de inscripción).  

A tal fin, se organiza el arreglo en 5 dimensiones:  

    d0: edificio (4 edificios)  
    d1: piso (5 pisos por edificio)  
    d2: ala (norte o sur)  
    d3: aula (25 aulas por ala)  
    d4: bloque horario (85 - 17 bloques horarios por 5 días)  
  
  
También se guarda un arreglo de similares características “CAPACIDAD” para guardar la capacidad de cada una de las aulas. 
Dado que es dato el vector de dimensiones, se quiere representar a los arreglos de 5 dimensiones sobre arreglos de única dimensión.  

Implementar:   

Creación de las estructuras   
Carga de datos en las mismas  

Dar algoritmos que respondan los siguientes interrogantes:   
a. Cuál es el aula/bloque horario con mayor porcentaje de ocupación   

b. Promedio de alumnos por piso en un bloque horario pasado como parámetro (entre todos los edificios – sólo 5 promedios)  

c. Dado como parámetro el edificio, el piso y el bloque horario, devolver la cantidad total de alumnos que están presentes en cada ala.  


Las pruebas deben también generar datos para las dimensiones requeridas 
Informe comparando los tiempos de respuesta de ambos desarrollos, tanto en forma tabular como gráficamente  
"""

#dimensiones
E=4 #edificio
P=5 #piso
AL=2 #ala
AU=25 #aula
B=85 #bloque

N=E*P*AL*AU*B #tamaño del arreglo

def indice(e,p,a,u,b):
    return ((((e*P)+p)*AL+a)*AU+u)*B+b

capacidad=[0]*N
inscriptos=[0]*N

def cargaDatos(e,p,al,au,b):
    for e in range(E):
        for p in range(P):
            for al in range(AL):
                for au in range(AU):
                    for b in range(B):
                        i=indice(e,p,al,au,b)
                        capacidad[i] = int(input(f"Capacidad edificio {e}, piso {p}, ala {al}, aula {au}, bloque {b}: "))
                        inscriptos[i] = int(input(f"Inscriptos edificio {e}, piso {p}, ala {al}, aula {au}, bloque {b}: "))
                        i+=1


#mayor porcentaje 
def mayorOcupacion(e,p,al,au,b):
    res = (0,0,0,0,0,0,0)
    i=0
    mayor=0
    for e in range(E):
        for p in range(P):
            for al in range(AL):
                for au in range(AU):
                    for b in range(B):
                        i=indice(e,p,al,au,b)
                        cap=capacidad[i]
                        ins=inscriptos[i]
                        if cap>0:
                            porcentaje=ins/cap
                            if porcentaje>mayor:
                                mayor=porcentaje
                                res=(e,p,al,au,b,ins,cap)
                        
    e,p,al,au,b,ins,cap=res
    print(f"Edificio {e}, Piso {p}, Aula {au}, Bloque {b}")
    print(f"Inscriptos:{ins}/Capacidad:{cap} -> {(mayor*100,2)}%")
  

#promedio de alumos por piso en el bloque 
def promedio(bloque):
    for p in range(P):
        total=0
        cantidad_aulas=0
        for e in range(E):
            for al in range(AL):
                for au in range(AU):
                    i=indice(e,p,al,au,bloque)
                    total+=inscriptos[i]
                    cantidad_aulas+=1
        promedio=total/cantidad_aulas
        print(f"Piso {p}: promedio= {(promedio,2)} alumnos")



def totales(edificio,piso,bloque):
    for au in range(AU):
        norte=indice(edificio,piso,0,au,bloque)
        sur=indice(edificio,piso,1,au,bloque)
        total_norte+=inscriptos[norte]
        total_sur+=inscriptos[sur]

    print(f"\n(c) Totales por ala en edificio {edificio}, piso {piso}, bloque {bloque}:")
    print(f"Norte:{total_norte} alumnos")
    print(f"Sur:{total_sur} alumnos")
    
    
def main():
    arr1=(4,5,2,25,85)
    arr2=(2,3,1,10,52)
    arr3=(5,3,3,20,65)
    
    cargaDatos(4,5,2,25,85)
    promedio(85)
    totales(4,5,85)
    mayorOcupacion(4,5,2,25,85)
    
    cargaDatos(2,3,1,10,52)
    promedio(52)
    totales(2,3,52)
    mayorOcupacion(2,3,1,10,52)
    
    cargaDatos(5,3,3,20,65)
    promedio(65)
    totales(5,3,65)
    mayorOcupacion(5,3,3,20,65)
    