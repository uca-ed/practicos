import random

# arreglo de 5 dimensiones representado sobre un arreglo lineal
# d0 edificio, d1 piso, d2 ala, d3 aula, d4 bloque
dims = [4, 5, 2, 25, 85]

# pesos para la formula de linealizacion
# (cada peso es el producto de las dimensiones que vienen despues)
pesos = [1, 1, 1, 1, 1]
pesos[3] = dims[4]
pesos[2] = dims[3] * pesos[3]
pesos[1] = dims[2] * pesos[2]
pesos[0] = dims[1] * pesos[1]

total = dims[0] * pesos[0]

def h(coords):
    pos = 0
    for i in range(len(coords)):
        pos = pos + coords[i] * pesos[i]
    return pos

def coordenadas(pos):
    c = []
    for i in range(len(dims)):
        c.append((pos // pesos[i]) % dims[i])
    return c

inscriptos = [0] * total
capacidad = [0] * total

def cargar_datos():
    cap = 0
    for k in range(total):
        if k % dims[4] == 0:   # arranca un aula nueva
            cap = random.randint(20, 45)
        capacidad[k] = cap
        inscriptos[k] = random.randint(0, cap)

def aula_bloque_mas_ocupado():
    mejor_pos = 0
    mejor_pct = 0
    for k in range(total):
        if capacidad[k] > 0:
            pct = inscriptos[k] / capacidad[k]
            if pct > mejor_pct:
                mejor_pct = pct
                mejor_pos = k
    return mejor_pos, mejor_pct

def promedio_por_piso(bloque):
    suma = [0, 0, 0, 0, 0]
    cuenta = [0, 0, 0, 0, 0]
    for k in range(total):
        if k % dims[4] == bloque:
            piso = (k // pesos[1]) % dims[1]
            suma[piso] = suma[piso] + inscriptos[k]
            cuenta[piso] = cuenta[piso] + 1
    prom = []
    for p in range(5):
        prom.append(suma[p] / cuenta[p])
    return prom

def alumnos_por_ala(edificio, piso, bloque):
    norte = 0
    sur = 0
    for aula in range(dims[3]):
        k = h([edificio, piso, 0, aula, bloque])
        norte = norte + inscriptos[k]
        k = h([edificio, piso, 1, aula, bloque])
        sur = sur + inscriptos[k]
    return norte, sur


cargar_datos()

pos, pct = aula_bloque_mas_ocupado()
print("a) aula/bloque con mayor ocupacion:")
print("  pos lineal =", pos, " coords =", coordenadas(pos))
print("  ocupacion =", round(pct * 100, 1), "%")

bloque = 10
print("")
print("b) promedio por piso en el bloque", bloque)
prom = promedio_por_piso(bloque)
for p in range(5):
    print("  piso", p, "->", round(prom[p], 2))

e = 2
p = 3
b = 40
norte, sur = alumnos_por_ala(e, p, b)
print("")
print("c) alumnos por ala (edificio", e, "piso", p, "bloque", b, ")")
print("  norte:", norte, " sur:", sur)
