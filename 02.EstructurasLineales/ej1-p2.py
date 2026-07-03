#Representar colas sobre un arreglo. El algoritmo debe leer el archivo de operaciones sobre colas y operar, partiendo de una cola vacía. 
#Se debe mostrar el resultado final.

def enqueue(cola,p,c,valor):
    if c<len(cola):
        cola[(p+c)%len(cola)]=valor
        c+=1
    return c

def dequeue(cola,p,c):
    if c>0:
        rsta=cola[p]
        cola.pop(p)
        c-=1
    else:
        rsta=None
    return rsta,p,c


def main():
    cola=[None]*5
    p=0
    c=0
    archivo=r"C:/Users/danie/OneDrive/Documentos/estructura de datos/practica2/ej1.txt"
    with open(archivo,"r") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            partes=linea.split(",")
            print(partes)
            op=partes[0]
            if "ENQUEUE" in op:
                c=enqueue(cola,p,c,partes[1])
            elif "DEQUEUE" in op:
                rsta,p,c=dequeue(cola,p,c)
                print(f"DEQUEUE obtenido: {rsta}")
    print(cola)
    print(f"Puntero al frente (p): {p}, Cantidad de elementos (c): {c}")

main()