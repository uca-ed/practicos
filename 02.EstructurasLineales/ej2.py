def operarPila(nombreArchivo):
    archivo=open(nombreArchivo,"r")
    pila=[]
    for linea in archivo:
        linea=linea.strip().split()
        opcion=linea[0].upper()
        
        if opcion=="PUSH":
            valor=linea[1]
            pila.append(valor)
        
        elif opcion=="POP":
            pila.pop()

    archivo.close()
    return pila 

def main():
    pilaRes=operarPila("operacionesPila.txt")
    for val in pilaRes:
        print(val)

main()