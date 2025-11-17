import girosv2
from collections import deque
from typing import Tuple
import time

Estado = Tuple[int, ...]

ESTADO_RESUELTO: Estado = tuple(
    [0,1,2,3,4,5,6,7] +      # posicion de esquinas
    [0]*8 +                  # orientacion de esquinas
    [0,1,2,3,4,5,6,7,8,9,10,11] +  # poscion de aristas
    [0]*12                   # orientacion de aristas
)
class Nodo:
    def __init__(self, estado:Estado, movimiento=None, padre=None, profundidad=0):
        self.estado = estado                
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
  
def girar(cubo,giro) -> Estado:
    ep = list(cubo[0:8])
    eo = list(cubo[8:16])
    ap = list(cubo[16:28])
    ao = list(cubo[28:40])

    getattr(girosv2, giro)(ep, eo, ap, ao)

    return tuple(ep + eo + ap + ao)

def variosGiros(cubo,giros) -> Estado:
    ep = list(cubo[0:8])
    eo = list(cubo[8:16])
    ap = list(cubo[16:28])
    ao = list(cubo[28:40])

    for giro in giros:
        getattr(girosv2, giro)(ep, eo, ap, ao)

    return tuple(ep + eo + ap + ao)

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
    while nodo_der and nodo_der.movimiento:
        movimientos.append(inverso(nodo_der.movimiento))
        nodo_der = nodo_der.padre
    return movimientos

def solver(cubo_desarmado, profundidad_max=10):
    padre_izq = Nodo(cubo_desarmado)
    padre_der = Nodo(ESTADO_RESUELTO)

    if padre_izq.estado == padre_der.estado: #caso de que ya este resuelto
        return []
    
    frontera_izq = deque([padre_izq])
    frontera_der = deque([padre_der])

    visitados_izq = {padre_izq.estado: padre_izq}
    visitados_der = {padre_der.estado: padre_der}

    profundidad=0
    while frontera_izq and frontera_der and profundidad < profundidad_max:
        profundidad +=1 #en cada bucle se expande 1 frontera
        
        if len(frontera_izq) < len(frontera_der): #expandir izq si es mas chica
            tam = len(frontera_izq)
            print("se expande frontera izquierda, tamaño:",tam)
            
            for _ in range(tam):
                actual = frontera_izq.popleft()
                
                if actual.profundidad >= profundidad_max:
                    continue
                
                for mov in movimientosPosibles(actual.movimiento):
                    nodo_nuevo = girar(actual.estado, mov)
                    
                    if nodo_nuevo not in visitados_izq:
                        hijo = Nodo(nodo_nuevo, mov, actual, actual.profundidad+1)
                        visitados_izq[nodo_nuevo] = hijo
                        frontera_izq.append(hijo)
                        

                        if nodo_nuevo in visitados_der:
                            return recorridoDe(hijo, visitados_der[nodo_nuevo])
        else:
            tam = len(frontera_der)
            print("se expande frontera derecha, tamaño:",tam)
            
            for _ in range(tam):
                actual = frontera_der.popleft()

                if actual.profundidad >= profundidad_max:
                    continue
                
                for mov in movimientosPosibles(actual.movimiento):
                    nodo_nuevo = girar(actual.estado, mov)
                    
                    if nodo_nuevo not in visitados_der:
                        hijo = Nodo(nodo_nuevo, mov, actual, actual.profundidad+1)
                        visitados_der[nodo_nuevo] = hijo
                        frontera_der.append(hijo)

                        if nodo_nuevo in visitados_izq:
                            return recorridoDe(visitados_izq[nodo_nuevo], hijo)
        
    return None
       
def main():
    cubo = ESTADO_RESUELTO
    giros = ["U","R2","F","B","R","B2","R","U2","L","B2","R","Up"] # 12 giros necesarios, ~ 25 segs
    """ 
    # ejemplo de giros para desarmar el cubo (20 giros), con la version actual tarda mucho en resolver
    giros = ["U","R2","F","B","R","B2","R","U2","L","B2","R","Up","Dp","R2","F","Rp","L","B2","U2","F2"]
     """
    cubo = variosGiros(cubo,giros)
    inicio = time.time()
    print("solucion encontrada:",solver(cubo,20))
    fin = time.time()
    print("tiempo empleado:",fin-inicio)
main()
