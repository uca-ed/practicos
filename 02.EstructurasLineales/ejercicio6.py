"""
6. Se modeliza en un arreglo “INSCRIPTOS” de 5 dimensiones la cantidad de alumnos que hay en las aulas de
la universidad en cada bloque horario (según las listas de inscripción).  

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

c. Dado como parámetro el edificio, el piso y el bloque horario, devolver la cantidad
total de alumnos que están presentesen cada ala.  


Las pruebas deben también generar datos para las dimensiones requeridas 
Informe comparando los tiempos de respuesta de ambos desarrollos, tanto en forma tabular como gráficamente  
"""
import random
import time
import json

class Universidad:
    def __init__(self):
        self.dimensions = [4, 5, 2, 25, 17]  
        self.total_size = self.producto_lista(self.dimensions) 
        self.INSCRIPTOS = [0] * self.total_size
        self.CAPACIDAD = [0] * self.total_size
        
        
        self.edificios_nombres = ["A", "B", "C", "D"]
        self.alas_nombres = ["Norte", "Sur"]
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    
    def producto_lista(self, lista):
        resultado = 1
        for num in lista:
            resultado *= num
        return resultado
    
    def calcular_indice(self, edificio, piso, ala, aula, bloque):
        return ((((edificio * self.dimensions[1] + piso) * self.dimensions[2] + ala) 
                * self.dimensions[3] + aula) * self.dimensions[4] + bloque)
    
    def cargar_datos_aleatorios(self):
        print("Cargando datos de prueba...")
        
        for edificio in range(self.dimensions[0]):
            for piso in range(self.dimensions[1]):
                for ala in range(self.dimensions[2]):
                    for aula in range(self.dimensions[3]):
                        for bloque in range(self.dimensions[4]):
                            idx = self.calcular_indice(edificio, piso, ala, aula, bloque)
                            
                            
                            capacidad = random.randint(20, 50)
                            self.CAPACIDAD[idx] = capacidad
                            
                            
                            inscritos = random.randint(0, capacidad)
                            self.INSCRIPTOS[idx] = inscritos
        
        print("Datos cargados exitosamente!")
    
    def aula_mayor_ocupacion(self):
        print("\nBuscando aula con mayor ocupación...")
        
        max_porcentaje = 0
        mejor_aula = None
        
        for edificio in range(self.dimensions[0]):
            for piso in range(self.dimensions[1]):
                for ala in range(self.dimensions[2]):
                    for aula in range(self.dimensions[3]):
                        for bloque in range(self.dimensions[4]):
                            idx = self.calcular_indice(edificio, piso, ala, aula, bloque)
                            
                            capacidad = self.CAPACIDAD[idx]
                            inscritos = self.INSCRIPTOS[idx]
                            
                            if capacidad > 0:
                                porcentaje = (inscritos / capacidad) * 100
                                
                                if porcentaje > max_porcentaje:
                                    max_porcentaje = porcentaje
                                    mejor_aula = {
                                        'edificio': edificio,
                                        'piso': piso,
                                        'ala': ala,
                                        'aula': aula,
                                        'bloque': bloque,
                                        'inscritos': inscritos,
                                        'capacidad': capacidad,
                                        'porcentaje': porcentaje
                                    }
        
        if mejor_aula:
            dia = self.dias[mejor_aula['bloque'] // 3]  
            bloque_dia = mejor_aula['bloque'] % 3 + 1
            
            print(f"   Aula con mayor ocupación:")
            print(f"   Edificio: {self.edificios_nombres[mejor_aula['edificio']]}")
            print(f"   Piso: {mejor_aula['piso'] + 1}")
            print(f"   Ala: {self.alas_nombres[mejor_aula['ala']]}")
            print(f"   Aula: {mejor_aula['aula'] + 1}")
            print(f"   Día: {dia}, Bloque: {bloque_dia}")
            print(f"   Inscriptos: {mejor_aula['inscritos']}/{mejor_aula['capacidad']}")
            print(f"   Ocupación: {mejor_aula['porcentaje']:.2f}%")
        
        return mejor_aula
    
    def promedio_alumnos_por_piso(self, bloque_horario):
        """b. Promedio de alumnos por piso en un bloque horario pasado como parámetro"""
        print(f"\nCalculando promedios por piso para bloque {bloque_horario}...")
        
        if bloque_horario < 0 or bloque_horario >= self.dimensions[4]:
            print(" Bloque horario inválido")
            return None
        
        promedios = [0] * self.dimensions[1]  
        
        for piso in range(self.dimensions[1]):
            total_alumnos = 0
            total_aulas = 0
            
            for edificio in range(self.dimensions[0]):
                for ala in range(self.dimensions[2]):
                    for aula in range(self.dimensions[3]):
                        idx = self.calcular_indice(edificio, piso, ala, aula, bloque_horario)
                        total_alumnos += self.INSCRIPTOS[idx]
                        total_aulas += 1
            
            promedios[piso] = total_alumnos / total_aulas if total_aulas > 0 else 0
        
        print("Promedios de alumnos por piso:")
        for i, promedio in enumerate(promedios):
            print(f"   Piso {i + 1}: {promedio:.2f} alumnos")
        
        return promedios
    
    def alumnos_por_ala(self, edificio, piso, bloque_horario):
        print(f"\nCalculando alumnos por ala...")
        
        if (edificio < 0 or edificio >= self.dimensions[0] or 
            piso < 0 or piso >= self.dimensions[1] or 
            bloque_horario < 0 or bloque_horario >= self.dimensions[4]):
            print("Parámetros inválidos")
            return None
        
        alumnos_ala = [0, 0]  # [Norte, Sur]
        
        for ala in range(self.dimensions[2]):
            total_alumnos = 0
            for aula in range(self.dimensions[3]):
                idx = self.calcular_indice(edificio, piso, ala, aula, bloque_horario)
                total_alumnos += self.INSCRIPTOS[idx]
            
            alumnos_ala[ala] = total_alumnos
        
        print(f"   Alumnos en Edificio {self.edificios_nombres[edificio]}, Piso {piso + 1}:")
        print(f"   Ala Norte: {alumnos_ala[0]} alumnos")
        print(f"   Ala Sur: {alumnos_ala[1]} alumnos")
        
        return alumnos_ala

def crear_grafico_texto(tiempos):
    """Crea un gráfico ASCII en lugar de usar matplotlib"""
    print("\n" + "="*50)
    print(" GRÁFICO DE TIEMPOS (ASCII)")
    print("="*50)
    
    max_tiempo = max(tiempos.values())
    if max_tiempo > 0:
        escala = 50 / max_tiempo  
    else:
        escala = 1
    
    for consulta, tiempo in tiempos.items():
        barras = "█" * int(tiempo * escala)
        descripcion = {
            'a': 'Mayor ocupación',
            'b': 'Promedio por piso', 
            'c': 'Alumnos por ala'
        }[consulta]
        print(f"{descripcion:<20} {barras} {tiempo:.4f}s")

def prueba_rendimiento():
    """Prueba de rendimiento comparativa"""
    print(" INICIANDO PRUEBAS DE RENDIMIENTO...")
    
    uni = Universidad()
    uni.cargar_datos_aleatorios()
    
    tiempos = {}
    
    # Prueba a: Aula con mayor ocupación
    start = time.time()
    resultado_a = uni.aula_mayor_ocupacion()
    tiempos['a'] = time.time() - start
    
    # Prueba b: Promedio por piso (bloque 8 = martes mañana)
    start = time.time()
    resultado_b = uni.promedio_alumnos_por_piso(8)
    tiempos['b'] = time.time() - start
    
    # Prueba c: Alumnos por ala (edificio 1, piso 2, bloque 8)
    start = time.time()
    resultado_c = uni.alumnos_por_ala(1, 2, 8)
    tiempos['c'] = time.time() - start
    
    
    print("\n" + "="*50)
    print(" TABLA DE TIEMPOS DE RESPUESTA")
    print("="*50)
    print(f"{'Consulta':<25} | {'Tiempo (segundos)':<15}")
    print("-" * 45)
    for consulta, tiempo in tiempos.items():
        descripcion = {
            'a': 'a) Mayor ocupación',
            'b': 'b) Promedio por piso', 
            'c': 'c) Alumnos por ala'
        }[consulta]
        print(f"{descripcion:<25} | {tiempo:<15.6f}")
    
   
    crear_grafico_texto(tiempos)
    
    
    resultados = {
        'tiempos': tiempos,
        'mejor_aula': resultado_a,
        'promedios_piso': resultado_b,
        'alumnos_ala': resultado_c
    }
    
    with open('resultados_universidad.json', 'w') as f:
        json.dump(resultados, f, indent=2)
    
    print(f"\n Resultados guardados en 'resultados_universidad.json'")
    
    return tiempos, uni

if __name__ == "__main__":
   
    tiempos, universidad = prueba_rendimiento()
    
    
    print("\n" + "="*50)
    print(" EJEMPLOS ADICIONALES")
    print("="*50)
    
    
    universidad.promedio_alumnos_por_piso(12)  
    
   
    universidad.alumnos_por_ala(0, 0, 5)  


