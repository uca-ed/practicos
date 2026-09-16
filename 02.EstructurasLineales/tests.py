

from ej1_cola import ColaArreglo
from ej2_pila import PilaArreglo
from ej3_lista import ListaEnlaceSimple
from ej6_arreglo5d import ArregloKD
import itertools

fallos = 0


def chequear(desc, condicion):
    global fallos
    print(f"  [{'OK ' if condicion else 'MAL'}] {desc}")
    if not condicion:
        fallos += 1


print("COLA - la vuelta circular (lo mas importante)")
c = ColaArreglo(5)
for v in [6, 2, 3]:
    c.enqueue(v)
c.dequeue()          # sale el 6, Pos pasa a 1
c.dequeue()          # sale el 2, Pos pasa a 2
c.enqueue(4)         # va a (2+1)%5 = 3
c.enqueue(5)         # va a (2+2)%5 = 4
c.enqueue(9)         # va a (2+3)%5 = 0  <- DA LA VUELTA
chequear("el 9 se guardo en el indice 0 reusando el hueco", c.arr[0] == 9)
chequear("Pos = 2", c.Pos == 2)
chequear("longitud = 4", c.longitud == 4)
chequear("contenido en orden = [3,4,5,9]", c.contenido() == [3, 4, 5, 9])

print("\nCOLA - casos limite")
c2 = ColaArreglo(2)
c2.enqueue("x")
c2.enqueue("y")
try:
    c2.enqueue("z")
    chequear("enqueue en cola llena tira error", False)
except Exception:
    chequear("enqueue en cola llena tira error", True)

c3 = ColaArreglo(3)
try:
    c3.dequeue()
    chequear("dequeue en cola vacia tira error", False)
except Exception:
    chequear("dequeue en cola vacia tira error", True)

c4 = ColaArreglo(4)
for v in [1, 2, 3]:
    c4.enqueue(v)
chequear("FIFO: sale primero el que entro primero", c4.dequeue() == 1)

print("\nPILA - casos limite")
p = PilaArreglo(3)
chequear("pila nueva arranca con top = -1", p.top == -1)
try:
    p.pop()
    chequear("pop en pila vacia tira error", False)
except Exception:
    chequear("pop en pila vacia tira error", True)

p.push(1); p.push(2); p.push(3)
try:
    p.push(4)
    chequear("push en pila llena tira error", False)
except Exception:
    chequear("push en pila llena tira error", True)

chequear("LIFO: sale el ultimo que entro", p.pop() == 3)
chequear("top bajo a 1", p.top == 1)
chequear("el 3 sigue en el arreglo como basura", p.pila[2] == 3)
chequear("pero el contenido valido no lo incluye", p.contenido() == [1, 2])

print("\nPILA - se vacia y se vuelve a llenar")
p2 = PilaArreglo(3)
p2.push("a"); p2.pop()
chequear("despues de vaciarse vuelve a top = -1", p2.top == -1)
p2.push("b")
chequear("el push pisa la basura anterior", p2.pila[0] == "b")

print("\nLISTA - casos limite")
l = ListaEnlaceSimple()
chequear("lista nueva esta vacia", l.vacia())
chequear("longitud 0", l.longitud() == 0)
chequear("eliminar en lista vacia devuelve False", l.eliminar(1) is False)
chequear("buscar en lista vacia devuelve -1", l.buscar(1) == -1)

l.insertar_ordenado(5)
chequear("insertar_ordenado en lista vacia", l.contenido() == [5])
l.insertar_ordenado(1)
chequear("insertar menor -> va al principio", l.contenido() == [1, 5])
l.insertar_ordenado(9)
chequear("insertar mayor -> va al final", l.contenido() == [1, 5, 9])
l.insertar_ordenado(3)
chequear("insertar en el medio", l.contenido() == [1, 3, 5, 9])

chequear("eliminar el primero", l.eliminar(1) and l.contenido() == [3, 5, 9])
chequear("eliminar el ultimo", l.eliminar(9) and l.contenido() == [3, 5])
chequear("eliminar uno del medio", l.eliminar(5) and l.contenido() == [3])
chequear("eliminar el unico que quedaba", l.eliminar(3) and l.vacia())

print("\nARREGLO K-DIMENSIONAL - funcion h y recorrido lineal")
A = ArregloKD([4, 5, 2, 25, 85])
chequear("saltos correctos (producto de las dims que siguen)",
         A.saltos == [21250, 4250, 2125, 85, 1])
chequear("total de celdas = 4*5*2*25*85 = 85000", A.total == 85000)
chequear("h(2,3,1,7,40) = 58010", A.h([2, 3, 1, 7, 40]) == 58010)
chequear("h^-1(58010) = (2,3,1,7,40)", A.h_inv(58010) == [2, 3, 1, 7, 40])
chequear("h(0,0,0,0,0) = 0", A.h([0, 0, 0, 0, 0]) == 0)
chequear("h de la ultima celda = total-1",
         A.h([3, 4, 1, 24, 84]) == A.total - 1)
chequear("fijando piso y bloque quedan 4*2*25 = 200 celdas",
         len(list(A.direcciones({1: 3, 4: 40}))) == 200)
chequear("fijando todo menos el aula quedan 25 celdas",
         len(list(A.direcciones({0: 2, 1: 3, 2: 1, 4: 40}))) == 25)
chequear("las 25 celdas del aula estan separadas de a 85 (salto del aula)",
         sorted(A.direcciones({0: 2, 1: 3, 2: 1, 4: 40}))[1] -
         sorted(A.direcciones({0: 2, 1: 3, 2: 1, 4: 40}))[0] == 85)
chequear("sin fijar nada recorre todo el arreglo, sin repetir",
         len(set(A.direcciones({}))) == A.total)


B = ArregloKD([2, 3, 2, 4, 3])
todo_ok = True
for r in range(6):
    for combo in itertools.combinations(range(5), r):
        fijos = {j: 1 % B.dims[j] for j in combo}
        obtenido = sorted(B.direcciones(fijos))
        esperado = sorted(B.h(list(c))
                          for c in itertools.product(*[range(d) for d in B.dims])
                          if all(c[j] == v for j, v in fijos.items()))
        if obtenido != esperado:
            todo_ok = False
chequear("direcciones() coincide con fuerza bruta en las 32 combinaciones",
         todo_ok)

print("\n" + "=" * 50)
if fallos == 0:
    print("TODAS LAS PRUEBAS PASARON")
else:
    print(f"HAY {fallos} PRUEBA(S) FALLIDA(S)")
