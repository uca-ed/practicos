import sys 

def leer_arbol_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        arbol = [int(linea.strip()) for linea in archivo]
    return arbol

def  barrido_post_orden(arbol,r):
    S = [(0,0)]
    while S:
        x,e=S.pop()
        if e ==0: 
            S.append((x,1))
            for i in range(r,0,-1):
                hijo = r * x + i
                if hijo < len(arbol):
                    S.append((hijo,0))
        else:
            print(arbol[x])


def main():
    r = int(sys.argv[1])
    arbol = leer_arbol_desde_archivo((sys.argv[2]))

    barrido_post_orden(arbol, r)
main()