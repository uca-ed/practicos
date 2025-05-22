#Representar pilas sobre un arreglo.
#El algoritmo debe leer el archivo de operaciones sobre pilas y operar,
#partiendo de una pila vacía.
#Se debe mostrar el resultado final.

tamanio_pila = 25  # tamaño máximo de la pila

def inicializar_pila():
    return [None] * tamanio_pila, 0 

def esta_vacia(tope):
    return tope == 0

def esta_llena(tope):
    return tope == tamanio_pila

def push(pila, valor, tope):
    if esta_llena(tope):
        print("Pila llena. No se puede PUSH.")
        return tope
    pila[tope] = valor
    return tope + 1

def pop(pila, tope):
    if esta_vacia(tope):
        print("Pila vacía. No se puede POP.")
        return tope
    pila[tope - 1] = None 
    return tope - 1

def main():
    pila, tope = inicializar_pila()
    tope = push(pila,10,tope)
    tope = push(pila,15,tope)
    #tope = pop(pila,tope)

    # Mostrar pila final (de abajo hacia arriba)
    print("Resultado final de la pila:")
    for i in range(tope - 1, -1, -1):
        print(pila[i])
main()