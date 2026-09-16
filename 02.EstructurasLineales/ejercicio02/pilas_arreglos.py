
def crearPila(tamanio):
    pila = [None]*tamanio
    top = -1

    return pila, top

def push(pila, top, valor):
    if (top < (len(pila)-1)):
        top+=1
        pila[top] = valor
    else:
        print("Error1!")
        
    return top

def pop(pila, top):
    if top>-1:
        rta = pila[top]
        top -= 1
        return rta, top
    else:
        print("Error2!")
        return None, top

def main():

    pila, tope = crearPila(10)


    archivo = open("pilas_operations.txt")
    for linea in archivo:
        datos = linea.strip().split(",")
        operacion = datos[0]
    
        if operacion == "PUSH":
            tope = push(pila, tope, datos[1])
        elif operacion == "POP":
            valor, tope = pop(pila, tope)
            print("push = " + valor)
    archivo.close()

    print("------RESULTADOS-------------")
    for i in range(tope+1):
        print(pila[i])

main()

