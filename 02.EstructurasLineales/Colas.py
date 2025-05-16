#Representar colas sobre un arreglo.El algoritmo debe leer el archivo de
#operaciones sobre colas y operar,partiendo de una cola vacía.
#Se debe mostrar el resultado final.

tamanio_cola = 25  # tamaño máximo de la cola

def inicializar_cola():
    return [None] * tamanio_cola, 0, 0  

def esta_vacia(inicio, fin):
    return inicio == fin

def esta_llena(fin):
    return fin == tamanio_cola

def enqueue(cola, valor, fin):
    if esta_llena(fin):
        print("Cola llena. No se puede ENQUEUE.")
        return fin
    cola[fin] = valor
    return fin + 1

def dequeue(cola, inicio, fin):
    if esta_vacia(inicio, fin):
        print("Cola vacía. No se puede DEQUEUE.")
        return inicio
    cola[inicio] = None  
    return inicio + 1

def main():
    #Inicializo la cola:
    cola, inicio_cola, fin_cola = inicializar_cola()
    
    # La funcion enqueue devuvle solamante el valor de fin, ya  que
    # savl en la primera iteracion este no se modifica. En la primera
    # iteracion fin == inicio
    
    #Lo mismo con dequeue pero con inicio.
    
    fin_cola = enqueue(cola,10,fin_cola)
    fin_cola = enqueue(cola,15,fin_cola)
    #fin_cola = enqueue(cola,10,fin_cola)
    inicio_cola = dequeue(cola,inicio_cola,fin_cola)
    #inicio_cola = dequeue(cola,inicio_cola,fin_cola)
    for i in range(inicio_cola, fin_cola):
        print(cola[i])
        
main()
