import sys

def leer_arbol_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-16') as archivo:
        arbol = [int(linea.strip()) for linea in archivo]
    return arbol

def barrido_simetrico(arbol):
    visitados=[]
    stack=[]
    if len(arbol) == 0:
        return visitados

    stack.append((0, 0))
    while(stack!=[]):
        (x,estado)=stack.pop()
        hijo_izquierdo=2*x +1
        hijo_derecho=2* x +2
        if(estado==0):
            stack.append((x,1))
            if hijo_izquierdo<len(arbol):
                stack.append((hijo_izquierdo, 0))
        else:
            visitados.append(arbol[x])
            if hijo_derecho < len(arbol):
                stack.append((hijo_derecho, 0))
    return visitados


def main():
    arbol = leer_arbol_desde_archivo(sys.argv[1])
    resultado_barrido=barrido_simetrico(arbol)
    for i in range(len(resultado_barrido)):
        print(f"{resultado_barrido[i]}")


if __name__=="__main__":
    main()