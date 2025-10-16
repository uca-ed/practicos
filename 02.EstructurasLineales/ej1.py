def operarCola(nombreArchivo):
    archivo=open(nombreArchivo,"r")
    cola=[]
    for linea in archivo:
        linea=linea.strip().split()
        opcion=linea[0].upper()
        if opcion=="ENQUEUE":
            valor=linea[1]
            cola.append(valor)
        
        elif opcion=="DEQUEUE":
            if len(cola)>0:
                cola.pop(0)
            else:
                print("Error: Cola vacía")
                
    return cola
    archivo.close()

def main():
    colaRes=operarCola("operacionesCola.txt")
    for val in colaRes:
        print(val)

main()
