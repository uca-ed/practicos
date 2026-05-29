#mapeo_universidad.py

import random

class GestionUniversidad1D:
    def __init__(self):
        self.S1 = 21250  
        self.S2 = 4250   
        self.S3 = 2125   
        self.S4 = 85     
        
        self.INSCRIPTOS = [0] * 85000
        self.CAPACIDAD = [0] * 85000
        self._inicializar_datos_simulados()

    def obtener_index_1d(self, d0, d1, d2, d3, d4):
        return (d0 * self.S1) + (d1 * self.S2) + (d2 * self.S3) + (d3 * self.S4) + d4

    def _inicializar_datos_simulados(self):
        random.seed(42)
        for i in range(85000):
            cap = random.randint(20, 50)
            self.CAPACIDAD[i] = cap
            self.INSCRIPTOS[i] = random.randint(0, cap)

    def mayor_porcentaje_ocupacion(self):
        max_porcentaje = -1.0
        idx_ganador = -1
        for i in range(85000):
            if self.CAPACIDAD[i] > 0:
                porcentaje = self.INSCRIPTOS[i] / self.CAPACIDAD[i]
                if porcentaje > max_porcentaje:
                    max_porcentaje = porcentaje
                    idx_ganador = i
        return idx_ganador, max_porcentaje

    def promedio_alumnos_por_piso(self, BH):
        promedios_pisos = []
        for p in range(5):
            suma_piso = 0
            for ed in range(4):
                for ala in range(2):
                    for aula in range(25):
                        idx = self.obtener_index_1d(ed, p, ala, aula, BH)
                        suma_piso += self.INSCRIPTOS[idx]
            promedios_pisos.append(suma_piso / 200)
        return promedios_pisos

    def total_alumnos_por_ala(self, E, P, BH):
        resultados_ala = {}
        for ala in range(2):
            total_alumnos = 0
            for aula in range(25):
                idx = self.obtener_index_1d(E, P, ala, aula, BH)
                total_alumnos += self.INSCRIPTOS[idx]
            nombre_ala = "Norte" if ala == 0 else "Sur"
            resultados_ala[nombre_ala] = total_alumnos
        return resultados_ala