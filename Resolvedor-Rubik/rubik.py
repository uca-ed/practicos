import girosv2
from collections import deque
import copy
import time
cubo_resuelto = {
        "esquinas_pos": [0,1,2,3,4,5,6,7],
        "esquinas_ori": [0,0,0,0,0,0,0,0],
        "aristas_pos": [0,1,2,3,4,5,6,7,8,9,10,11],
        "aristas_ori": [0,0,0,0,0,0,0,0,0,0,0,0]
    }

class Nodo:
    def __init__(self, cubo, movimiento=None, padre=None, profundidad=0):
        self.cubo = cubo                
        self.movimiento = movimiento    
        self.padre = padre              
        self.profundidad = profundidad  

    def __repr__(self):
        return f"Nodo({self.movimiento}, prof={self.profundidad})"

def movimientosPosibles(ultimo_Giro=None):
     todos = ["U", "Up", "U2",
              "R", "Rp", "R2",
              "F", "Fp", "F2",
              "L", "Lp", "L2",
              "D", "Dp", "D2",
              "B", "Bp", "B2"]
     if ultimo_Giro is None:
         return todos
     grupo = todos.index(ultimo_Giro)//3
     return todos[:grupo*3]+ todos[(grupo*3+3):]    

def generar_hijos(padre):
    hijos=[]
    for m in movimientosPosibles(padre.movimiento):
        nuevo_cubo = copy.deepcopy(padre.cubo) #para no modificar el original
        hijo = Nodo(
            cubo=nuevo_cubo,
            movimiento=m,
            padre=padre,
            profundidad=padre.profundidad + 1
        )
        getattr(girosv2,m)(hijo.cubo["esquinas_pos"],hijo.cubo["esquinas_ori"],hijo.cubo["aristas_pos"], hijo.cubo["aristas_ori"])
        hijos.append(hijo)
    return hijos
#esto es para obtener el recorrido desde la derecha
def inverso(mov):
    if mov.endswith("p"):     # si termina con "p", es el inverso (por ejemplo "Up")
        return mov[:-1]       # le quita la "p" → "U"
    elif mov.endswith("2"):   # los giros dobles son su propio inverso
        return mov
    else:
        return mov + "p"      # si no tiene "p", le agrega "p" → "U" → "Up"

def recorridoDe(nodo_izq, nodo_der):
    movimientos = []
    while nodo_izq and nodo_izq.movimiento:
        movimientos.append(nodo_izq.movimiento)
        nodo_izq = nodo_izq.padre

    movimientos.reverse()
    camino_der =[]
    while nodo_der and nodo_der.movimiento:
        movimientos.append(inverso(nodo_der.movimiento))
        nodo_der = nodo_der.padre
    camino_der.reverse()
    movimientos.extend(camino_der)
    return movimientos

def comparar_cubos(c1,c2):
    return (
        c1["esquinas_pos"] == c2["esquinas_pos"] and
        c1["esquinas_ori"] == c2["esquinas_ori"] and
        c1["aristas_pos"] == c2["aristas_pos"] and
        c1["aristas_ori"] == c2["aristas_ori"]
    )

def print_cube(cubo, giro):
    print("=== ",giro," ===")
    print("Esquinas:")
    for i, (p, o) in enumerate(zip(cubo["esquinas_pos"],cubo["esquinas_ori"])):
        print(f"  {i}: pos={p}, ori={o}")
    print("\nAristas:")
    for i, (p, o) in enumerate(zip(cubo["aristas_pos"], cubo["aristas_ori"])):
        print(f"  {i}: pos={p}, ori={o}")
    print("=================") 


def solver(cubo_desarmado, profundidad_max=10):
    padre_izq = Nodo(copy.deepcopy(cubo_desarmado))
    padre_der = Nodo(copy.deepcopy(cubo_resuelto))

    if comparar_cubos(padre_izq.cubo, padre_der.cubo): #caso de que ya este resuelto
        return []
    
    frontera_izq = deque([padre_izq])
    frontera_der = deque([padre_der])
    visitados_izq = {repr(padre_izq.cubo): padre_izq}
    visitados_der = {repr(padre_der.cubo): padre_der}
    profundidad=0
    while frontera_izq and frontera_der and profundidad < profundidad_max:
        profundidad +=1 #en cada bucle se expande 1 frontera
        if len(frontera_izq) < len(frontera_der): #expandir izq si es mas chica
            print("se expande frontera izquierda, tamaño:",len(frontera_izq))
            for _ in range(len(frontera_izq)):
                actual = frontera_izq.popleft()
                if actual.profundidad >= profundidad_max:
                    continue
                for hijo in generar_hijos(actual):
                    key = repr(hijo.cubo)
                    if key not in visitados_izq:
                        visitados_izq[key] = hijo
                        frontera_izq.append(hijo)

                        if key in visitados_der:
                            return recorridoDe(hijo, visitados_der[key])
        else:
            print("se expande frontera derecha, tamaño:",len(frontera_der))
            for _ in range(len(frontera_der)):
                actual = frontera_der.popleft()
                if actual.profundidad >= profundidad_max:
                    continue
                for hijo in generar_hijos(actual):
                    key = repr(hijo.cubo)
                    if key not in visitados_der:
                        visitados_der[key] = hijo
                        frontera_der.append(hijo)

                        if key in visitados_izq:
                            return recorridoDe(visitados_izq[key], hijo)
        
    return None

def variosGiros(cubo,giros):
    for g in giros:
        getattr(girosv2,g)(cubo["esquinas_pos"],cubo["esquinas_ori"],cubo["aristas_pos"], cubo["aristas_ori"])
        
def main():
    cubo = copy.deepcopy(cubo_resuelto)
    giros = ["U","R2","F","B","R","B2","R","U2","L","B2","R"]
    variosGiros(cubo,giros)
    inicio = time.time()
    print("solucion encontrada:",solver(cubo,20))
    fin = time.time()
    print("tiempo empleado:",fin-inicio)
main()
