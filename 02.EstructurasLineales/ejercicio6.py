import random
import csv
class Matriz5D:
    def __init__(self,d0,d1,d2,d3,d4):
        self.arreglo = [0]*d0*d1*d2*d3*d4
        self.d0=d0
        self.d1=d1
        self.d2=d2
        self.d3=d3
        self.d4=d4
        
    def imprimirMatriz(self):
        for a in range(self.d0):
                for b in range(self.d1):
                    for c in range(self.d2):
                        for d in range(self.d3):
                            print(f"\nD0: {a} D1: {b} D2: {c} D3: {d} D4: \n")
                            for e in range(self.d4):
                                print(f"{self.ver(a,b,c,d,e)} ",end="")
                            print()
                                
    
    def llenarLaTabla(self,datos): # lleno la matriz con datos directamente
        for d in range(len(datos)):
            self.arreglo[d] = datos[d]
    
    def coordenadaAindice(self,a,b,c,d,e): 
        d0 = self.d0
        d1 = self.d1
        d2 = self.d2
        d3 = self.d3
        d4 = self.d4      
        index = a * d1*d2*d3*d4 + b * d2*d3*d4 + c * d3*d4 + d * d4 + e
        return index
    
    def indiceAcoordenadar(self,index):
        e = index % self.d4
        index = index // self.d4
        d = index % self.d3
        index = index // self.d3
        c = index % self.d2
        index = index // self.d2
        b = index % self.d1
        index = index // self.d1
        a = index
        
        return ( a , b , c , d , e)
    
    def insertar(self,a,b,c,d,e,valor):
        index = self.coordenadaAindice(a,b,c,d,e)
        if index >= len(self.arreglo) or index < 0:
            raise Exception("Indice fuera de rango")
        self.arreglo[index] = valor
        
    def ver(self,a,b,c,d,e):
        index = self.coordenadaAindice(a,b,c,d,e)
        if index >= len(self.arreglo) or index < 0:
            raise Exception("Indice fuera de rango")
        return self.arreglo[index]
    
    
def crearValoresRandomCapacidadInscriptos(max, min):
    edificios = 4
    pisos = 5
    alas = 2
    aulas = 25
    bloques = 17 * 5 # 17 bloques por dia; 5 dias
    with open("inscriptos.csv", "w") as inscriptos:
        with open("capacidad.csv", "w") as capacidad:
            for a in range(edificios):
                for b in range(pisos):
                    for c in range(alas):
                        for d in range(aulas):
                            capacidadDeAlumnos = random.randint(min,max)
                            for e in range(bloques):
                                capacidad.write(f"{capacidadDeAlumnos}\n")
                                inscriptos.write(f"{random.randint(0,capacidadDeAlumnos)}\n")
                                
    print("\n---archivos de capacidad e inscriptos creados---\n")
    
        
def aulaConMayorPorcentajeDeOcupacion(capacidad,inscriptos):
    edificios = 4
    pisos = 5
    alas = 2
    aulas = 25
    bloques = 17 * 5 # 17 bloques por dia; 5 dias
        
    maximoPorcentaje = (0,0,0,0,0) # tupla con (edificio, piso, ala, aula, porcentaje)
    
    for a in range(edificios):
        for b in range(pisos):
            for c in range(alas):
                for d in range(aulas):
                    porcentaje = 0
                    for e in range(bloques):
                        cap = capacidad.ver(a,b,c,d,e)
                        ins = inscriptos.ver(a,b,c,d,e)
                        por= int(ins)/int(cap) # porcentaje de ocupacion en 1 bloque horario de un aula
                        porcentaje += por
                    porcentaje /= bloques
                    if porcentaje > maximoPorcentaje[4]:
                        maximoPorcentaje = (a,b,c,d,porcentaje)

    return maximoPorcentaje

def bloqueConMayorPorcentajeDeOcupacion(capacidad,inscriptos):
    edificios = 4
    pisos = 5
    alas = 2
    aulas = 25
    bloques = 17 * 5 # 17 bloques por dia; 5 dias
    
    totalidadDeAulas = edificios*pisos*alas*aulas
    
    maximoPorcentaje = (0,0) # tupla con (bloque, porcentaje)

    for e in range(bloques):
        porcentaje = 0
        for a in range(edificios):
            for b in range(pisos):
                for c in range(alas):
                    for d in range(aulas):
                        cap = capacidad.ver(a,b,c,d,e)
                        ins = inscriptos.ver(a,b,c,d,e)
                        por= int(ins)/int(cap) # porcentaje de ocupacion en 1 bloque horario de un aula
                        porcentaje += por
        porcentaje /= totalidadDeAulas
        if porcentaje > maximoPorcentaje[1]:
            maximoPorcentaje = (e,porcentaje)
                        
    return maximoPorcentaje

