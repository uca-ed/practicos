#3) listas por medio de celdas con enlaces simples 
lista=[]
inicio=-1
def agregar_al_inicio(valor):
    global lista,inicio
    nuevo_nodo=(valor,inicio)
    lista.append(nuevo_nodo)
    inicio=len(lista)-1

def mostrar_lista():
    global lista,inicio
    i=inicio
    print("Lista enlazada: ", end=" ")
    while i != -1:
        print(f"({lista[i][0]} -> {lista[i][1]})", end=" ")
        i = lista[i][1]
    print("None")
