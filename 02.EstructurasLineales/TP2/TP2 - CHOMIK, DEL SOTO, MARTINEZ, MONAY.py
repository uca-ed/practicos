####################################################
#########            EJERCICIO 1           #########
####################################################
print("\nEJERCICIO 1\n")

def procesar_cola(nombre_archivo):
    pos=0
    longitud=0
    cola = [None]*5
    archivo=open(nombre_archivo,"r")
    
    for linea in archivo:
        linea=linea.strip().split(',')
        if linea[0] == "ENQUEUE":
            if(longitud<len(cola)):
                cola[(pos+longitud)%len(cola)]=linea[1]
                longitud+=1
                print("Se ha encolado el valor "+linea[1])
            else:
                print("Cola llena")
                
        elif linea[0] == "DEQUEUE":
            if(longitud>0):
                rta=cola[pos]
                cola[pos]=None
                pos=(pos + 1) % len(cola)
                longitud -= 1
                print("Se ha desencolado el valor "+rta)
            else:
                print("Cola vacia")
        else:
            print("Comando inválido")
            
        print(cola)
    archivo.close()
    
procesar_cola("EJ1.txt") 
    
####################################################
#########            EJERCICIO 2           #########
####################################################
print("\nEJERCICIO 2\n")

def procesar_pila(nombre_archivo):
    top=-1
    pila = [None]*5
    archivo=open(nombre_archivo,"r")
    
    for linea in archivo:
        linea=linea.strip().split(',')
        if linea[0] == "PUSH":
            if(top<len(pila)-1):
                top+=1
                pila[top]=linea[1]
                print("PUSH del valor "+linea[1])
            else:
                print("Pila llena")
                
        elif linea[0] == "POP":
            if(top>-1):
                rta=pila[top]
                pila[top]=None
                top -= 1
                print("POP del valor "+rta)
            else:
                print("Pila vacia")
        else:
            print("Comando inválido")
            
        print(pila)
    archivo.close()

procesar_pila("EJ2.txt")

####################################################
#########            EJERCICIO 3           #########
####################################################
print("\nEJERCICIO 3\n")

class Celda:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def procesar_lista(nombre_archivo):
    cabeza = None
    
    try:
        archivo = open(nombre_archivo, "r")
        for linea in archivo:
            linea = linea.strip().split(',')
            comando = linea[0]
            
            if comando == "INSERTAR":
                valor = linea[1]
                nueva_celda = Celda(valor)
                nueva_celda.siguiente = cabeza
                cabeza = nueva_celda
                print("Se insertó el valor " + valor)
                
            elif comando == "ELIMINAR":
                if cabeza is not None:
                    rta = cabeza.dato
                    cabeza = cabeza.siguiente
                    print("Se eliminó el valor " + rta)
                else:
                    print("Lista vacía, no hay nada que eliminar")
                    
            else:
                print("Comando inválido")
            
            actual = cabeza
            estado = []
            while actual is not None:
                estado.append(actual.dato)
                actual = actual.siguiente
            estado.append("None")
            
            print("Estado: " + " -> ".join(estado))
            
        archivo.close()
    except FileNotFoundError:
        print("El archivo " + nombre_archivo + " no existe. Crealo para probar.")

procesar_lista("EJ3.txt")
##############################################
############       EJERCICIO 4      ##########
##############################################
print("\nEJERCICIO 4\n")

def radix_sort(palabras):
    if not palabras:
        return []
        
    p = max(len(palabra) for palabra in palabras)
    Q = palabras.copy()
    
    for j in range(p - 1, -1, -1):
        colas = [[] for _ in range(256)]
        
        while len(Q) > 0:
            X = Q.pop(0)
            
            if j < len(X):
                valor_caracter = ord(X[j])
            else:
                valor_caracter = 0
                
            colas[valor_caracter].append(X)
            
        for cola in colas:
            Q.extend(cola)
            
    return Q

