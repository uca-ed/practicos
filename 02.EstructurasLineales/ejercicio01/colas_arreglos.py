
def crearCola(capacidad):
    cola = [None]*capacidad
    first = 0 
    long = 0 
    return cola, first, long

def enqueue(cola, first, long, capacidad, valor):
    if long == capacidad:
        print('Cola llena')
    else:
        posicionNueva = (first+long)%capacidad
        cola[posicionNueva] = valor
        long+=1
    return long 

def dequeue(cola, first, long, capacidad):
    if long == 0:
        print('Cola vacia!')
        return None, first, long
    else:
        rta = cola[first]
        first = (first+1)%capacidad
        long-=1
        return rta, first, long

    

def main():
    capacity = 10 
    colita, first, long = crearCola(capacity)

    archivo = open("colas_operations.txt")
    for linea in archivo:
        datos = linea.strip().split(",")
        operacion = datos[0]
    
        if operacion == "ENQUEUE":
            long = enqueue(colita, first, long, capacity, datos[1])
            
        elif operacion == "DEQUEUE":
            rta, first, long = dequeue(colita, first, long, capacity)
            print("DEQUEUE = " + rta)
            
    archivo.close()

    print('----RESULTADOS----------')
    i = first
    for j in range(long):
        print(colita[i])
        i = (i+1)%capacity

    

main()