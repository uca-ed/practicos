
class Pila():
    def __init__(self,tam):
        self.tos=-1
        self.tam=tam
        self.arr=[None]*tam

    def push(self,e):
        if(self.tos==self.tam-1):
            print("PUSH ERROR: pila llena")
        else:
            self.tos+=1
            self.arr[self.tos]=e
        
    def pop(self):
        if(self.tos==-1):
            print("POP ERROR: pila vacia")
            return None
        else:
            res=self.arr[self.tos]
            self.tos-=1
            return res
        
def leerArch(ruta):
    f=open(ruta,'r')
    while True:
        line=f.readline()
        if not line:
            break
        strline=line.strip().split(',')

    return strline
        
def operar(pila: Pila,operaciones):
    i=0
    while i<len(operaciones):
        if operaciones[i]=='+':
            i+=1
            pila.push(int(operaciones[i]))
        else:
            print(f'POP: {pila.pop()}')
        i+=1

def main():
    pila=Pila(5)

    operaciones=leerArch('/home/ignacio-berkelaar/Documents/GitHub/practicos/02.EstructurasLineales/datos1.csv')
    operar(pila,operaciones)

    #LOS ERROR SON PARA VER SI DETECTA SI ESTA VACIA O LLENA
    


if __name__=='__main__':
    main()