def promedioDeAlumnos(capacidad, inscriptos, piso, bloque):
    edificios = 4
    alas = 2
    aulas = 25    
    
    promedio = 0
    
    for a in range(edificios):
        for c in range(alas):
            for d in range(aulas):
                cap = capacidad.ver(a,piso,c,d,bloque)
                ins = inscriptos.ver(a,piso,c,d,bloque)
                por= int(ins)/int(cap)
                promedio += por
                
    promedio /= edificios*alas*aulas
    return promedio


def cantidadDeAlumnosPorAula(inscriptos, edificio, piso, ala, bloque):
    aulas = 25
    
    alumnosPorAula = 0
    

    for d in range(aulas):
        ins = inscriptos.ver(edificio,piso,ala,d,bloque)
        alumnosPorAula += int(ins)
            
    return alumnosPorAula

def main():
    edificios = 4
    pisos = 5
    alas = 2
    aulas = 25
    bloques = 17 * 5 # 17 bloques por dia; 5 dias
    
    # SI NO TENES LAS TABLAS CORRÉ ESTO 1 VEZ PARA CREAR LOS ARCHIVOS CON LOS DATOS
    crearValoresRandomCapacidadInscriptos(30,15) 

    INSCRIPTOS = Matriz5D(edificios,pisos,alas,aulas,bloques)
    CAPACIDAD = Matriz5D(edificios,pisos,alas,aulas,bloques)
    
    # LLENO LA MATRIZ DE INSCRIPTOS CON LOS VALORES DE LA TABLA
    with open('inscriptos.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        datos_inscriptos = []
        lector_csv = csv.reader(archivo_csv)
        for palabra in list(lector_csv): # una lista de python con 
            datos_inscriptos.append(palabra[0])
            
        INSCRIPTOS.llenarLaTabla(datos_inscriptos)
        
    # LLENO LA MATRIZ DE CAPACIDAD CON LOS VALORES DE LA TABLA
    with open('capacidad.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        datos_capacidad = []
        lector_csv = csv.reader(archivo_csv)
        for palabra in list(lector_csv): # una lista de python con 
            datos_capacidad.append(palabra[0])
            
        CAPACIDAD.llenarLaTabla(datos_capacidad)
        
    #print("\nMatriz de CAPACIDAD:\n")
    #CAPACIDAD.imprimirMatriz()
    
    #print("\nMatriz de INSCRIPTOS:\n")
    #INSCRIPTOS.imprimirMatriz()
    
    (mpEdificio, mpPiso, mpAla, mpAula, mpPorcentaje) = aulaConMayorPorcentajeDeOcupacion(CAPACIDAD,INSCRIPTOS)
    print("El aula con maximo porcentaje de ocupacion entre todos sus bloques horarios es:")
    print(f"Edificio: {mpEdificio} Piso: {mpPiso} Ala: {"Norte" if mpAla == 0 else "Sur"} Aula: {mpAula} ")
    print(f"Porcentaje de ocupación: {int(mpPorcentaje*100)} %")
    
    (mpBloque,mpPorcentaje) = bloqueConMayorPorcentajeDeOcupacion(CAPACIDAD,INSCRIPTOS)
    print("\nEl bloque horario con maximo porcentaje de ocupacion es:")
    print(f"Bloque horario: {mpBloque} Porcentaje de ocupación: {int(mpPorcentaje*100)} %")
    
    bloqueX = random.randint(0,bloques-1)
    print(f"\nEl porcentaje de ocupación de las aulas para el bloque {bloqueX} es:")
    for pisoX in range(pisos):
        print(f"En el piso: {pisoX} el porcentaje: {int(promedioDeAlumnos(CAPACIDAD,INSCRIPTOS,pisoX,bloqueX) * 100)}%")
    
    edificioX = random.randint(0,edificios-1)
    pisoX = random.randint(0,pisos-1)
    bloqueX = random.randint(0,bloques-1)
    for ala in range(alas):
        print(f"\nPara el ala {"NORTE" if ala else "SUR"} :")
        print(f"En el edificio {edificioX} piso {pisoX} bloque horario {bloqueX},")
        print(f"hay {cantidadDeAlumnosPorAula(INSCRIPTOS,edificioX,pisoX,ala,bloqueX)} alumnos.")
        
    

print("\nEjercicio 6 - Matriz de N dimensiones sobre arreglos 1D")
main()
print()