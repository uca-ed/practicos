#Minimal: nadia apunta a el
#En la matriz de adyacencia dirigiada, la fila representa hacia
#donde apunta el nodo y la columna representa quienes apuntan al nodo.
def BuscarMinimal(arr):
    count=0
    col=0
    fila=0
    minimales=[]
    while(fila<len(arr) and col<len(arr)):
        
        if(int(arr[fila][col]) == 0):
            count+=1
            fila+=1
            if(count==len(arr)):
                minimales.append(col+1)
                col+=1
                count=0
                fila=0
        else:
            col+=1
            count=0
            fila=0
            
    return minimales
#Maximal: no apunta a nadie
def BuscarMaximal(arr):
    count=0
    col=0
    fila=0
    maximales=[]
    while(fila<len(arr) and col<len(arr)):
        
        if(int(arr[fila][col]) == 0):
            count+=1
            col+=1
            if(count==len(arr)):
                maximales.append(fila)
                fila+=1
                count=0
                col=0
        else:
            fila+=1
            count=0
            col=0
            
    return maximales

#Vecindad Derecha
def BuscarVecindadDer(arr):
    pos=[]
    for fila in range(len(arr)):
        for dato in range(len(arr[fila])):
            if(dato>fila and int(arr[fila][dato])==1):
                #encontre vecindad derecha
                print(fila,dato)
                tupla=fila,dato
                pos.append(tupla)
    return pos


def BuscarVecindadIz(arr):
    pos=[]
    for fila in range(len(arr)):
        for dato in range(len(arr[fila])):
            if (dato < fila and int(arr[fila][dato]) == 1):
                #encontre vecindad izquierda
                print(fila,dato)
                tupla=fila,dato
                pos.append(tupla)
    return pos




def main():
    with open("archivosEjemplos/archivos_ej1/02.csv", "r") as f:
        ##print(f.read())
        datos = f.read()

    arr = []
    lista=[]
    for d in datos:
        if(d=='\n'):
            arr.append(lista)
            lista=[]
        elif(d!=','):
            lista.append(d)
    print("Vecindad Derecha: ")
    print(BuscarVecindadDer(arr))
    print("  ")
    print("  ")
    print("Vecindad Izquierda:   ")
    print(BuscarVecindadIz(arr))
    print("  ")
    print("  ")
    print("Minimales: ")
    print(BuscarMinimal(arr))
    print("  ")
    print("  ")
    print("Maximales: ")
    print(BuscarMaximal(arr))
    


main()