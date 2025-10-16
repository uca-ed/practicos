#2) pila sobre arreglos
pila=[]
top=-1
MAX=0
def constructor(tam):
    global pila,top,MAX
    MAX=tam
    pila=[None]*MAX
    top=-1
def push(valor):
    global pila, top,MAX
    if(top<MAX-1):
        top+=1
        pila[top]=valor
    else:
        print("Pila llena")
def pop():
    global pila, top
    if top>=0:
        res=pila[top]
        top-=1
        return res
    else:
        print("Pila vacia")
        return None
def mostrar_pila():
    global pila, top
    if top == -1:
        print("La pila esta vacia.")
    else:
        print("Contenido final de la pila:")
        for i in range(top, -1, -1):
            print(pila[i])


def procesar_archivo_pila(nombre_archivo,tam):
    constructor(tam)
    with open(nombre_archivo, "r") as f:
        for linea in f:
            partes = linea.strip().split()
            if len(partes) == 0:
                continue

            operacion = partes[0].upper()

            if operacion == "PUSH" and len(partes) > 1:
                valor = int(partes[1])
                push(valor)
            elif operacion == "POP":
                valor_desapilado=pop()
                if valor_desapilado is not None:
                    print(f"Elemento desapilado: {valor}")
            else:
                print(f"Operacion invalida: {linea.strip()}")
    mostrar_pila()
if __name__ == '__main__':
    try:
        tam_pila = int(input("Ingrese el tamaño máximo de la pila: "))
        procesar_archivo_pila("operaciones_pila.txt", tam_pila)
    except FileNotFoundError:
        print("Error: El archivo 'operaciones_pila.txt' no se encontró.")
    except ValueError:
        print("Error: Ingrese un número válido para el tamaño de la pila.")
