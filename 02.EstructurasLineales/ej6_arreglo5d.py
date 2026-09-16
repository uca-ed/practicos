"""
Ejercicio 6 - Arreglos de 5 dimensiones representados sobre ARREGLOS LINEALES.
"""

import random

NOMBRES = ["edificio", "piso", "ala", "aula", "bloque"]
ALAS = ["norte", "sur"]


class ArregloKD:
    

    def __init__(self, dims, valor_inicial=0):
        self.dims = list(dims)
        self.k = len(dims)

       
        self.saltos = []
        for j in range(self.k):
            prod = 1
            for w in range(j + 1, self.k):
                prod *= self.dims[w]
            self.saltos.append(prod)

        self.total = self.saltos[0] * self.dims[0]
        self.arr = [valor_inicial] * self.total      

    def h(self, coords):
       
        return sum(coords[j] * self.saltos[j] for j in range(self.k))

    def h_inv(self, m):
      
        coords = []
        resto = m
        for j in range(self.k):
            coords.append(resto // self.saltos[j])
            resto = resto % self.saltos[j]
        return coords


    def get(self, coords):
        return self.arr[self.h(coords)]

    def set(self, coords, valor):
        self.arr[self.h(coords)] = valor


    def direcciones(self, fijos):
        
        base = sum(v * self.saltos[j] for j, v in fijos.items())
        libres = [j for j in range(self.k) if j not in fijos]

        if not libres:
            yield base
            return

        contador = [0] * len(libres)
        m = base
        while True:
            yield m

            
            p = len(libres) - 1
            while p >= 0:
                j = libres[p]
                contador[p] += 1
                m += self.saltos[j]                  # avanzo un salto
                if contador[p] < self.dims[j]:
                    break
                m -= self.dims[j] * self.saltos[j]   # me pase: vuelvo al inicio
                contador[p] = 0
                p -= 1
            if p < 0:
                return




def crear_estructuras(dims, semilla=42):
    
    rnd = random.Random(semilla)

    INSCRIPTOS = ArregloKD(dims)
    CAPACIDAD = ArregloKD(dims)

    n_edif, n_piso, n_ala, n_aula, n_bloque = dims

    for e in range(n_edif):
        for p in range(n_piso):
            for a in range(n_ala):
                for au in range(n_aula):
                    cap = rnd.choice([20, 25, 30, 35, 40, 50, 60, 80, 100, 120])

                  
                    base = (e * INSCRIPTOS.saltos[0] + p * INSCRIPTOS.saltos[1] +
                            a * INSCRIPTOS.saltos[2] + au * INSCRIPTOS.saltos[3])

                    for b in range(n_bloque):
                        CAPACIDAD.arr[base + b] = cap
                        
                        if rnd.random() < 0.45:
                            INSCRIPTOS.arr[base + b] = 0
                        else:
                            INSCRIPTOS.arr[base + b] = rnd.randint(1, cap)

    return INSCRIPTOS, CAPACIDAD


def describir(coords):
    e, p, a, au, b = coords
    dia = b // 17
    franja = b % 17
    return (f"edificio {e}, piso {p}, ala {ALAS[a]}, aula {au}, "
            f"bloque {b} (dia {dia}, franja {franja})")



def punto_a(INSCRIPTOS, CAPACIDAD):
    
    mejor_oc = -1.0
    mejor_m = -1
    empatan = 0

    for m in range(INSCRIPTOS.total):
        cap = CAPACIDAD.arr[m]
        if cap > 0:
            oc = INSCRIPTOS.arr[m] / cap
            if oc > mejor_oc:
                mejor_oc = oc
                mejor_m = m
                empatan = 1
            elif oc == mejor_oc:
                empatan += 1

    return mejor_m, mejor_oc, empatan


def punto_b(INSCRIPTOS, bloque):
    
    promedios = []

    for p in range(INSCRIPTOS.dims[1]):
        suma = 0
        cant = 0
        for m in INSCRIPTOS.direcciones({1: p, 4: bloque}):
            suma += INSCRIPTOS.arr[m]
            cant += 1
        promedios.append((p, suma, cant, suma / cant if cant else 0.0))

    return promedios




def punto_c(INSCRIPTOS, edificio, piso, bloque):
    
    totales = []

    for a in range(INSCRIPTOS.dims[2]):
        suma = 0
        cant = 0
        for m in INSCRIPTOS.direcciones({0: edificio, 1: piso, 2: a, 4: bloque}):
            suma += INSCRIPTOS.arr[m]
            cant += 1
        totales.append((a, suma, cant))

    return totales




def verificar(INSCRIPTOS, CAPACIDAD, bloque, edificio, piso):
    n_edif, n_piso, n_ala, n_aula, n_bloque = INSCRIPTOS.dims
    ok = True

    # a) fuerza bruta con 5 indices anidados
    mejor_oc = -1.0
    mejor_coords = None
    for e in range(n_edif):
        for p in range(n_piso):
            for a in range(n_ala):
                for au in range(n_aula):
                    for b in range(n_bloque):
                        c = [e, p, a, au, b]
                        cap = CAPACIDAD.get(c)
                        if cap > 0:
                            oc = INSCRIPTOS.get(c) / cap
                            if oc > mejor_oc:
                                mejor_oc = oc
                                mejor_coords = c
    m_lineal, oc_lineal, _ = punto_a(INSCRIPTOS, CAPACIDAD)
    ok &= abs(oc_lineal - mejor_oc) < 1e-12
    print(f"  [{'OK ' if abs(oc_lineal - mejor_oc) < 1e-12 else 'MAL'}] "
          f"punto a: version lineal y version con indices anidados coinciden "
          f"({oc_lineal:.4f} vs {mejor_oc:.4f})")

    # b)
    esperado_b = []
    for p in range(n_piso):
        s = 0
        n = 0
        for e in range(n_edif):
            for a in range(n_ala):
                for au in range(n_aula):
                    s += INSCRIPTOS.get([e, p, a, au, bloque])
                    n += 1
        esperado_b.append((p, s, n))
    obtenido_b = [(p, s, n) for p, s, n, _ in punto_b(INSCRIPTOS, bloque)]
    igual = obtenido_b == esperado_b
    ok &= igual
    print(f"  [{'OK ' if igual else 'MAL'}] punto b: los 5 promedios coinciden "
          f"(200 aulas por piso: {all(n == 200 for _, _, n in obtenido_b)})")

    # c)
    esperado_c = []
    for a in range(n_ala):
        s = 0
        n = 0
        for au in range(n_aula):
            s += INSCRIPTOS.get([edificio, piso, a, au, bloque])
            n += 1
        esperado_c.append((a, s, n))
    obtenido_c = punto_c(INSCRIPTOS, edificio, piso, bloque)
    igual = obtenido_c == esperado_c
    ok &= igual
    print(f"  [{'OK ' if igual else 'MAL'}] punto c: los totales por ala coinciden "
          f"(25 aulas por ala: {all(n == 25 for _, _, n in obtenido_c)})")

    # h / h^-1
    rnd = random.Random(7)
    consistente = True
    for _ in range(5000):
        c = [rnd.randrange(INSCRIPTOS.dims[j]) for j in range(5)]
        if INSCRIPTOS.h_inv(INSCRIPTOS.h(c)) != c:
            consistente = False
            break
    ok &= consistente
    print(f"  [{'OK ' if consistente else 'MAL'}] h y h^-1 son inversas "
          f"(5000 pruebas al azar)")

    return ok



def ejecutar(bloque=40, edificio=2, piso=3):
    DIMS = [4, 5, 2, 25, 85]

    print("CREACION DE LAS ESTRUCTURAS")
    INSCRIPTOS, CAPACIDAD = crear_estructuras(DIMS)

    print(f"  Vector de dimensiones d = {tuple(DIMS)}")
    for j in range(5):
        print(f"    d{j}: {NOMBRES[j]:<9} {INSCRIPTOS.dims[j]:>3} valores   "
              f"salto = {INSCRIPTOS.saltos[j]:>6}")
    print(f"  Arreglo lineal de {INSCRIPTOS.total} celdas "
          f"(indices 0 .. {INSCRIPTOS.total - 1})")
    print(f"  Se crearon 2 estructuras: INSCRIPTOS y CAPACIDAD")

    print("\n  Ejemplo de la funcion de direccionamiento:")
    c = [2, 3, 1, 7, 40]
    m = INSCRIPTOS.h(c)
    print(f"    h(2,3,1,7,40) = 2*21250 + 3*4250 + 1*2125 + 7*85 + 40 = {m}")
    print(f"    h^-1({m})   = {tuple(INSCRIPTOS.h_inv(m))}   -> vuelve al mismo lugar")
    print(f"    INSCRIPTOS[{m}] = {INSCRIPTOS.arr[m]} alumnos   "
          f"CAPACIDAD[{m}] = {CAPACIDAD.arr[m]} lugares")

    # ---------- a ----------
    print("\n" + "-" * 74)
    print("a) AULA / BLOQUE HORARIO CON MAYOR PORCENTAJE DE OCUPACION")
    print("-" * 74)
    m, oc, empatan = punto_a(INSCRIPTOS, CAPACIDAD)
    coords = INSCRIPTOS.h_inv(m)
    print(f"  Recorrido: una sola pasada por las {INSCRIPTOS.total} celdas del")
    print(f"             arreglo lineal. No hace falta ninguna coordenada.\n")
    print(f"  Posicion lineal ganadora : {m}")
    print(f"  Coordenadas (via h^-1)   : {describir(coords)}")
    print(f"  Inscriptos / Capacidad   : {INSCRIPTOS.arr[m]} / {CAPACIDAD.arr[m]}")
    print(f"  Ocupacion                : {oc * 100:.2f} %")
    if empatan > 1:
        print(f"  (hay {empatan} aula/bloque con esa misma ocupacion maxima; "
              f"se informa el de menor indice lineal)")

    # ---------- b ----------
    print("\n" + "-" * 74)
    print(f"b) PROMEDIO DE ALUMNOS POR PISO EN EL BLOQUE {bloque} "
          f"(dia {bloque // 17}, franja {bloque % 17})")
    print("-" * 74)
    print(f"  Para cada piso se recorren las posiciones del arreglo lineal con")
    print(f"  piso fijo y bloque fijo: 4 edificios x 2 alas x 25 aulas = 200 aulas.\n")
    print(f"  {'Piso':<8}{'Aulas':<9}{'Total alumnos':<17}{'Promedio'}")
    for p, suma, cant, prom in punto_b(INSCRIPTOS, bloque):
        print(f"  {p:<8}{cant:<9}{suma:<17}{prom:.2f}")

    # ---------- c ----------
    print("\n" + "-" * 74)
    print(f"c) ALUMNOS POR ALA EN edificio {edificio}, piso {piso}, bloque {bloque}")
    print("-" * 74)
    print(f"  Con edificio, piso, ala y bloque fijos, la unica coordenada libre")
    print(f"  es el aula (salto 85): son 25 posiciones separadas de a 85.\n")
    print(f"  {'Ala':<10}{'Aulas':<9}{'Total de alumnos presentes'}")
    total_general = 0
    for a, suma, cant in punto_c(INSCRIPTOS, edificio, piso, bloque):
        total_general += suma
        print(f"  {ALAS[a]:<10}{cant:<9}{suma}")
    print(f"  {'':<10}{'':<9}{'-' * 26}")
    print(f"  {'las dos':<10}{50:<9}{total_general}")

    # ---------- verificacion ----------
    print("\n" + "-" * 74)
    print("VERIFICACION")
    print("-" * 74)
    ok = verificar(INSCRIPTOS, CAPACIDAD, bloque, edificio, piso)
    print(f"\n  {'TODO CORRECTO' if ok else 'HAY ALGO MAL'}")

    return INSCRIPTOS, CAPACIDAD


if __name__ == "__main__":
    ejecutar()
