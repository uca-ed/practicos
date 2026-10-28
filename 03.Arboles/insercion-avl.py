import sys

# nodo = [clave,izquierdo,derecho,altura]

def crear_nodo(clave):
    return [clave, None, None, 1]  # una hoja tiene altura 1

def leer_arbol_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-16') as archivo:
        arbol = [int(linea.strip()) for linea in archivo]
    return arbol

def altura(nodo):
    if nodo is None:
        return 0
    return nodo[3]

def actualizar_altura(nodo):
    nodo[3] = 1 + max(altura(nodo[1]), altura(nodo[2]))

def factor_balanceo(nodo):
    return altura(nodo[2]) - altura(nodo[1])

def rotar_izquierda(a):
    b = a[2]
    a[2] = b[1]
    b[1] = a
    actualizar_altura(a)
    actualizar_altura(b)
    return b  # b pasa a ser la raíz de este subárbol

def rotar_derecha(a):
    b = a[1]
    a[1] = b[2]
    b[2] = a
    actualizar_altura(a)
    actualizar_altura(b)
    return b

def insertar(nodo, clave):
    if nodo is None:
        return crear_nodo(clave)
    if clave < nodo[0]:
        nodo[1] = insertar(nodo[1], clave)
    elif clave > nodo[0]:
        nodo[2] = insertar(nodo[2], clave)
    else:
        return nodo  # si el número ya está, no se inserta

    actualizar_altura(nodo)
    balance = factor_balanceo(nodo)

    if balance == -2:                                  # cargado a la izquierda
        if factor_balanceo(nodo[1]) > 0:       # zigzag: rotación doble
            nodo[1] = rotar_izquierda(nodo[1])
        return rotar_derecha(nodo)

    if balance == 2:                                   # cargado a la derecha
        if factor_balanceo(nodo[2]) < 0:         # zigzag: rotación doble
            nodo[2] = rotar_derecha(nodo[2])
        return rotar_izquierda(nodo)

    return nodo

def mostrar(raiz):
    nivel = [raiz]
    while nivel != []:
        renglon = ""
        siguiente = []
        for nodo in nivel:
            renglon = renglon + f"{nodo[0]}({factor_balanceo(nodo)})   "
            if nodo[1] is not None:
                siguiente.append(nodo[1])
            if nodo[2] is not None:
                siguiente.append(nodo[2])
        print(renglon.center(80))
        nivel = siguiente

def main():
    nombre_archivo = "datos.txt"
    if len(sys.argv) > 1:
        nombre_archivo = sys.argv[1]
    claves = leer_arbol_desde_archivo(nombre_archivo)
    raiz = None
    for clave in claves:
        raiz = insertar(raiz, clave)
    mostrar(raiz)

if __name__ == "__main__":
    main()
