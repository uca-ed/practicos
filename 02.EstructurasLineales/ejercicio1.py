#1) cola sobre arreglos
cola=[]
frente=-1
atras=-1
MAX=0

def constructor(tam):
    global cola, frente, atras,MAX
    MAX= tam
    cola=[None]*MAX
    frente=-1
    atras=-1

def enqueue(valor):
    global cola, frente, atras,MAX
    if atras<MAX-1:
        if (frente==-1):
            frente=0
        atras+=1
        cola[atras]=valor
    else:
        print("Cola llena")
def dequeue():
    global cola,frente,atras
    if(frente!=-1):
        res=cola[frente]
        if (frente==atras):
            frente=-1
            atras=-1
        else:
            frente+=1
        return res
    else:
        print("Cola vacia")
        return None

def mostrar_cola():
    global cola,frente,atras
    if frente==-1:
        print("Cola vacia")
    else:
        print("Contenido final de la cola:")
        for i in range(frente, atras + 1):
            print(cola[i], end=" ")
        print()
def procesar_operaciones_cola(nombre_archivo, tam):
    constructor(tam)
    with open(nombre_archivo, 'r') as f:
        for linea in f:
            partes = linea.strip().split()
            if not partes:
                continue
            operacion = partes[0].upper()

            if operacion == "ENQUEUE" and len(partes) == 2:
                enqueue(int(partes[1]))
            elif operacion == "DEQUEUE":
                valor=dequeue()
                if valor is not None:
                    print(f"Elemento desencolado: {valor}")
            else:
                print("Operacion invalida:", linea.strip())
    mostrar_cola()

if __name__ == "__main__":
    try:
        tam = int(input("Ingrese el tamaño máximo de la cola: "))
        procesar_operaciones_cola("operaciones.txt", tam)
    except FileNotFoundError:
        print("Error: El archivo 'operaciones.txt' no se encontró.")
    except ValueError:
        print("Error: Ingrese un número válido para el tamaño de la cola.")
