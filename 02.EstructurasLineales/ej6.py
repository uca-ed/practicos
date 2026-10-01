import random

class ArregloLinealMultidimensional:
    def __init__(self, *dimensiones):
        self.dimensiones = dimensiones
        self.pesos = []
        peso = 1
        
        for d in reversed(dimensiones):
            self.pesos.insert(0, peso)
            peso *= d
            
        self.total_size = peso
        self.datos = [0] * self.total_size

    def get_index(self, *indices):
        idx = 0
        for i, p in zip(indices, self.pesos):
            idx += i * p
        return idx

    def get_coordenadas(self, idx):
        coords = []
        for d in reversed(self.dimensiones):
            coords.insert(0, idx % d)
            idx //= d
        return coords


def main():
    # Dimensiones: d0=Edificio(4), d1=Piso(5), d2=Ala(2), d3=Aula(25), d4=Bloque(85)
    D_EDIF, D_PISO, D_ALA, D_AULA, D_BLOQ = 4, 5, 2, 25, 85
    print("Creando estructuras y calculando pesos lineales...")
    INSCRIPTOS = ArregloLinealMultidimensional(D_EDIF, D_PISO, D_ALA, D_AULA, D_BLOQ)
    CAPACIDAD = ArregloLinealMultidimensional(D_EDIF, D_PISO, D_ALA, D_AULA)

    for i in range(CAPACIDAD.total_size):
        CAPACIDAD.datos[i] = random.randint(20, 50) # Capacidad entre 20 y 50 (datos random)

    for i in range(INSCRIPTOS.total_size):
        coords = INSCRIPTOS.get_coordenadas(i)  # coords = [edificio, piso, ala, aula, bloque]
        capacidad_aula = CAPACIDAD.datos[CAPACIDAD.get_index(coords[0], coords[1], coords[2], coords[3])]
        
        INSCRIPTOS.datos[i] = random.randint(0, capacidad_aula)

    print(f"Total datos Inscriptos: {INSCRIPTOS.total_size} | Pesos Inscriptos: {INSCRIPTOS.pesos}")
    print("-" * 50)

    
    # a. Cuál es el aula/bloque horario con mayor porcentaje de ocupación
    # Iteramos directamente sobre el arreglo lineal (1 solo FOR)
    max_pct = -1
    mejor_coord = None

    for i in range(INSCRIPTOS.total_size):
        coords = INSCRIPTOS.get_coordenadas(i)
        inscritos = INSCRIPTOS.datos[i]
        cap = CAPACIDAD.datos[CAPACIDAD.get_index(coords[0], coords[1], coords[2], coords[3])]
        
        pct = (inscritos / cap) * 100 if cap > 0 else 0
        if pct > max_pct:
            max_pct = pct
            mejor_coord = coords
            if max_pct == 100: break 

    print(f"A) Mayor ocupación: Edif {mejor_coord[0]}, Piso {mejor_coord[1]}, Ala {'Norte' if mejor_coord[2]==0 else 'Sur'}, Aula {mejor_coord[3]}, Bloque {mejor_coord[4]} -> {max_pct:.2f}%")


    # b. Promedio de alumnos por piso en un bloque horario (5 promedios)
    b_param = 42 
    sumas_piso = [0] * 5
    cant_aulas_por_piso = D_EDIF * D_ALA * D_AULA # 4 * 2 * 25 = 200


    W_PISO = INSCRIPTOS.pesos[1] 

    # Como el bloque es la dimensión menos significativa (W4=1), 
    # todos los índices lineales que pertenecen al bloque 42 terminan en 42 módulo 85.
    for i in range(INSCRIPTOS.total_size):
        if i % D_BLOQ == b_param:
            piso = (i // W_PISO) % D_PISO
            sumas_piso[piso] += INSCRIPTOS.datos[i]

    print(f"\nB) Promedio de alumnos por piso para el bloque horario {b_param}:")
    for p in range(5):
        promedio = sumas_piso[p] / cant_aulas_por_piso
        print(f"   Piso {p}: {promedio:.1f} alumnos promedio por aula.")


    # c. Dado edificio, piso y bloque, devolver total en cada ala.
    e_param, p_param, bl_param = 2, 3, 10
    
    base_idx = (e_param * INSCRIPTOS.pesos[0]) + (p_param * INSCRIPTOS.pesos[1]) + (bl_param * INSCRIPTOS.pesos[4])
    
    W_ALA = INSCRIPTOS.pesos[2]
    W_AULA = INSCRIPTOS.pesos[3]

    total_norte = 0
    total_sur = 0

    for aula in range(D_AULA):
        idx_norte = base_idx + (0 * W_ALA) + (aula * W_AULA)
        idx_sur   = base_idx + (1 * W_ALA) + (aula * W_AULA)
        
        total_norte += INSCRIPTOS.datos[idx_norte]
        total_sur   += INSCRIPTOS.datos[idx_sur]

    print(f"\nC) Edificio {e_param}, Piso {p_param}, Bloque {bl_param}:")
    print(f"   Total Ala Norte: {total_norte} alumnos.")
    print(f"   Total Ala Sur:   {total_sur} alumnos.")

if __name__ == "__main__":
    main()

    '''
    Resultados obtenidos (ejemplo):
    
    Creando estructuras y calculando pesos lineales...
Total datos Inscriptos: 85000 | Pesos Inscriptos: [21250, 4250, 2125, 85, 1]
--------------------------------------------------
A) Mayor ocupaci�n: Edif 0, Piso 0, Ala Norte, Aula 1, Bloque 12 -> 100.00%

B) Promedio de alumnos por piso para el bloque horario 42:
   Piso 0: 16.7 alumnos promedio por aula.
   Piso 1: 18.3 alumnos promedio por aula.
   Piso 2: 17.7 alumnos promedio por aula.
   Piso 3: 19.1 alumnos promedio por aula.
   Piso 4: 18.9 alumnos promedio por aula.

C) Edificio 2, Piso 3, Bloque 10:
   Total Ala Norte: 430 alumnos.
   Total Ala Sur:   395 alumnos.
    '''