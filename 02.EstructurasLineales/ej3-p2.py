#Representar listas por medio de celdas con enlace simple.

def crear_celda(valor):
    return {'valor':valor,'siguiente':None}

def enlazar_celdas(origen, destino):
    origen['siguiente']=destino

def mostrar_lista(cabeza):
    actual=cabeza
    while actual is not None:
        print(f"[{actual['valor']}]", end=" -> ")
        actual=actual["siguiente"]
    print("Null")

def main():
    celda1=crear_celda(input("Ingrese el valor de la celda 1: "))
    celda2=crear_celda(input("Ingrese el valor de la celda 2: "))
    celda3=crear_celda(input("Ingrese el valor de la celda 3: "))
    cabeza=celda1
    enlazar_celdas(celda1, celda2)
    enlazar_celdas(celda2, celda3)
    mostrar_lista(cabeza)

main()