
import random
from typing import List, Tuple

# ----- Dimensiones (en este orden) -----
N_EDIFICIOS = 4
N_PISOS     = 5
N_ALAS      = 2   # 0=norte, 1=sur
N_AULAS     = 25
N_BLOQUES   = 85  # 17*5

def dims_vector() -> List[int]:
    # Orden fijo: [edificio, piso, ala, aula, bloque]
    return [N_EDIFICIOS, N_PISOS, N_ALAS, N_AULAS, N_BLOQUES]

# ----- h() e inversa h_inv() -----
def h(shape: List[int], idxs: List[int]) -> int:
    """(i1,...,ik) -> índice lineal (row-major, última dim es la que más rápido cambia)."""
    assert len(shape) == len(idxs)
    acc = 0
    stride = 1
    for j in range(len(shape) - 1, -1, -1):
        i = idxs[j]
        n = shape[j]
        assert 0 <= i < n, f"índice {i} fuera de rango [0,{n-1}] en dim {j}"
        acc += i * stride
        stride *= n
    return acc

def h_inv(shape: List[int], lin: int) -> List[int]:
    total = 1
    for n in shape: total *= n
    assert 0 <= lin < total, f"índice lineal {lin} fuera de rango [0,{total-1}]"
    out = [0]*len(shape)
    for j in range(len(shape)-1, -1, -1):
        lin, r = divmod(lin, shape[j])
        out[j] = r
    return out

# Helpers
def total_size(shape: List[int]) -> int:
    t = 1
    for n in shape: t *= n
    return t

# ----- Creación y carga -----
def crear_estructuras():
    shape = dims_vector()
    inscriptos = [0] * total_size(shape)
    # CAPACIDAD es por aula (no depende de bloque). La replico a 5D para acceso simple.
    capacidad  = [0] * total_size(shape)
    return shape, inscriptos, capacidad

def cargar_datos(shape, inscriptos, capacidad, seed_cap=123, seed_ins=456):
    random.seed(seed_cap)
    E,P,A,U,B = shape
    # Asignar capacidad fija por aula y replicar en todos los bloques
    for e in range(E):
        for p in range(P):
            for a in range(A):
                for u in range(U):
                    cap_aula = random.randint(20, 80)
                    for b in range(B):
                        lin = h(shape, [e,p,a,u,b])
                        capacidad[lin] = cap_aula

    # Inscriptos por bloque con tope en la capacidad del mismo lin
    random.seed(seed_ins)
    for lin in range(total_size(shape)):
        capacidad_lin = capacidad[lin]
        inscriptos[lin] = random.randint(0, capacidad_lin)

# ----- (a) Aula/bloque con mayor % de ocupación -----
def mayor_ocupacion(shape, insc, cap) -> Tuple[float, Tuple[int,int,int,int,int]]:
    E,P,A,U,B = shape
    best_pct = -1.0
    best_idx = (0,0,0,0,0)
    for e in range(E):
        for p in range(P):
            for a in range(A):
                for u in range(U):
                    for b in range(B):
                        lin = h(shape, [e,p,a,u,b])
                        c = cap[lin]
                        if c == 0: 
                            continue
                        pct = insc[lin] / c
                        if pct > best_pct:
                            best_pct = pct
                            best_idx = (e,p,a,u,b)
    return best_pct, best_idx

# ----- (b) Promedio de alumnos por piso en un bloque -----
def promedios_por_piso_en_bloque(shape, insc, bloque: int) -> List[float]:
    E,P,A,U,B = shape
    assert 0 <= bloque < B, "bloque fuera de rango"
    proms = [0.0]*P
    # Cantidad de aulas por piso agregando todos los edificios y alas
    denom = E * A * U
    for p in range(P):
        s = 0
        for e in range(E):
            for a in range(A):
                for u in range(U):
                    lin = h(shape, [e,p,a,u,bloque])
                    s += insc[lin]
        proms[p] = s / denom
    return proms

# ----- (c) Totales por ala dado edificio/piso/bloque -----
def totales_por_ala(shape, insc, edificio: int, piso: int, bloque: int):
    E,P,A,U,B = shape
    assert 0 <= edificio < E and 0 <= piso < P and 0 <= bloque < B
    tot = [0,0]  # [norte, sur]
    for a in range(A):
        s = 0
        for u in range(U):
            lin = h(shape, [edificio, piso, a, u, bloque])
            s += insc[lin]
        tot[a] = s
    return {"norte": tot[0], "sur": tot[1]}

def main():
    shape, ins, cap = crear_estructuras()
    cargar_datos(shape, ins, cap)

    # (a)
    pct, (e,p,a,u,b) = mayor_ocupacion(shape, ins, cap)
    print("a) Mayor ocupación:")
    print(f"   edificio={e}, piso={p}, ala={'norte' if a==0 else 'sur'}, aula={u}, bloque={b}, ocupación={pct*100:.2f}%")

    # (b)
    bloque = 10
    proms = promedios_por_piso_en_bloque(shape, ins, bloque)
    print(f"b) Promedio de alumnos por piso en bloque {bloque}:")
    for i,v in enumerate(proms):
        print(f"   piso {i}: {v:.2f} alumnos")

    # (c)
    edificio, piso, bloque = 2, 3, 10
    tot = totales_por_ala(shape, ins, edificio, piso, bloque)
    print(f"c) Totales por ala en edificio={edificio}, piso={piso}, bloque={bloque}: {tot}")

    # Chequeo opcional de límites
    T = total_size(shape)
    max_idx = h(shape, [shape[0]-1, shape[1]-1, shape[2]-1, shape[3]-1, shape[4]-1])
    assert max_idx == T-1, f"máximo índice {max_idx} debería ser {T-1}"

if __name__ == "__main__":
    main()
