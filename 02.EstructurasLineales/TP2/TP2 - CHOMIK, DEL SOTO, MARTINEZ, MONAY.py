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
