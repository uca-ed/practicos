####################################################
#########            EJERCICIO 1           #########
####################################################
print("\nEJERCICIO 1\n")

def procesar_cola(nombre_archivo):
    pos=0
    longitud=0
    cola = [None]*5
    archivo=open(nombre_archivo,"r")
    
    for linea in archivo:
        linea=linea.strip().split(',')
        if linea[0] == "ENQUEUE":
            if(longitud<len(cola)):
                cola[(pos+longitud)%len(cola)]=linea[1]
                longitud+=1
                print("Se ha encolado el valor "+linea[1])
            else:
                print("Cola llena")
                
        elif linea[0] == "DEQUEUE":
            if(longitud>0):
                rta=cola[pos]
                cola[pos]=None
                pos=(pos + 1) % len(cola)
                longitud -= 1
                print("Se ha desencolado el valor "+rta)
            else:
                print("Cola vacia")
        else:
            print("Comando inválido")
            
        print(cola)
    archivo.close()
    
procesar_cola("EJ1.txt") 
    
####################################################
#########            EJERCICIO 2           #########
####################################################
print("\nEJERCICIO 2\n")

def procesar_pila(nombre_archivo):
    top=-1
    pila = [None]*5
    archivo=open(nombre_archivo,"r")
    
    for linea in archivo:
        linea=linea.strip().split(',')
        if linea[0] == "PUSH":
            if(top<len(pila)-1):
                top+=1
                pila[top]=linea[1]
                print("PUSH del valor "+linea[1])
            else:
                print("Pila llena")
                
        elif linea[0] == "POP":
            if(top>-1):
                rta=pila[top]
                pila[top]=None
                top -= 1
                print("POP del valor "+rta)
            else:
                print("Pila vacia")
        else:
            print("Comando inválido")
            
        print(pila)
    archivo.close()

procesar_pila("EJ2.txt")

####################################################
#########            EJERCICIO 3           #########
####################################################
print("\nEJERCICIO 3\n")

class Celda:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def procesar_lista(nombre_archivo):
    cabeza = None
    
    try:
        archivo = open(nombre_archivo, "r")
        for linea in archivo:
            linea = linea.strip().split(',')
            comando = linea[0]
            
            if comando == "INSERTAR":
                valor = linea[1]
                nueva_celda = Celda(valor)
                nueva_celda.siguiente = cabeza
                cabeza = nueva_celda
                print("Se insertó el valor " + valor)
                
            elif comando == "ELIMINAR":
                if cabeza is not None:
                    rta = cabeza.dato
                    cabeza = cabeza.siguiente
                    print("Se eliminó el valor " + rta)
                else:
                    print("Lista vacía, no hay nada que eliminar")
                    
            else:
                print("Comando inválido")
            
            actual = cabeza
            estado = []
            while actual is not None:
                estado.append(actual.dato)
                actual = actual.siguiente
            estado.append("None")
            
            print("Estado: " + " -> ".join(estado))
            
        archivo.close()
    except FileNotFoundError:
        print("El archivo " + nombre_archivo + " no existe. Crealo para probar.")

procesar_lista("EJ3.txt")
##############################################
############       EJERCICIO 4      ##########
##############################################

def radix_sort(palabras):
    if not palabras:
        return []
        
    p = max(len(palabra) for palabra in palabras)
    Q = palabras.copy()
    
    for j in range(p - 1, -1, -1):
        colas = [[] for _ in range(256)]
        
        while len(Q) > 0:
            X = Q.pop(0)
            
            if j < len(X):
                valor_caracter = ord(X[j])
            else:
                valor_caracter = 0
                
            colas[valor_caracter].append(X)
            
        for cola in colas:
            Q.extend(cola)
            
    return Q

def procesar_radix(nombre_archivo):
    try:
        archivo = open(nombre_archivo, "r", encoding="utf-8")
        palabras = []
        for linea in archivo:
            palabra = linea.strip()
            if palabra:
                palabras.append(palabra)
        archivo.close()
        
        print("Palabras leidas:")
        print(palabras)
        
        palabras_ordenadas = radix_sort(palabras)
        
        print("\nPalabras ordenadas:")
        for palabra in palabras_ordenadas:
            print(palabra)
            
    except FileNotFoundError:
        print("El archivo " + nombre_archivo + " no existe.")

procesar_radix("EJ4.txt")
