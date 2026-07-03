#Representar pilas sobre un arreglo. El algoritmo debe leer el archivo de operaciones sobre pilas y operar, partiendo de una pila vacía. 
#Se debe mostrar el resultado final.

def push(pila,tope,valor):
    if tope<len(pila):
        tope+=1
        pila[tope]=valor
    else:
        return print("Pila llena")
    return pila

def pop(pila,tope):
    if tope>=0:
        rsta=pila[tope]
        pila.pop(tope)
        tope-=1
        return rsta
    else:
        return print("Pila vacía")

def main():
    pila=[None]*5
    tope=-1
    with open(r"C:\Users\danie\OneDrive\Documentos\estructura de datos\practica2\ej2.txt") as f:
        for linea in f:
            op=linea.split(",")
            if op[0]=="PUSH":
                pila=push(pila,tope,op[1])
                tope+=1
            elif op[0]=="POP":
                rsta=pop(pila,tope)
                tope-=1
                print(rsta)
    print(pila)

main()