def procesar_radix(nombre_archivo):
    try:
        archivo = open(nombre_archivo, "r", encoding="utf-8")
        palabras = []
        for linea in archivo:
            palabra = linea.strip()
            if palabra:
                palabras.append(palabra)
        archivo.close()
        
        print("Palabras leidas:")
        print(palabras)
        
        palabras_ordenadas = radix_sort(palabras)
        
        print("\nPalabras ordenadas:")
        for palabra in palabras_ordenadas:
            print(palabra)
            
    except FileNotFoundError:
        print("El archivo " + nombre_archivo + " no existe.")

procesar_radix("EJ4.txt")

####################################################
#########            EJERCICIO 5           #########
####################################################

####################################################
#########            EJERCICIO 6           #########
####################################################
print("\nEJERCICIO 6\n")

import random

d = [4,5,2,25,85]
elementos_totales  = 1
for dim in d: elementos_totales  *= dim 

INSCRIPTOS = [0]*elementos_totales
CAPACIDAD = [0]*elementos_totales

for d0 in range(d[0]):
    for d1 in range(d[1]):
        for d2 in range(d[2]):
            for d3 in range(d[3]):
                capacidad_aula = random.randint(15,60)
                for d4 in range(d[4]):
                    indice_lineal = d0*(d[1]*d[2]*d[3]*d[4]) + d1*(d[2]*d[3]*d[4]) + d2*(d[3]*d[4]) + d3*(d[4]) + d4
                                   
                    INSCRIPTOS[indice_lineal] = random.randint(0,capacidad_aula)
                    CAPACIDAD[indice_lineal] = capacidad_aula

def obtener_coordenada(indice_lineal, d):
    k = len(d)
    i = [0]*k
    resto = indice_lineal
    for j in range(k-1, -1, -1):
        i[j] = resto%d[j]
        resto = resto//d[j]
    return i 

def ocupacion_max(ins, cap, d):
    porcentaje_max = 0
    indice = 0
    for i in range(len(ins)):
        if porcentaje_max < (ins[i]/cap[i])*100:
            porcentaje_max = (ins[i]/cap[i])*100
            indice = i
    coord = obtener_coordenada(indice,d)
    print(f"El aula {coord[3]+1} (Edificio {coord[0]+1}, Piso {coord[1]+1}, Ala {coord[2]+1}) en el bloque {coord[4]+1} tiene un {porcentaje_max}% de ocupacion.")

def alumnos_por_piso(bloque, ins, d):
    bloque -= 1 
    aulas_por_piso = d[0] * d[2] * d[3] 
    for piso in range(d[1]):
        suma = 0
        for edificio in range(d[0]):
            for ala in range(d[2]):
                salto = edificio*(d[1]*d[2]*d[3]*d[4]) + piso*(d[2]*d[3]*d[4]) + ala*(d[3]*d[4]) + bloque
                for aula in range(d[3]):
                    indice = salto + aula * (d[4])
                    suma += ins[indice]
                    
        promedio = suma / aulas_por_piso
        print(f"Piso {piso+1}: Suma total = {suma} | Promedio = {promedio:.2f} alumnos.")

def alumnos_por_ala(edificio,piso,bloque,ins, d):
    edificio-=1
    piso-=1
    bloque-=1
    for ala in range(d[2]):
        suma = 0
        salto = edificio*(d[1]*d[2]*d[3]*d[4]) + piso*(d[2]*d[3]*d[4]) + ala*(d[3]*d[4]) + bloque
        for aula in range(d[3]):
            indice = salto + aula*(d[4])
            suma += ins[indice]
        print(f"Alumnos en ala {ala+1}: {suma}")

""" 
#Prueba con menos dimensiones
d = [2, 1, 1, 2, 2] 
INSCRIPTOS = [5, 3, 15, 4, 8, 9, 10, 5]
CAPACIDAD  = [10, 10, 20, 20, 10, 10, 20, 20]
"""

print("a.")
ocupacion_max(INSCRIPTOS, CAPACIDAD, d)
        
print("b.")
alumnos_por_piso(2, INSCRIPTOS, d)

print("c.")
alumnos_por_ala(2,1,2,INSCRIPTOS,d)
